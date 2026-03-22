from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_community.document_loaders import PyPDFLoader , TextLoader
load_dotenv()


llm = os.getenv("GROQ_API")

model = ChatGroq(api_key=llm , model="llama-3.1-8b-instant")

load_text = TextLoader(file_path="./texxt.txt",)

text_data = load_text.load()

print(text_data)