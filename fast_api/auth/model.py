from sqlalchemy.orm import Session , relationship
from Databse import Base
from sqlalchemy import Column , String , Integer , ForeignKey 




class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True ,  autoincrement=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    posts = relationship("Post",back_populates="user")



class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer,primary_key=True ,  autoincrement=True)
    title = Column(String)
    description = Column(String)
    create_by = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts") 
    
