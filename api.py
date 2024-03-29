
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def print_message():
    return {"Message": "Hello World!"}

@app.post("/info")
async def add_info():
    person = {
        "Name": "Aditya",
        "Age": 24
    }
    return person