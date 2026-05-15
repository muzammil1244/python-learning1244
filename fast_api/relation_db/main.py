from fastapi import FastAPI
from route import router

from Database import Base, Database
import model



Base.metadata.create_all(bind=Database)

app = FastAPI()

app.include_router(router)