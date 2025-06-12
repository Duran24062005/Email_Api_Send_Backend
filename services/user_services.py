from models.user_models import User as UserEntity
from sqlalchemy.orm import Session


class UserServices:

    def __init__(self, db: Session)->None:
        self.db = db

    def get_all_users(self):
        """Retrieve all users from the database"""
        try:
            users = (self.db.query(UserEntity).all())
            return users
        
        except:
            return False