from fastapi import FastAPI , Depends




dp = FastAPI(title="depends")


def hello():
    return "hi how are you "



@dp.get("/")
def dep_fun(data:str = Depends(hello)):
    res = data
    return res