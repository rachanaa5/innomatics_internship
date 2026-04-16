from langchain_openai import ChatOpenAI
from prompts.templates import eval_prompt

def get_eval_chain():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # Using LCEL pipeline 
    chain = eval_prompt | llm
    return chain