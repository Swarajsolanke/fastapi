from fastapi import FastAPI
from enum import Enum
app = FastAPI()

@app.get('/')
async def root():
    return {"message":"hello world!"}

@app.post('/')
async def post():
    return {"message":"post route returning"}

@app.put('/')
async def put():
    return {"message":"hello i  am returning put method "}


@app.get('/item')
async def home():
    return {"massage":"hey i am learning it "}


class FoodEnum(str,Enum):
    vegatibale="vegatibale"
    dairy="dairy"
    food ="food"

@app.get("/fruits/{food_name}")
async def get_food(food_name :FoodEnum):
    if food_name == FoodEnum.vegatibale:
        return {"food_name": food_name,"massage":"you are health"}
    if food_name.value=="food":
        return {
            "food_name":food_name,
            "message":"you are still eating food"}
    
    return{"food_name":food_name , "message":"i like chocolate"}



