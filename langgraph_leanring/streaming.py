from langgraph.graph import StateGraph , START , END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from  pydantic import BaseModel , Field


load_dotenv()







#  model assign

llm = os.getenv("GROQ_API")
model = ChatGroq(api_key=llm , model="llama-3.3-70b-versatile")



# state management

class graph_state(BaseModel):
    user_message : str 
    ai_res :str 


# node management


#  1 ) for input node
def input_node(state:graph_state) ->graph_state:
    print("input node activate")

    message = input("ask something : ")

    state.user_message = str(message)

    return state

#  2 ) for process

def output_node(state:graph_state) ->graph_state:
    print("output  node activate")


    process = model.invoke(state.user_message)

    state.ai_res = process.content

    return state






# assign node 

graph = StateGraph(graph_state)

graph.add_node("input_node",input_node)
graph.add_node("output_node"  , output_node)


#  assign edges

graph.add_edge(START,"input_node")
graph.add_edge("input_node","output_node")
graph.add_edge("output_node",END)


# ///////////////////////////////

final_graph = graph.compile()

ob1 = graph_state(user_message="what is the name of india prime minister",ai_res="")

for event in final_graph.stream(ob1):
     if "output_node" in event:

        print(event["output_node"]["ai_res"])
  




