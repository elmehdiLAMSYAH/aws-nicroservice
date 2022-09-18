import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from helpers.logic import wikiData, wikiSearch, sentencwblob
from textblob import TextBlob

app = FastAPI()

products = {
    1: {"mat": "QBCD7878 ", "name": "tendeuse a barbe", "price": "25.89"},
    2: {"mat": "QBCD789", "name": "souris logitech wireless", "price": "17.99"},
}


class Product(BaseModel):
    mat: str
    name: str
    price: float


class UpdateProduct(BaseModel):
    mat: str
    name: str
    price: float


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/getproduct/{id}")
def get_product(ident: int):
    if ident not in products:
        return {"erreur": "product not exist"}
    print(products[int(ident)])
    return products[int(ident)]


@app.get("/getproductByName")
async def getproductByName(mat: str = None):
    for ident in products:
        if products[ident]["mat"] == mat:
            return products[ident]
    return {"data": "product not found in dict"}


@app.post("/addProduct/{id}")
async def add_product(identification: int, product: Product):
    if identification in products:
        return {"erreur": "product already exist"}
    products[identification] = product
    return products[identification]


@app.put("/updateProduct/{id}")
async def updateProduct(identification: int, product: UpdateProduct):
    if identification not in products:
        return {"erreur": "product not exist"}
    if product.mat != "string":
        products[identification]["mat"] = product.mat
    if product.name != "string":
        products[identification]["name"] = product.name
    if product.price != 0:
        products[identification]["price"] = product.price
    return products[identification]


@app.delete("/deleteProduct/{id}")
async def deleteProduct(identification: int):
    if identification not in products:
        return {"error": "Product not exist"}
    del products[identification]
    return {"succes": "Product deleted"}


@app.get("/search/{name}")
async def searchInWiki(name: str):
    """ searching name  """
    if name is not None:
        return {f"result : {wikiSearch(name=name)}"}
    return {f"result by default for no cotent : {wikiSearch()}"}


@app.get("/searchtags/{name}")
async def searchInWikitags(name: str):
    """ searching name with token tags """
    if name is not None:
        return {f"result with tags : {sentencwblob(wikiData(name=name))}"}
    return {f"no result for None data "}


@app.get("/wikisentence/{sentence}/{lenght}")
async def searchDataInWiki(sentence: str, lenght=int):
    if sentence is not None:
        return {f"result : {wikiData(name=sentence, length=lenght)}"}
    return {f"result by default for no cotent : {wikiData()}"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="localhost")
