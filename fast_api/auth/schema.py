from pydantic import BaseModel , Field




class Usercreate(BaseModel):
    name:str
    email :str
    password : str

class Userresponse(BaseModel):
    name:str
    email :str


class UserLogin(BaseModel):
    email : str
    password : str

class Postcreate(BaseModel): 
   
    title : str 
    description : str
    create_by : int

class Postcreate(BaseModel): 
   
    title : str 
    description : str
    create_by : int