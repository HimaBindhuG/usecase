from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import sys
# sys.path.append('/C:/Users/Hima.g/usecase/mag_login/app/task_1')
# # from repository import manager,task,leave


SQLALCHAMY_DATABASE_URL = "mysql://root:Hima.bindhu123@127.0.0.1:3306/employeedb"

# engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
#                        "check_same_thread": False})
engine = create_engine(SQLALCHAMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()