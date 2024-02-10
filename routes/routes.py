from http.client import HTTPException

from fastapi import APIRouter
from config.db import collection_name
from models.fastDemos import FastDemo
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()


# GET request method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


# POST request method
@router.post("/")
async def todo_post(todo: FastDemo):
    collection_name.insert_one(dict(todo))


# PUT request method
@router.put("/{id}")
async def put_todo(id: str, todo: FastDemo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})


@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})


'''@router.get("/error/handling")
async def handle_error(id:str):
    if id==2:
        return HTTPException(status_code=400,details="item is not equal to")
    return {"value":id}'''
