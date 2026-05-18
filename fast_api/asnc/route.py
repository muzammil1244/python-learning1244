from fastapi import APIRouter,Depends , HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from Database import get_db
from model import User , Post
from typing import List
from sqlalchemy import select

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
async def createUser(user:UserClass,db:AsyncSession =Depends(get_db) ):
    user_data =User(
        name = user.name,
        email = user.email
    )
    db.add(user_data)
    await db.commit()
    return {
        "message":"user created successfully"
    }



@router.post("/create/post")
async def createPost(post:PostClass,db:AsyncSession =Depends(get_db) ):
    user_data =Post(
        title = post.title,
        create_by = post.create_by
    )
    db.add(user_data)
    await db.commit()
    return {
        "message":"post created successfully"
    }




@router.get("/read/",response_model=List[Userrsponse])
async def createUser(db:AsyncSession =Depends(get_db) ):
  
    result = await db.execute(
     select(User)
    )

    res = result.scalars().all()
   
    if not res:
        raise HTTPException(404,detail="user not found bro ok ")

    return res


@router.get("/read/{user_id}" , response_model=Userrsponse)
async def createUser(user_id:int,db:AsyncSession =Depends(get_db) ):
  
    result =await  db.execute(
        select(User).where(User.id == user_id)
    )  
    res = result.scalar()
    return res


