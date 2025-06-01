from fastapi import APIRouter


profile_routes = APIRouter()


@profile_routes.get('/profile')
async def profile():
    pass