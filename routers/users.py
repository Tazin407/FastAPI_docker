from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
async def read_users():
    return [{"name": "Foo"}, {"name": "Bar"}]

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}