from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel, Field
from uuid import UUID
from database import Base ,engine,SessionLocal
import models 
from sqlalchemy.orm import Session

app=FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_api(db:Session=Depends(get_db)):
    print(db.query(models.Books).all())
    return db.query(models.Books).all()
    

class Book(BaseModel):
    title:str= Field(min_length=1)
    author:str=Field(min_length=1, max_length=100)
    description:str=Field(min_length=1,max_length=400)
    rating:int=Field(gt=-1, lt=101)

Books=[] 


@app.post("/")
async def create_item(book:Book,db:Session=Depends(get_db)):
    book_model=models.Books()
    book_model.title=book.title
    book_model.author=book.author
    book_model.description=book.description
    book_model.rating=book.rating
    db.add(book_model)
    db.commit()
                                    
    return book

@app.put("/{book_id}")
def update_book(book_id:int,book:Book,db:Session=Depends(get_db)):
    book_model=db.query(models.Books).filter(models.Books.id==book_id).first()
    print(f"data present inside database:{book_model.data}")
    if book_model is None:
        raise HTTPException(
            status_code=404,
            details=f"book id:{book_id} does not exist"
        )
    book_model.title=book.title
    book_model.author=book.author
    book_model.description=book.description
    book_model.rating=book.rating
    db.add(book_model)
    db.commit()
                                    
    return book
    counter=0
    for x in Books:
        counter+=1
        if x.id==book_id:
            Books[counter-1]=book
            return Books[counter-1]
    raise HTTPException(
            status_code=404,
            detail="book not found"
        )

@app.delete("/{book_id}")
def delete_book(book_id:int,db:Session=Depends(get_db)):
    book_model=db.query(models.Books).filter(models.Books.id==book_id).first()
    if book_model is None:
        raise HTTPException(
            status_code=404,
            details=f"id {book_id} Does not exist"
        )
    db.query(models.Books).filter(models.Books.id==book_id).delete()
    db.commit()

    """counter=0
    for x in Books:
        counter+=1
        if x.id==book_id:
            del Books[counter-1]
            return {"message":"book deleted sucessfully"}
    raise HTTPException(
        status_code=404,
        detail="book not found"

    )
    """
    