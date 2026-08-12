from rag.loaders.web_loader import load_web_pages
from rag.processing.chunking import split_documents
from rag.vector_store.chroma_store import create_vector_store
from rag.generation.generator import generate_answer

DOCS=[
    "https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/langchain/install",
    "https://docs.langchain.com/oss/python/langchain/quickstart",
    "https://docs.langchain.com/oss/python/langchain/philosophy",
    "https://docs.langchain.com/oss/python/langchain/agents",
    "https://docs.langchain.com/oss/python/langchain/models",
    "https://docs.langchain.com/oss/python/langchain/messages",
    "https://docs.langchain.com/oss/python/langchain/tools",
    "https://docs.langchain.com/oss/python/langchain/short-term-memory",
    "https://docs.langchain.com/oss/python/langchain/event-streaming",
    "https://docs.langchain.com/oss/python/langchain/streaming",
    "https://docs.langchain.com/oss/python/langchain/structured-output",
    "https://docs.langchain.com/oss/python/langchain/middleware/overview",
    "https://docs.langchain.com/oss/python/langchain/middleware/built-in",
    "https://docs.langchain.com/oss/python/langchain/middleware/custom",
    "https://docs.langchain.com/oss/python/langchain/guardrails",
    "https://docs.langchain.com/oss/python/langchain/runtime",
    "https://docs.langchain.com/oss/python/langchain/context-engineering",
    "https://docs.langchain.com/oss/python/langchain/mcp",
    "https://docs.langchain.com/oss/python/langchain/human-in-the-loop",
    "https://docs.langchain.com/oss/python/langchain/multi-agent/index",
    "https://docs.langchain.com/oss/python/langchain/long-term-memory",
    "https://docs.langchain.com/oss/python/langchain/frontend/overview",
    "https://docs.langchain.com/oss/python/langchain/studio",
    "https://docs.langchain.com/oss/python/langchain/test",
    "https://docs.langchain.com/oss/python/langchain/ui",
    "https://docs.langchain.com/oss/python/langchain/deploy",
    "https://docs.langchain.com/oss/python/langchain/observability"
    ]

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