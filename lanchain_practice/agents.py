from langchain_groq import ChatGroq
from langchain.agents import create_agent
import os
from langchain.tools import tool

from dotenv import load_dotenv


load_dotenv()
llm = os.getenv("GROQ_API")
serper_api = os.getenv("SERPER_API")

model = ChatGroq(
    api_key=llm,
model="llama-3.1-8b-instant")

from langchain_community.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper(serper_api_key = serper_api)




def search_tool(query: str) -> str:
    """Search the internet"""
    return search.run(query)


agent1 = create_agent(model,tools = [search_tool])

res = agent1.invoke({
    "messages": [
        {"role": "user", "content": "what is the height of Burj Khalifa"}
    ]
})
print(res)