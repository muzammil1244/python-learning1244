from langchain_huggingface.embeddings import HuggingFaceEmbeddings




docs = [
  "Muzammil is a BCA student learning Artificial Intelligence and Machine Learning.",
  "React Native is a framework used to build mobile applications using JavaScript and React.",
  "LangChain is a framework that helps in building applications using large language models.",
  "FAISS is a vector database used for similarity search and fast retrieval of embeddings.",
  "Groq provides fast inference for large language models but does not support embeddings.",
  "HuggingFace provides free embedding models like all-MiniLM-L6-v2.",
]

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

query_result = embeddings.embed_documents(docs)

print(query_result[:3])
