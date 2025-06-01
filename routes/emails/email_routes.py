from fastapi import APIRouter


email_routes = APIRouter()


@email_routes.get('/email')
async def email():
    pass