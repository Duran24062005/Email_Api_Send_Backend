from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTerror, jwt
from passlib.context import CryptContext

from sqlalchemy.orm import Session
from ..config.database import SessionLocal
from models.user_models import User
from dotenv import load_dotenv

load_dotenv()

# Encriptacion
pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Helpers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Password
def hash_password(password: str)->str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str)->bool:
    return pwd_context.verify(plain, hashed)


