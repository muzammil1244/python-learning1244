from sqlalchemy import Column, Integer, String
from db.Database import Base


class UserData(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)