from models.email_models import Email as EmailEntity
from sqlalchemy.orm import Session, joinedload


class EmailServices:

    def __init__(self, db:Session)->None:
        self.db = db

    def get_all_emails(self):
        try:
            emails = (
                self.db.query(EmailEntity)
                .options(joinedload(EmailEntity.user_id))
                .all()
            )
            if emails:
                return emails
            else:
                return False
        except Exception as e:
            return f"Error to fetch emails: {e}"