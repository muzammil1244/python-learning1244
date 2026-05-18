from model import User
from pwdlib import PasswordHash
from fastapi import HTTPException , status
import jwt


password_hash =  PasswordHash.recommended()

def hassPassword(password):
   hashed_password = password_hash.hash(password)
   return hashed_password




def Register(body,db):
   
   new_user = User(
      
      name = body.name,
      email = body.email,
      password = hassPassword(body.password)

   )

   db.add(new_user)
   db.commit()


   
   
   return  {
   "name": new_user.name,
   "email": new_user.email,
   "password": new_user.password
}


# login controller

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def login(body,db):
   
   is_user = db.query(User).filter(User.email == body.email).first()

   if not is_user :
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail=" user not found ")
   
   if not verify_password(body.password,is_user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED , detail="  you  password not matched ")
   
   token = jwt.encode({"id" : is_user.id},"muzammil",algorithm="HS256")

   return {
       "message":"user login successfully",
       "token":token
   }
      
   

def dashboard(user):
    return user

