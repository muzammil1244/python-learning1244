from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API")

llm = ChatGroq(api_key=api_key , model="llama-3.1-8b-instant")

promt = [
    ("system","behave like your are my teacher"),
    ("user","how to control mind")
]
res = llm.invoke(promt)

print(res.content)