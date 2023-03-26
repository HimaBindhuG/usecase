from fastapi import HTTPException,status
from requests import Session
from sqlalchemy import Date, create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#create sqlite engine instance
# engine=create_engine("sqlite:///himadb2.db")


SQLALCHAMY_DATABASE_URL = 'sqlite:///employee.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#create declarativemeta instance
Base = declarative_base()

#Define To Do class inheriting from Base
# class Employee(Base):
#     __tablename__ = 'employee'
#     id = Column(Integer, primary_key=True)
#     name =  Column(String(50))
#     email =  Column(String(50))
#     password=Column(String(50))
#     dept =  Column(String(50))
#     address=Column(String(256))
#     gender=Column(String(11))
#     dob=Column(Date)
#     phone=Column(Integer)
#     posting=Column(String(50))
#     blood_group=Column(String(2))
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
