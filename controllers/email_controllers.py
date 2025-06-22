from services.email_services import EmailServices
from config.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError


class EmailController:

    def get_emails_():
        try:
            with SessionLocal() as db:
                emails = EmailServices(db).get_all_emails()
            if emails:
                return emails
            else:
                return "Not emails"
        except Exception as e:
            return f"Error to fetch emails"