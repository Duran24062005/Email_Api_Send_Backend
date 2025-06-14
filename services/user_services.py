from models.user_models import User as UserEntity
from sqlalchemy.orm import Session


class UserServices:

    def __init__(self, db: Session)->None:
        self.db = db

    def get_all_users(self):
        """Retrieve all users from the database"""
        try:
            users = (self.db.query(UserEntity).all())
            if users:
                return users
            else:
                return False
        
        except:
            return "Error al ejecutar la busqueda."

    def get_user(self, id: int):
        """Get user filter by ID"""
        try:
            user = self.db.query(UserEntity).filter(UserEntity.id == id).first()
            if user:
                return user
            else:
                return False
                
        except:
            return "Error al ejecutar la consulta."

    def create_user(self, data_user):
        """Create a new user"""
        try:
            user_created = self.db.query(UserEntity).filter(UserEntity.email == data_user.email).first()
            if user_created:
                return False
            else:
                new_user = UserEntity(**data_user.model_dump())
                self.db.add(new_user)
                self.db.commit()
                self.db.refresh(new_user)
                self.db.close()
                return new_user
        except:
            return False