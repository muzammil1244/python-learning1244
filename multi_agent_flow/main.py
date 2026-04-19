from langchain_groq import ChatGroq
from langchain_community.tools import tool
from langgraph.graph import StateGraph , START , END
from dotenv import load_dotenv
from pydantic import BaseModel,Field
import os
from typing import Literal
from langchain.agents import create_agent




# classes

class Method_class(BaseModel):
    question :str 
    category : Literal["google_search","coding","weather"] = Field(default="google_search" )
    answer:str = Field(default="sorry....... ")


class Questioncatogery(BaseModel):
    category : Literal["google_search","coding","weather"] = Field(default="google_search")




# model diclearesion 


load_dotenv()
llm = os.getenv("API")
model = ChatGroq(api_key=llm,model="llama-3.1-8b-instant")



# ///////////


@tool
def google_search_tool(query:str) -> str:

    """
    so you are google searcher that search question on google and returns answer
    """
    return f"so yes i have searched the question and i dont know about {query} the answer"


agent = create_agent(model=model,
                     tools=[google_search_tool],
                     system_prompt="so you are a agent that search on google answers"
                     )


def check_catogery(state:Method_class) -> Method_class:
    question = state.question
    print(question,type(question))
    
    structured_llm = model.with_structured_output(Questioncatogery) 
    res = structured_llm.invoke(
        f"""
        Classify the question into ONLY one of these categories:
        - google_search
        - coding
        - weather

        Rules:
        - If unsure → return google_search
        - DO NOT return anything else

        Question: {question}
        """
    ) 

    state.category = res.category

    return state






def route(state:Method_class) -> Literal["google_search","coding","weather"]:

    return state.category



def google_search(state:Method_class) -> Method_class:
    
    res = agent.invoke({"messages":[{"role":"user","content":state.question}]})

    state.answer = res["messages"][-1].content
    return state


def weather(state:Method_class) -> Method_class:
    
    res = "the temperature 70 d"

    state.answer = res
    return state



def coding(state:Method_class) -> Method_class:
    
    res = model.invoke(f"behavio like you are coding master for any tool or languages of programming and give me the answer of this question {state.question}")

    state.answer = res.content
    return state



# agenst and tools






#  graph work

graph = StateGraph(Method_class)

graph.add_node("check_question_category",check_catogery)
graph.add_node("route",route)
graph.add_node("google_search",google_search)
graph.add_node("coding",coding)
graph.add_node("weather",weather)


# edges

graph.add_edge(START,"check_question_category")
graph.add_conditional_edges("check_question_category",route)
graph.add_edge("google_search",END)
graph.add_edge("coding",END)
graph.add_edge("weather",END)


final_graph = graph.compile()

print(final_graph.get_graph().draw_mermaid())


response = final_graph.invoke({"question":"what is is tha current date "})

print(response)