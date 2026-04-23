def build_prompt(context, query, intent):
    return f"""
You are a polite and professional support assistant.

Detected Intent: {intent}

Use the following context to answer clearly:

Context:
{context}

Customer Question:
{query}

Final Answer:
"""
