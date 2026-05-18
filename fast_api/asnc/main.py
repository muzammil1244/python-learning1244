from fastapi import FastAPI
from Database import engine
from model import Base
from route import router

app = FastAPI()


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )

app.include_router(router=router)