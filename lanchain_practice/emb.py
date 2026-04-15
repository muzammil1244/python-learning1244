from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
from langchain_chroma import Chroma
load_dotenv()



docs = [
  "Muzammil is a BCA student learning Artificial Intelligence and Machine Learning.",
  "React Native is a framework used to build mobile applications using JavaScript and React.",
  
]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query_result = embeddings.embed_documents(docs)

vector_store = Chroma.from_texts(
    texts= docs,
    embedding=embeddings,
    persist_directory="./chroma_langchain_db",  
)



query = " Muzammil Course and skills"

result = vector_store.similarity_search(query=query,k=3)

print(result)
