from pydantic import BaseModel , Field

class movie:
    name=""
    director=""
    review = 5



movie_data = movie()
movie_data.name = "attonment",
movie_data.director ="ahemad"
movie_data.review = "5"


print(movie_data.review)

# in python it s is hard to difine rull for data store validation so we used pydentic here 

class movie2(BaseModel):
    name:str 
    
    review:int = 0



movie2_data = movie2(name="muzammmil ",review=5)



print(movie2_data)

# field validation 



class Product(BaseModel):
    name:str = Field(min_length=5,max_length=20)
    des:str = Field(min_length=5,max_length=50)
    price:int = Field(gr=100 , le=1000)


product_data = Product(name="muzammil",des="hmmm bahot badhiya hai ye product ",price=500)

print(product_data)

class Order(BaseModel):
    id:str = Field(min_length=2)
    products:Product 



from typing import List


order = Order(id="iii",products = product_data)

print(order)



class Cart(BaseModel):
    id:str = Field(min_length=2)
    itemss : List[Product]
    comment:str = Field(
        default=" No comments"
    )




cart = Cart(id="jj",itemss=[product_data],comment="hmm ok ")

print(cart)