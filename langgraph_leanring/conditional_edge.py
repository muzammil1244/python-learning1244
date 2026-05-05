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
    data : int


# node management


#  1 ) for input node
def input_node(state:graph_state) ->graph_state:
    

  


    return state

#  2 ) for process
def node_one(state:graph_state) ->graph_state:
    print("data is 5")




    return state



#  3 ) for printing output 
def node_two(state:graph_state) ->graph_state:  
    print("data is 3")
   

    return state




def conditional_edges(state:graph_state):
    if state.data == 5 :
        return "node_one"
    else :
        return "node_two"




# assign node 

graph = StateGraph(graph_state)

graph.add_node("input_node",input_node)
graph.add_node("node_one",node_one)
graph.add_node("node_two",node_two)


#  assign edges

graph.add_edge(START,"input_node")
graph.add_conditional_edges("input_node",conditional_edges)
graph.add_edge("node_one",END)
graph.add_edge("node_two",END)


# ///////////////////////////////

final_graph = graph.compile()

print(final_graph.get_graph())

ob1 = graph_state(data=3)
final_graph.invoke(ob1)






