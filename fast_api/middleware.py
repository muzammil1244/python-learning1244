from fastapi import FastAPI , Request





md = FastAPI(title="middleware")



@md.middleware("http")
async def middleware_fun(request : Request , call_next):

    print("before route executing")
    res = await call_next(request)
    print(f"after route executing {res}")

    return res


@md.get("/")
def first_route():
    return {"data":"hello"}