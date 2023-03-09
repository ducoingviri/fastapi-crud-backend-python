from typing import List
from pydantic import BaseModel


class DogModel(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": "I'm an item X!"
            }
        }


class DogModels(BaseModel):
    items: List[DogModel]

    class Config:
        schema_extra = {
            "example": {
                "items": [
                    {
                        "name": "example schema 1"
                    },
                    {
                        "name": "example schema 2"
                    }
                ]
            }
        }
