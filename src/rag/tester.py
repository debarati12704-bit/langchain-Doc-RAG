from rag.loaders.web_loader import load_web_pages
from rag.processing.chunking import split_documents
from rag.vector_store.chroma_store import create_vector_store
from rag.generation.generator import generate_answer

DOC_URLS = [ 
    "https://docs.langchain.com/oss/python/langchain/overview", 
    "https://docs.langchain.com/oss/python/langchain/agents", 
    ]

documents=load_web_pages(DOC_URLS)
print(f"no. of documents :{len(documents)}\n\n")

chunks=split_documents(documents)
print(f"no. of chunks:{len(chunks)}\n\n")

vector_store=create_vector_store(chunks)
print("Vector Store created successfully\n\n\n")

query="What are LangChain Agents?"
results=vector_store.similarity_search(query,k=3)

print(f"\n\nQuery: {query}")
print(f"no. of results: {len(results)}\n\n")

for i,document in  enumerate(results,start=1):
    print(f"\n-----RESULT {i}-----")
    print(f"source:{document.metadata.get("source")}")
    print(document.page_content,"...\n\n\n")


answer=generate_answer(query=query,documents=results)

print("-----GENERATED ANSWER-----")
print(answer)