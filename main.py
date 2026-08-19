from fastapi import FastAPI

app = FastAPI()


users = [
    {"id": 1, "name": "Ali", "age": 25},
    {"id": 2, "name": "Ahmed", "age": 30},
]


@app.get("/")
def home():
    return {"message": "Welcome to my API"}


@app.get("/users")
def get_users():
    return users