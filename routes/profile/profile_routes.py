from fastapi import APIRouter


profile_routes = APIRouter()


@profile_routes.get('/profile')
def profile():
    pass