from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book Catalog API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


class Book(BookCreate):
    id: int


books: list[Book] = []
next_book_id = 1


@app.get("/books", response_model=list[Book])
def list_books() -> list[Book]:
    # TODO: Return the current books.
    pass


@app.post(
    "/books",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
)
def create_book(book_data: BookCreate) -> Book:
    global next_book_id
    # TODO: Create a book with a unique ID, add it to books, and return it.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int) -> Book:
    # TODO: Find and return the book, or raise HTTPException with status 404.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookCreate) -> Book:
    # TODO: Replace the book's title and author, or raise HTTPException with status 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int) -> Response:
    # TODO: Remove the book, or raise HTTPException with status 404.
    pass
