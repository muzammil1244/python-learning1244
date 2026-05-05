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
    password : int
    is_pass : bool
    attempt : int = Field( default=0)


# node management


#  1 ) for input node

def input_node(state:graph_state) ->graph_state:
    
    state.attempt += 1
    print(f"Attempt: {state.attempt}")

   

    if state.attempt < 3:
         state.password = 1000
    else :
         state.password = 1234
    
    return state






#  2 ) for process
def node_check(state:graph_state) ->graph_state:
   
 if state.password == 1234:
   state.is_pass = True
   print(state.is_pass)
 return state



#  3 ) for printing output 
def node_message(state:graph_state) ->graph_state:  

  
            
    print("PASS WORD IS CORRECT")
   
   

    return state




def conditional_edges(state:graph_state):
    if state.is_pass :
        return "node_message"
    else :
        return "input_node"




# assign node 

graph = StateGraph(graph_state)

graph.add_node("input_node",input_node)
graph.add_node("node_message",node_message)
graph.add_node("node_check",node_check)


#  assign edges

graph.add_edge(START,"input_node")
graph.add_edge("input_node","node_check")

graph.add_conditional_edges("node_check",conditional_edges)

graph.add_edge("node_message",END)


# ///////////////////////////////

final_graph = graph.compile()

print(final_graph.get_graph())


obj = graph_state(password=0 , is_pass=False , attempt=0)
response = final_graph.invoke(obj)

print(response)






