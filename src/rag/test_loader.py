from rag.loaders.web_loader import load_web_pages


urls = [
    "https://docs.langchain.com/oss/python/langchain/overview",
    "https://docs.langchain.com/oss/python/langchain/agents",
]

documents = load_web_pages(urls)

print("Number of documents:", len(documents))

for document in documents:
    print("\nSource:", document.metadata["source"])
    print("Characters:", len(document.page_content))
    print("content:", document.page_content[:100],"...")