from langgraph.graph import StateGraph , START , END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from  pydantic import BaseModel , Field


load_dotenv()







#  model assign

llm = os.getenv("GROQ_API")
model = ChatGroq(api_key=llm , model="llama-3.3-70b-versatile")

res = model.invoke("hi how are you ")
print(res.content)


# state management

class graph_state(BaseModel):
    user_message : str = Field(default="hi ")
    ai_res :str = Field(default="no response from ai  ")


# node management


#  1 ) for input node
def input_node(state:graph_state) ->graph_state:
    print("input node activate")

    message = input("ask something : ")

    state.user_message = str(message)

    return state

#  2 ) for process
def process_node(state:graph_state) ->graph_state:
    print("process node activate")


    process = model.invoke(state.user_message)

    state.ai_res = process.content

    return state



#  3 ) for printing output 
def print_node(state:graph_state) ->graph_state:  
    print("print_node node activate")

    print(state)

    return state


# assign node 

graph = StateGraph(graph_state)

graph.add_node("input_node",input_node)
graph.add_node("process_node",process_node)
graph.add_node("print_node",print_node)


#  assign edges

graph.add_edge(START,"input_node")
graph.add_edge("input_node","process_node")
graph.add_edge("process_node","print_node")
graph.add_edge("print_node",END)


# ///////////////////////////////

final_graph = graph.compile()

print(final_graph.get_graph())
ob1 = graph_state(user_message="what is the name of india prime minister")
final_graph.invoke(ob1)






