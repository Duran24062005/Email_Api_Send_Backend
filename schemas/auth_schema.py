from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str


class UserOuth(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True