from langchain_huggingface.embeddings import HuggingFaceEmbeddings
<<<<<<< HEAD
from dotenv import load_dotenv
import os
from langchain_chroma import Chroma
load_dotenv()
=======

>>>>>>> dedd904ecc751a9cb2204a6465fb71ea2f9cbda6



docs = [
  "Muzammil is a BCA student learning Artificial Intelligence and Machine Learning.",
  "React Native is a framework used to build mobile applications using JavaScript and React.",
<<<<<<< HEAD
  
=======
  "LangChain is a framework that helps in building applications using large language models.",
  "FAISS is a vector database used for similarity search and fast retrieval of embeddings.",
  "Groq provides fast inference for large language models but does not support embeddings.",
  "HuggingFace provides free embedding models like all-MiniLM-L6-v2.",
>>>>>>> dedd904ecc751a9cb2204a6465fb71ea2f9cbda6
]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query_result = embeddings.embed_documents(docs)

<<<<<<< HEAD
vector_store = Chroma.from_texts(
    texts= docs,
    embedding=embeddings,
    persist_directory="./chroma_langchain_db",  
)



query = " Muzammil Course and skills"

result = vector_store.similarity_search(query=query,k=3)

print(result)
=======
print(query_result[:3])
>>>>>>> dedd904ecc751a9cb2204a6465fb71ea2f9cbda6
