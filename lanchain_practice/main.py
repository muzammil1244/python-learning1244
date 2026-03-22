from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API")

llm = ChatGroq(api_key=api_key , model="llama-3.1-8b-instant" , streaming = True)

promt = [
    ("system","behave like your are my teacher"),
    ("user","how to control mind")
]
res = llm.stream(promt)

for chunk in res:
    print(chunk.content ,end="")