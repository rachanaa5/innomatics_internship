import streamlit as st

def setup_metrics():
    st.session_state.setdefault("total_queries", 0)
    st.session_state.setdefault("human_escalations", 0)

def record_query():
    st.session_state.total_queries += 1

def record_escalation():
    st.session_state.human_escalations += 1
