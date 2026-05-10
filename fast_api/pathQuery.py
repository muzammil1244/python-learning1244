from fastapi import FastAPI



pq = FastAPI(title="path and query learning process")



@pq.get("/product/name/{data}")
def path_fun(data:int):
    path_data = data
    return {"data":f"so this is path data {path_data}"}

@pq.get("/no")
def query_fun(data:int):
    path_data = data
    return {"data":f"so this is path data {path_data}"}


@pq.get("/product/{name}")
def path_query(name:str,no:int):
    return { 
        "product_name":name,
      
    }