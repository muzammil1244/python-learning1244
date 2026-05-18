from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Database import Base


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)

    posts = relationship("Post", back_populates="user")


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)

    create_by = Column(
        Integer,
        ForeignKey("user.id")
    )

    user = relationship("User", back_populates="posts")