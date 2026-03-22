from langchain_groq import ChatGroq
from langchain.agents import create_agent
import os
from langchain.tools import tool

from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver


load_dotenv()
llm = os.getenv("GROQ_API")
serper_api = os.getenv("SERPER_API")

model = ChatGroq(
    api_key=llm,
model="llama-3.1-8b-instant")

from langchain_community.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper(serper_api_key = serper_api)




@tool
def search_tool(query: str) -> str:
    """Search the internet"""
    return search.run(query)

agent1 = create_agent(
    model,
    tools=[search_tool],
    checkpointer=MemorySaver()
)
res = agent1.invoke({
    "messages": [
        {"role": "user", "content": "and the location of that"}
    ]
},   {"configurable": {"thread_id": "1"}},)


print(res["messages"][-1].content)