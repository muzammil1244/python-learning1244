from fastapi import FastAPI
from pydantic import BaseModel




rs = FastAPI(title="response_model",description= " learning about response_model on Fast Api")



class Request_model(BaseModel):
    name:str
    email:str
    password:int
    age:int


class res_model(BaseModel):
    id:int
    name:str
    email:str
    age:int


@rs.post("/user/create",response_model=res_model)
def createUser(user:Request_model):
    res = {
        "id":1,
        "name":user.name,
        "email" : user.email,
        "age" : user.age
    }
    return res
