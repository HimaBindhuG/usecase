from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

#create sqlite engine instance
engine=create_engine("sqlite:///himadb2.db")

#create declarativemeta instance
Base = declarative_base()

#Define To Do class inheriting from Base
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name =  Column(String(50))
    email =  Column(String(50))
    age =  Column(Integer)
    dept =  Column(String(50))