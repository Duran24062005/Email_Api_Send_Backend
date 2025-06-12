from services.user_services import UserServices
from config.database import SessionLocal
from sqlalchemy.exc import SQLAlchemyError


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
