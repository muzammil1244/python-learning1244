from fastapi import APIRouter,Depends , HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Database import get_db
from model import User , Post
from typing import List


class UserClass(BaseModel):

    name :str
    email :str
    

class Userrsponse(BaseModel):
    name:str
    email:str

class PostClass(BaseModel):
    title : str
    create_by:int

class Post_response(BaseModel):

    title:str
    create_by : int

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/create")
def createUser(user:UserClass,db:Session =Depends(get_db) ):
    user_data =User(
        name = user.name,
        email = user.email
    )
    db.add(user_data)
    db.commit()
    return {
        "message":"user created successfully"
    }



@router.post("/create/post")
def createPost(post:PostClass,db:Session =Depends(get_db) ):
    user_data =Post(
        title = post.title,
        create_by = post.create_by
    )
    db.add(user_data)
    db.commit()
    return {
        "message":"post created successfully"
    }




@router.get("/read/",response_model=List[Userrsponse])
def createUser(db:Session =Depends(get_db) ):
  
    res = db.query(User).all()
   
    if not res:
        raise HTTPException(404,detail="user not found bro ok ")

    return res


@router.get("/read/{user_id}" , response_model=Userrsponse)
def createUser(user_id:int,db:Session =Depends(get_db) ):
  
    res = db.query(User).filter(User.id == user_id).first()   
    return res


