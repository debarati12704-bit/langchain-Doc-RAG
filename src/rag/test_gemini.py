import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key not found")

model=ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=api_key
)


response=model.invoke("say hello in one sentence")

print(response.content)