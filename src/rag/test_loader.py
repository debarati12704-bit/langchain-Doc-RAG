from rag.loaders.web_loader import load_web_pages
from rag.processing.chunking import split_documents

urls = [
    "https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/langchain/agents",
]

documents = load_web_pages(urls)

print("Number of documents:", len(documents))

chunks=split_documents(documents)

print(f"no. of chunks:{len(chunks)}")
for i,chunk in enumerate(chunks[:2]):
    print(f"\n\n-----Chunk{i+1}-----")
    print(f"Chunk content:{chunk.page_content}")
    print(f"Chunk metadata: {chunk.metadata["source"]}")
    print(f"Characters in chunk :{len(chunk.page_content)}")