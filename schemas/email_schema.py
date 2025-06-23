from pydantic import BaseModel


class SendEmailSchema(BaseModel):
    user_id: int
    from_: str
    to: str
    subject: str
    message: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "user_id": 1,
                "from_": "john.doe@gmail.com",
                "to": "johana.doe@gmail.com",
                "subject": "Salute",
                "message": "Hello, world"
            }
        }