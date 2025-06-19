from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from controllers.user_controller import UserController
from schemas.user_schemas import CreateUser
import json

user_router = APIRouter()

@user_router.get('/all')
async def all_users():
    users = UserController.get_users()
    if (users):
        return JSONResponse(content=jsonable_encoder(users), status_code=200)
    else: 
        return JSONResponse(content={"Error message": "No se optuvo respuesta."})

@user_router.get('/{id}', status_code=200)
async def get_one_user_by_id(id: int):
    find_user = UserController.get_user_by_id(id)
    if (find_user):
        return JSONResponse(content=jsonable_encoder(find_user), status_code=200)
    else:
        return JSONResponse(content=jsonable_encoder(find_user ),status_code=400)

@user_router.post('/create', status_code=201)
def create_user(data: CreateUser):
    new_user = UserController.create_new_user(data)
    if (new_user):
        return JSONResponse(content=jsonable_encoder(new_user), status_code=201)
    else:
        return JSONResponse(content=jsonable_encoder(new_user), status_code=500)

@user_router.put('/update', status_code=200)
def update_user_by_id(id: int, user_data:CreateUser):
    user = UserController.update_user(id, user_data.model_dump())
    if user:
        return JSONResponse(content=jsonable_encoder(user), status_code=200)
    

@user_router.delete('/{id}')
def delete_user_route(id: int):
    user_deleted = UserController.delete_user(id)
    if user_deleted:
        return JSONResponse(content=jsonable_encoder(user_deleted), status_code=200)

