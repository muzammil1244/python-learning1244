from pydantic import BaseModel
from langgraph.graph import StateGraph,START,END


# Message_class
class Message_class(BaseModel):
    message:str="",



graph = StateGraph(Message_class)

# functions


def Greet(state:Message_class):
    state.message = f"hi how are you {state.message}"
    return state

def Upper(state:Message_class):
    state.message = state.message.upper()
    return state

graph.add_node("greet",Greet)
graph.add_node("upper",Upper)

graph.add_edge(START,"greet")
graph.add_edge("greet","upper")
graph.add_edge("upper",END)

final_grap = graph.compile()


res = final_grap.invoke({"message":"muzammil"})

print(res)


