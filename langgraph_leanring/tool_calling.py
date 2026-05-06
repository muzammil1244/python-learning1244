from langgraph.graph import StateGraph , START , END
from langchain_groq import ChatGroq
from langchain.tools import tool
from dotenv import load_dotenv
import os
from pydantic import BaseModel 
from typing import List , Literal

# llm 

load_dotenv()

llm = os.getenv("GROQ_API")

model  = ChatGroq(api_key =llm, model="llama-3.3-70b-versatile")


# graph setup

class graph_state(BaseModel):
    question : str
    output:str
    tool : List[str]


class structure_output_class(BaseModel):
     tool : List[Literal["calculate","weather","google_search"]]
     


graph = StateGraph(graph_state)


# nodes and tools


def question_node(state:graph_state):
    print("input node executed")
    qna = input("ask some thing")
    state.question = str(qna)
    return state

def identify_tools(state:graph_state):
      print(" identify tool node executed ")
      qna2 = state.question

      structure_model = model.with_structured_output(structure_output_class)
      res = structure_model.invoke(f"""
You are an AI tool selector.

Available tools:
- calculate
- weather
- google_search

Question: {state.question}

Return ONLY valid JSON:
{{
  "tool": ["calculate"]
}}
""")
      print("output from the identify tool ",res)

      state.tool = res.tool
      return state
 
def calculate(state:graph_state):
     
     print("calculate node executed")
     qna3 = state.question
     res = model.invoke(f"you are my calculatere that calculate the value {qna3} ")
     state.output = res.content
     return state


def weather(state:graph_state):
     
     print("weather node executed")
     qna3 = state.question
    
     state.output = "the today weather is sunny "
     return state

def google_search(state:graph_state):
     
     print("google_search node executed")
     qna3 = state.question
     state.output = "ok so i have google searched and this is the response from google searched"
     return state
     
def conditional_node(state: graph_state):
    if not state.tool:
        return "google_search"

    tool = state.tool[0]

    if tool == "calculate":
        return "calculate"
    elif tool == "weather":
        return "weather"
    else:
        return "google_search"
     

graph.add_node("input_node",question_node)
graph.add_node("identify_tools",identify_tools)
graph.add_node("calculate",calculate)
graph.add_node("weather",weather)
graph.add_node("google_search",google_search)

graph.add_edge(START,"input_node")
graph.add_edge("input_node","identify_tools")
graph.add_conditional_edges("identify_tools",conditional_node)
graph.add_edge("calculate",END)
graph.add_edge("weather",END)
graph.add_edge("google_search",END)


final_graph = graph.compile()

ob = graph_state(question="",output="",tool=[""])

respones = final_graph.invoke(ob)

print(respones)









