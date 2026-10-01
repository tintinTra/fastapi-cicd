from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = {}


class Book(BaseModel):
    title: str
    isbn: str
    author: str


@app.get("/status")
def status():
    return {"status": 200}


@app.post("/book")
def book(book: Book):

    db[book.isbn] = book.model_dump()
    return {
        "title": book.title,
        "isbn": book.isbn,
        "author": book.author,
    }


@app.post("/books")
def multiple_books(books: list[Book]):

    for book in books:
        db[book.isbn] = book

    return books
