from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def health_get():
    return {"Message": "API is running perfectly."}
