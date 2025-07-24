
from fastapi import FastAPI
from pydantic import BaseModel , Field
from uuid import UUID
app=FastAPI()
@app.get('/{name}')
def read_api(name:str):
    return {'welcome':name}

class Book(BaseModel):
    id:UUID
    title:str=Field(min_length=1)

@app.post()
def create_item(Book:BaseModel):
    return {"item":Book}