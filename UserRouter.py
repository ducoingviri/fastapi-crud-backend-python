from fastapi import APIRouter, Path, HTTPException, status
from UserModel import UserModel

user_router = APIRouter()
user_list = []


@user_router.post("/user")
async def store(user: UserModel) -> dict:
    user_list.append(user)
    return {"message": "User added successfully!"}


@user_router.get("/user")
async def index() -> dict:
    return {"users": user_list}


@user_router.get("/user/{user_id}")
async def show(user_id: int = Path(..., title="User ID of the user to show")) -> dict:
    for user in user_list:
        if user.id == user_id:
            return {"user": user}
    return {"message": "There is not User for the given ID."}


@user_router.put("/user/{user_id}")
async def update(user_data: UserModel, user_id: int = Path(..., title="User ID of the user to update")) -> dict:
    for user in user_list:
        if user.id == user_id:
            user.id = user_data.id
            user.username = user_data.username
            return {"message": "User updated successfully!"}
    return {"message": "There is not User for the given ID."}


@user_router.delete("/user/{user_id}")
async def destroy(user_id: int) -> dict:
    for index_id in range(len(user_list)):
        user = user_list[index_id]
        if user.id == user_id:
            user_list.pop(index_id)
            return {"message": "User deleted successfully!"}
    return {"message": "There is not User for the given ID."}


@user_router.get("/user/handling-exception/{user_id}")
async def show_handling_exception(user_id: int = Path(..., title="User ID of the user to show")) -> dict:
    for user in user_list:
        if user.id == user_id:
            return {"user": user}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="There is not User for the given ID."
    )
