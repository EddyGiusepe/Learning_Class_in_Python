"""
Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

setup:
======
$ pip install fastapi
$ pip install "uvicorn[standard]"

Execução:
=========

$ uvicorn main:app --reload


Interactive API docs:
=====================

http://127.0.0.1:8000/docs
"""

from typing import Union, Optional
from fastapi import FastAPI
import uvicorn
import httpx

app = FastAPI()

async def fetch_data_from_external_api():
    # Simula uma requisição para uma API externa
    async with httpx.AsyncClient() as client:
        # Faça uma requisição GET para uma API fictícia
        response = await client.get("https://fakestoreapi.com/products")
        if response.status_code == 200:
            return response.json()
        else:
            return None
        
@app.get("/")
# async def read_root():
#     return print("Testando o Locust 🤗: ", 1 + 2) #{"message": "Olá, Mundo"}
async def read_root():
    # Lê dados de uma fonte externa:
    data = await fetch_data_from_external_api()
    if data:
        return {"message": "🤗 Dados lidos com sucesso 🤗", "data": data}
    else:
        return {"message": "😭😭 Falha ao ler dados da fonte externa 😭😭"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "q": query}


@app.post("/items/")
async def create_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "q": query}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
