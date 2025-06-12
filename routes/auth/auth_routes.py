from fastapi import APIRouter


auth_router = APIRouter()


@auth_router.get('/register')
async def register():
    pass

@auth_router.get('/login')
async def login():
    pass

@auth_router.get('/login')
async def login():
    pass