from fastapi import APIRouter , Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.Database import get_db
from db.module import UserData



class UserCalss(BaseModel):
    name:str
    email:str
    age:int






app = APIRouter(
    prefix="/user",
    tags=["user"]
)


@app.post("/create")
def createUser(users:UserCalss ,db : Session = Depends(get_db)  ):
    
    user_data = UserData(
        name = users.name,
        email = users.email,
        age = users.age
    )

    db.add(user_data)
    db.commit()
    return {"message":"user created"}



@app.get("/read")
def readUser(db:Session = Depends(get_db)):
    
    data = db.query(UserData).all()

    return {
        "message":"data read successfully",
        "data":data
    }

@app.put("/update/{user_id}")
def updateUser(user:UserCalss ,user_id : int, db : Session = Depends(get_db)):
    
    data = db.query(UserData).filter(UserData.id == user_id).first()
    data.name = user.name
    data.email = user.email
    data.age = user.age
    db.commit()

    return {
        "message":"data updated successfully",
        "data" : data
    }


@app.delete("/delete/{delete_id}")
def deleteUser(delete_id : int, db : Session = Depends(get_db)):

    user = db.query(UserData).filter(UserData.id == delete_id).first()

    db.delete(user)
    db.commit()
    return {"message": "user deleted successfully"}
    