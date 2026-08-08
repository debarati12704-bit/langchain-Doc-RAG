from rag.loaders.web_loader import load_web_pages
from rag.processing.chunking import split_documents
from rag.embeddings.embedder import embed_documents

DOC_URLS = [ "https://docs.langchain.com/oss/python/langchain/overview", "https://docs.langchain.com/oss/python/langchain/agents", ]

documents=load_web_pages(DOC_URLS)
print(f"no. of documents :{len(documents)}\n\n")

chunks=split_documents(documents)
print(f"no. of chunks:{len(chunks)}")
print(f"content of first chunk:\n{chunks[0].page_content}...\n\n")

embeddings=embed_documents(chunks)
print(f"no. of embeddings:{len(embeddings)}")
print(f"embedding dimensions:{len(embeddings[0])}")
print(f"first 10 values:{embeddings[0][:10]}")