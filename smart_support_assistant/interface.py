import streamlit as st
from langchain_chroma import Chroma
from dashboard import setup_metrics, record_query, record_escalation
from router import classify_intent, needs_escalation
from helpers import build_prompt
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings

st.set_page_config(page_title="Smart Support Assistant", layout="wide")

setup_metrics()

st.sidebar.header("📊 Support Analytics")
st.sidebar.metric("Queries", st.session_state.total_queries)
st.sidebar.metric("Escalations", st.session_state.human_escalations)

st.title("💡 Smart Support Assistant")
st.caption("RAG + Intent Routing + HITL")

@st.cache_resource
def init_system():
    db = Chroma(collection_name="support_kb", persist_directory="./vector_store")
    llm = Ollama(model="llama3", temperature=0)
    return db, llm

db, llm = init_system()

if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

for msg in st.session_state.chat_log:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

query = st.chat_input("Type your support question...")

if query:
    record_query()
    st.session_state.chat_log.append({"role": "user", "content": query})

    docs = db.similarity_search(query, k=3)
    intent = classify_intent(query)

    if needs_escalation(query, docs):
        record_escalation()
        response = "⚠️ Escalated to human support team."
    else:
        context = "\n".join([doc.page_content for doc in docs])
        prompt = build_prompt(context, query, intent)
        response = llm.invoke(prompt)

    with st.chat_message("assistant"):
        st.write(response)
        st.info(f"Intent: {intent}")

    st.session_state.chat_log.append({"role": "assistant", "content": response})
