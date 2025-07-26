from fastapi import FastAPI ,Request
from fastapi.templating import Jinja2Templates
app= FastAPI()

templates= Jinja2Templates(directory="templates")

Dogs=[{"name":"milo","age":2},{"name":"max","age":3},{"name":"bella","age":1}]

@app.get("/")
async def name(request:Request):
    return templates.TemplateResponse('home.html',{"request":request,"name":'swaraj',"dogs":Dogs})
