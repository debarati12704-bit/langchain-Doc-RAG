from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document 

def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
def embed_documents(documents:list[Document])->list[list[float]]:
    model=get_embedding_model()
    text=[document.page_content for document in documents]
    return model.embed_documents(text)