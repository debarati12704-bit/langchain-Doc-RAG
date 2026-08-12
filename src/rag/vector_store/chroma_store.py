from langchain_chroma import Chroma
from langchain_core.documents import Document
from rag.embeddings.embedder import get_embedding_model


PERSIST_DIRECTORY="chroma_db"

def create_vector_store(documents:list[Document])->Chroma:
    embeddings=get_embedding_model()
    vector_store=Chroma(
        collection_name="langchain_docs",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY
    )

    vector_store.add_documents(documents)
    return vector_store