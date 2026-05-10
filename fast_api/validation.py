from fastapi import FastAPI
from pydantic import BaseModel



vd = FastAPI(
    title = "to learning about validation with pydantic " 
)



class createuserClass(BaseModel):
    name:str
    email:str
    age:int


@vd.post("/create/user")
def createUser(user:createuserClass):
    return{
        "message":"user created successfully",
        "data":user
    }