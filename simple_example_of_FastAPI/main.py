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

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Olá, Mundo"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "q": query}


@app.post("/items/")
async def create_item(item_id: int, query: Optional[str] = None):
    return {"item_id": item_id, "q": query}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
