from fastapi import FastAPI
from route import auth_router
from Databse import Base , engine
import model

app = FastAPI()


Base.metadata.create_all(bind = engine)

app.include_router(auth_router)