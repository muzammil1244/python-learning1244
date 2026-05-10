from fastapi import FastAPI 
from pydantic import BaseModel
from router_file import router


rt = FastAPI()



rt.include_router(router=router)
