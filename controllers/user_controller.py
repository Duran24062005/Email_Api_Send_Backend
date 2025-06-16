from services.user_services import UserServices
from config.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from schemas.user_schemas import CreateUser


class UserController:

    def get_users():
        try:
            with SessionLocal() as db:
                users = UserServices(db).get_all_users()
                if (users):
                    return users
                else:
                    return("No hay usuarios registrados.")

        except:
            print("Error inesperado")

    def get_user_by_id(id: int):
        try:
            with SessionLocal() as db:
                user = UserServices(db).get_user(id)
            if user:
                return user
            else:
                return f"User with id {id} does not exist"
        except:
            return f"Error when executing the query."

    def create_new_user(data:CreateUser):
        try:
            with SessionLocal() as db:
                created = UserServices(db).create_user(data)
            if created:
                return created
            else:
                return f"This user already exist"
        except:
            return f"Error when executing the query."


    def update_user(id, data:CreateUser):
        try:
            with SessionLocal() as db:
                user_updated = UserServices(db).update_user_created(id, data)
            if user_updated:
                return user_updated
            else:
                return(f"User with id = {id} not found.")
        except Exception as e:
            return f"Error to update user: {e}"

