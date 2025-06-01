from fastapi import APIRouter


home_routes = APIRouter()


@home_routes.get('/home')
async def home():
    pass