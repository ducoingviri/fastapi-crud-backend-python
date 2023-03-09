from fastapi import FastAPI
from todo import todo_router
from UserRouter import user_router
from animal.DogRouter import dog_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello, world!"}

app.include_router(todo_router)
app.include_router(user_router)
app.include_router(dog_router)
