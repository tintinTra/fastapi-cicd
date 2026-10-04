import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def main():

    uvicorn.run("fastapi_cicd:app", host="127.0.0.1", port=8000, reload=True)


class Book(BaseModel):
    title: str
    isbn: str
    author: str


db: dict[str, Book] = {}


@app.get("/status", description="get server status", tags=["status"])
def status():
    return {"status": 200}


@app.get("/books", tags=["Books"])
def get_books():
    return [book.model_dump() for book in db.values()]


@app.post("/book", tags=["Books"])
def post_book(book: Book):

    db[book.isbn] = book
    # return {
    #     "title": book.title,
    #     "isbn": book.isbn,
    #     "author": book.author,
    # }
    return book.model_dump()


@app.post("/books", tags=["Books"])
def multiple_books(books: list[Book]):

    for book in books:
        db[book.isbn] = book

    return books
