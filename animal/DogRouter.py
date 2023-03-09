from typing import Any, List, Union

from fastapi import APIRouter
from pydantic import BaseModel

dog_router = APIRouter()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@dog_router.post("/dogs/", response_model=Item)
async def create_dog(item: Item) -> Any:
    return item


@dog_router.get("/dogs/", response_model=List[Item])
async def read_dogs() -> Any:
    return [
        {"name": "Tommy", "price": 33.0},
        {"name": "Boby", "price": 66.0},
    ]
