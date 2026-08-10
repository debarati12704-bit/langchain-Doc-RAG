from rag.loaders.web_loader import load_web_pages
from rag.processing.chunking import split_documents
from rag.vector_store.chroma_store import create_vector_store
from rag.generation.generator import generate_answer

DOCS=["https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/langchain/agents"]

def create_pipeline():
    documents=load_web_pages(DOCS)
    chunks=split_documents(documents)
    vector_store=create_vector_store(chunks)

    return vector_store

def ask_question(
        vector_store,
        query: str,
        k: int=3
)-> str:
    results=vector_store.similarity_search(query,k=3)
    answer=generate_answer(query=query,documents=results)
    return answer