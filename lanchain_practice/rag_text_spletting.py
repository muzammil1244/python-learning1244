from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from langchain_community.document_loaders import PyPDFLoader , TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv()


llm = os.getenv("GROQ_API")

model = ChatGroq(api_key=llm , model="llama-3.1-8b-instant")

load_text = TextLoader(file_path="./texxt.txt",)

text_data = load_text.load()

print(text_data)



splitter_model = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20 )

splitter_data = splitter_model.split_text(text_data[0].page_content)

print(splitter_data)