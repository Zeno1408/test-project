

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def health_get():
    return {"Message": "Server is up and running!"}

books_list = [
    {"id": 1, "Name": "The Secret History", "Author": "Donna Tart"},
    {"id": 2, "Name": "Dune", "Author": "Frank Herbert"},
    {"id": 3, "Name": "Warbreaker", "Author": "Brandon Sanderson"}
]

@app.post("/books")
async def add_books_list():
    return books_list

@app.get("/books")
async def get_books():
    return books_list

@app.put("/books/{id}")
async def update_book_by_id(book_id: int):
    for book in books_list:
        if book["id"] == book_id:
            book["Name"] = "The Goldfinch"
    return books_list

@app.delete("/books/{id}")
async def delete_book_by_id(book_id: int):
    for book in books_list:
        if book["id"] == book_id:
            books_list.pop(book_id-1)
    return books_list