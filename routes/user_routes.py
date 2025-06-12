from fastapi import APIRouter
from fastapi.responses import JSONResponse
from controllers.user_controller import UserController

user_router = APIRouter()

@user_router.get('/all')
async def all_users():
    users = UserController.get_users()
    if (users):
        return JSONResponse(content=users, status_code=200)
    else: 
        return JSONResponse(content={"Error message": "No se optuvo respuesta."})
