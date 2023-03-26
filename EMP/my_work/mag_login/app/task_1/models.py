from sqlalchemy import Column, Integer, String, ForeignKey
from task_1.database import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel

# class Task(BaseModel):
#     title: str
#     body: str
#     task_id: int

class Task(Base):
    __tablename__ = 'tasks_assigned'

    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    body = Column(String(255))
    creator_id=Column(Integer)
    user_id = Column(Integer, ForeignKey('managers.mag_id'))

    #creator = relationship("Manager", back_populates="tasks")



class Leave(Base):
    __tablename__ = 'leave_status'

    leave_id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255))
    body = Column(String(255))
    days=Column(Integer)
    from_d=Column(String(255))
    to_d=Column(String(255))
    status=Column(String(255))
    user_id = Column(Integer, ForeignKey('managers.mag_id'))

    # creator = relationship("Employee", back_populates="tasks")
    
    
class Manager(Base):
    __tablename__ = 'managers'

    mag_id = Column(Integer, primary_key=True, index=True)
    mag_name = Column(String(255))
    email =Column(String(255))
    password =Column(String(255))
    dept =  Column(String(255))
    address=Column(String(255))
    gender=Column(String(255))
    dob=Column(String(255))
    phone=Column(String(255))
    posting=Column(String(255))
    

    #tasks = relationship('Task', back_populates="creator")

class Employee(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    dept =  Column(String(255))
    address=Column(String(256))
    gender=Column(String(255))
    dob=Column(String(255))
    phone=Column(String(255))
    posting=Column(String(255))
    emp_mag_id=Column(Integer,ForeignKey('managers.mag_id'))
       
   

    #tasks = relationship('Task', back_populates="creator")
    
class Admin(Base):
    __tablename__ = 'admin'

    admin_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    dept =  Column(String(255))
    address=Column(String(256))
    gender=Column(String(255))
    dob=Column(String(255))
    phone=Column(String(255))
    posting=Column(String(255))

    
# class Emp_Mag(Base):
#     __tablename__ = 'employee_manager'

#     id = Column(Integer, primary_key=True, index=True)
#     mag_id=Column(Integer)
#     emp_name=Column(String(255))
