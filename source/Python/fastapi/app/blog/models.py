from sqlalchemy import Column,Integer,String,ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__='TASKS'

    id= Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))
    manager=relationship("Employee",back_populates="tasks")



class Employee(Base):
    __tablename__='EMPLOYEE'
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    address=Column(String)
    phone=Column(String)
    blood=Column(String)
    posting=Column(String)
    dept=Column(String)
    password=Column(String)


    tasks=relationship('Task',back_populates="manager")
    
    


