from fastapi import APIRouter , status , Depends ,Request
from schema import Usercreate , Userresponse , UserLogin
from sqlalchemy.orm import Session
from model import User

from Databse import get_db
from controller import Register , login , dashboard 
from helper import auth_check



auth_router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@auth_router.post("/create",status_code=status.HTTP_201_CREATED , response_model=Userresponse)
def create_user(body:Usercreate, db : Session = Depends(get_db)):
    return Register(body , db)


@auth_router.post("/login",status_code=status.HTTP_202_ACCEPTED)
def login_user(body:UserLogin,db:Session = Depends(get_db)):
    return login(body,db)


@auth_router.get("/dashboard",status_code=status.HTTP_202_ACCEPTED , response_model=Userresponse)
def dashboard_route(user:User = Depends(auth_check)):
    return dashboard(user)


    