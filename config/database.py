import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sql_file_name = "../send_email.sqlite"
base_dir = os.path.dirname(os.path.relpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir, sql_file_name)}"

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()