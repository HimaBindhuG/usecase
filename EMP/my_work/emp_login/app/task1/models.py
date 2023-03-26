

from sqlalchemy import Column, Integer, String, ForeignKey
from task1.database import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class Task(Base):
    __tablename__ = 'tasks_assigned'

    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    body = Column(String(255))
    creator_id=Column(Integer)
    user_id = Column(Integer, ForeignKey('employees.emp_id'))

    #creator = relationship("Employee", back_populates="tasks")
    
class Leave(Base):
    __tablename__ = 'leave_status'

    leave_id = Column(Integer, primary_key=True, index=True)
    type = Column(String(255))
    body = Column(String(255))
    days=Column(Integer)
    from_d=Column(String(255))
    to_d=Column(String(255))
    status=Column(String(255))
    user_id = Column(Integer, ForeignKey('employees.emp_id'))

    # creator = relationship("Employee", back_populates="tasks")

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
    emp_mag_id = Column(Integer)


    # manager = relationship('Manager', back_populates="employees")

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
    
    
    # employees = relationship('Employee', back_populates="manager")

    
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
