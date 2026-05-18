from fastapi import Request , Depends
from model import User
from sqlalchemy.orm import Session
from Databse import get_db
import jwt


def auth_check(request : Request,db  : Session = Depends(get_db)):
    print("depend called here")
    header = request.headers.get("authorization")
    print("this is ruf header", header)
    token= header.split(" ")[-1] 

    decoded_token =jwt.decode(token, "muzammil", algorithms=["HS256"])
    print(decoded_token["id"])
    result = db.query(User).filter(User.id ==decoded_token["id"] ).first()
    
    return result