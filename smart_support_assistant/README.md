# Smart Support Assistant

## Overview
Smart Support Assistant is a customer support automation project built with Retrieval-Augmented Generation (RAG). It retrieves company policy data, detects query intent, and generates accurate responses using a local LLM. Sensitive queries are escalated to human support.

## Features
- RAG-based question answering
- Intent detection (refund, shipping, cancellation, exchange, complaint)
- Human-in-the-loop escalation
- Analytics dashboard
- Chat memory/history

## Tech Stack
- Python
- Streamlit
- LangChain
- ChromaDB
- OpenAI / Ollama
- Sentence Transformers

## Setup
```bash
py -m venv env
env\Scripts\activate
pip install -r requirements.txt
python loader.py
streamlit run interface.py
