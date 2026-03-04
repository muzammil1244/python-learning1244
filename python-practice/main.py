from fastapi import FastAPI, HTTPException , BackgroundTasks
from pydantic import BaseModel
import httpx 
import json

app = FastAPI()

# basic get method
@app.get("/")
async def home():
    return {"Message":"his home"}


# res.body by pydantic


class PromptRequest(BaseModel):
    prompt: str
    


class PromptRequest2(BaseModel):
    
  title: str
  body: str
  userId: int


class ChatRequest(BaseModel):
    chat: str




# response Models 

class ChatResponse(BaseModel):
    id:int
    title:str


@app.post("/ask")
async def ask_ai(data: PromptRequest):
    return {
        "you_sent": data.prompt,
        "response": "This is fake AI response"
    }


@app.post("/chat")
async def chat_rout(chat:ChatRequest):
    return{
        "Response":{
            "req":chat.chat,
            "res":"hi this fak chat boat"
        }
    }


# api calling inside the route

@app.post("/real_chat", response_model = ChatResponse)
async def chat_with_ai(req:PromptRequest2):
    
    async with httpx.AsyncClient() as client:
        response = await client.post("https://jsonplaceholder.typicode.com/posts",
                                     json = {
                                         "title":req.title,
                                         "body":req.body,
                                         "userId":req.userId
                                     })
 
    data = response.json()
    return { "id": data["id"],
        "title": data["title"]} 
    
# Error Handling 


@app.post("/error/handling")
async def error_handling():
    num = 0

    if num < 1 :
       raise HTTPException(
           status_code = 500,
           detail = "num is less then 1"
       )

    return {"message":"Id is successfully collected"}
    

# background task writing response and request

class RQStoreHistory(BaseModel):
    req : str


class RSStoreHistory(BaseModel):
    res:str

def data_base(req:str , res:str):
    with open("history.txt","a",) as f:
      json.dump({"req": req, "res": res}, f)
@app.post("/write/history",response_model = RSStoreHistory)
async def write_history(req:RQStoreHistory , background_tasks:BackgroundTasks):


    ress = "hi this is fake ai response "

    if not ress :
     
     raise HTTPException(
           status_code = 500,
           detail = " resposen not found from fak ai "
       )
    
    background_tasks.add_task(data_base,req.req , ress)
    return{
        "res":ress
    }
# sfsfsfsffsfd