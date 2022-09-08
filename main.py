from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

products = {
    1: {
        "mat": "QBCD7878 ",
        "name": "tendeuse a barbe",
        "price": "25.89"

    },
    2: {
        "mat": "QBCD789",
        "name": "souris logitech wireless",
        "price": "17.99"

    }
}


class Product(BaseModel):
    mat: str
    name: str
    price: float


class UpdateProduct(BaseModel):
    mat: Optional[str]
    name: Optional[str]
    price: Optional[float]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/getproduct/{id}")
def get_product(id: int):
    if id not in products:
        return {"erreur": "product not exist"}
    print(products[int(id)])
    return products[int(id)]


@app.get("/getproductByName")
async def getproductByName(mat: Optional[str] = None):
    for id in products:
        if products[id]["mat"] == mat:
            return products[id]
    return {"data": "product not found in dict"}


@app.post("/addProduct/{id}")
async def add_product(id: int, product: Product):
    if id in products:
        return {"erreur": "product already exist"}
    products[id] = product
    return products[id]


@app.put("/updateProduct/{id}")
async def updateProduct(id: int, product: UpdateProduct):
    if id not in products:
        return {"erreur": "product not exist"}
    if product.mat != "string":
        products[id]["mat"] = product.mat
    if product.name != "string":
        products[id]["name"] = product.name
    if product.price != 0:
        products[id]["price"] = product.price
    return products[id]


@app.delete("/deleteProduct/{id}")
async def deleteProduct(id: int):
    if id not in products:
        return {"error": "Product not exist"}
    del products[id]
    return {"succes": "Product deleted"}
