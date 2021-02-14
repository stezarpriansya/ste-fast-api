from typing import Optional
import pandas as pd
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data")
def read_root():
    data = pd.read_csv('cities.csv')
    data = data.values.tolist()()
    return {"datas": data}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}