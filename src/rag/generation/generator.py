from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.documents import Document
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        temperature=0
    )

def generate_answer(
        query: str,
        documents: list[Document]
)-> str:
    context="\n\n".join(
        document.page_content
        for document in documents
    )
    prompt=f"""
You're an assistant answering questions about Langchain documents.
use provided context to answer queries.

if an answer cannot be found in the context, say:
    "I do not have enough information to answer that question."

Context:
{context}

Query:
{query}

Anwer:
"""
    model=get_llm()
    response=model.invoke(prompt)

    return response.text