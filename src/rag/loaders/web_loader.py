from langchain_core.documents import Document
import requests
from bs4 import BeautifulSoup


def load_web_page(url: str) -> Document:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    for element in soup(["script", "style", "nav", "header", "footer"]):
        element.decompose()

    text = soup.get_text(separator="\n", strip=True)

    return Document(
        page_content=text,
        metadata={"source": url},
    )


def load_web_pages(urls: list[str]) -> list[Document]:
    documents = []

    for url in urls:
        try:
            document = load_web_page(url)
            documents.append(document)

        except requests.RequestException as e:
            print(f"Request failed at {url} with {e}")

    return documents