from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel , Field
import os
load_dotenv()

llm = os.getenv("GROQ_API")

model = ChatGroq(api_key=llm , model="llama-3.1-8b-instant")



prompt_modified = ChatPromptTemplate([
  {"role":"system","content":"behave like google translatar and translate the sentence into {language}"}
  ,{"role":"user","content":"{content}"}
])

def modified_response(result):
    return result.content

def transfer_into_upperCase(result):
    return result.upper()


# final_prompt = prompt_modified.format_messages(language="marathi",content = "tum hara nam kya hai ")


# # prompt_modified.invoke({"language":"marathi","content" :"tum hara nam kya hai "})

# chain = prompt_modified | model | modified_response | transfer_into_upperCase

# res = chain.invoke({"language":"marathi","content" :"tum hara nam kya hai "})

# print(res)


class structure_output(BaseModel):
    title : str = Field(description="title of the movie")
    year : int = Field(description = "year of move that made")
    director:str = Field(description="director name of move ")




moview_data = model.with_structured_output(structure_output)

res = moview_data.invoke("tell me about it movie")
print(res)