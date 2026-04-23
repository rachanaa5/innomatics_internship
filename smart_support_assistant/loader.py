from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load text file
loader = TextLoader("knowledge_base/policies.txt")
docs = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=80
)
chunks = splitter.split_documents(docs)

# Embedding model (no API key required)
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store in ChromaDB
db = Chroma.from_documents(
    chunks,
    embedding,
    persist_directory="vector_store"
)

print("✅ Knowledge base stored successfully!")
