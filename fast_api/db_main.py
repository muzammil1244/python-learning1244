from fastapi import FastAPI
from db.rourte import app





real_app = FastAPI()

@real_app.get("/")
def getpage():
    return {
        "message":"hi "
    }


real_app.include_router(router=app)