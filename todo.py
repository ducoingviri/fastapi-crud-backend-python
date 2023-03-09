from fastapi import APIRouter

todo_router = APIRouter()
todo_list = []


@todo_router.post("/todo")
async def store(todo: dict) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully!"}


@todo_router.get("/todo")
async def index() -> dict:
    return {"todos": todo_list}
