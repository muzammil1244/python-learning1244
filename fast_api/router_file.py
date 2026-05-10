from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter()



@router.get("/user")
def user():
    return {
        "message" : " return  "
    }
