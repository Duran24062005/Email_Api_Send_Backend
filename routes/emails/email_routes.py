from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from controllers.email_controllers import EmailController
from schemas.email_schema import SendEmailSchema


email_routes = APIRouter()


@email_routes.get('/all')
def email_gets():
    gets_email = EmailController.get_emails_()
    return JSONResponse(content=jsonable_encoder(gets_email), status_code=200)

@email_routes.get('/id={id}')
def get_email_by_id(id):
    return id

@email_routes.post('/send')
def Send_Email(email: SendEmailSchema):
    return email


@email_routes.delete('/id={id}')
def delete_email(id):
    return id