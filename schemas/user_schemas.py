from pydantic import BaseModel, EmailStr
from datetime import date, datetime
from typing import Optional, List


class CreateUser(BaseModel):
    
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    imageUrl: Optional[str]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john@doe.com",
                "password": "httpskmjd",
                "imageUrl": "None"
            }
        }