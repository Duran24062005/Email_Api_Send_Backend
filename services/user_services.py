from models.user_models import User as UserEntity
from sqlalchemy.orm import Session, joinedload
from schemas.user_schemas import CreateUser


class UserServices:

    def __init__(self, db: Session)->None:
        self.db = db

    def get_all_users(self):
        """Retrieve all users from the database"""
        try:
            users = (
                self.db.query(UserEntity)
                .options(joinedload(UserEntity.emails))
                .all()
            )
            if users:
                return users
            else:
                return False
        
        except Exception as e:
            return f"Error al ejecutar la busqueda {e}."

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

    def create_user(self, data_user: CreateUser):
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

    def update_user_created(self, user_id: int, user_data: CreateUser):
        try:
            user = self.db.query(UserEntity).filter(UserEntity.id == user_id).first()
            if not user:
                return False
            for key, value in user_data.items():
                setattr(user, key, value)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception as e:
            return f"Error inesperado: {e}"

    def delete_user_(self, id: int):
        try:
            user = self.get_user(id)
            if user:
                self.db.delete(user)
                self.db.commit()
                self.db.close()
                return True
            else:
                return False
        except Exception as e:
            return f"Error when trying to delete to user with id: {id}. {e}"