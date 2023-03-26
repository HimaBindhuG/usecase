from sqlalchemy import Column, Date, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship



class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    task_id = Column(Integer, ForeignKey('employee.id'))

    creator = relationship("Employee", back_populates="follower")


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)

   
    
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True,index=True)
    name =  Column(String(50))
    email =  Column(String(50))
    password=Column(String(50))
    dept =  Column(String(50))
    address=Column(String(256))
    gender=Column(String(11))
    dob=Column(Date)
    phone=Column(Integer)
    posting=Column(String(50))
    blood_group=Column(String(2))
    
    follower = relationship('Task', back_populates="creator")
