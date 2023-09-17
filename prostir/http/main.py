import uvicorn
from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


user_DB = [
    {"id": 0, "user_name": "Bill"},
    {"id": 1, "user_name": "WiLL"},
    {"id": 2, "user_name": "Dill"}
]


class User(BaseModel):
    id: int
    user_name: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/user/{user_id}")
async def read_id(user_id: int):
    return [user for user in user_DB if user.get("id") == user_id]


@app.post("/id")
async def add_id(user: List[User]):
    user_DB.extend(user)
    return{"status": 200, "data": user_DB}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.1.0.1",reload=True)
