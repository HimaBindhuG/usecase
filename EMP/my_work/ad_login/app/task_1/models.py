from sqlalchemy import Column, Integer, String, ForeignKey
from task_1.database import Base
from sqlalchemy.orm import relationship


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



    
    
    

