from typing import List, Optional, Union
from pydantic import BaseModel


# class TaskBase(BaseModel):
#     title: str
#     body: str

# class Task(TaskBase):
#     class Config():
#         orm_mode = True

class Employee(BaseModel):
    emp_name:str
    email:str
    password:str
    dept :str
    address:str
    gender:str
    dob:str
    phone:str
    posting:str
    emp_mag_id:int
    
    class Config():
        orm_mode = True
    

class ShowEmployee(BaseModel):
    emp_name:str
    email:str
    dept :str
    address:str
    gender:str
    dob:str
    phone:str
    posting:str
    emp_mag_id:int
    
    class Config():
        orm_mode = True

class Admin(BaseModel):
    name:str
    email:str
    password:str
    dept :str
    address:str
    gender:str
    dob:str
    phone:str
    posting:str

        
class Manager(BaseModel):
    mag_name:str
    email:str
    password:str
    dept :str
    address:str
    gender:str
    dob:str
    phone:str
    posting:str
    
    class Config():
        orm_mode = True
    
class ShowManager(BaseModel):
    mag_name:str
    email:str    
    dept :str
    address:str
    gender:str
    dob:str
    phone:str
    posting:str
    # tasks : List[Task] =[]
    class Config():
        orm_mode = True
        
    

class ShowAdmin(BaseModel):
    name:str
    email:str
    dept :str
    address:str
    gender:str
    dob:str
    phone:str
    posting:str
    employees: List[Union[Employee, Manager]] = []


    class Config():
        orm_mode = True

# class EmpMag(Employee,Manager):
#     id=int
#     name=str
#     empmag=List[Employee]=[]

#     class Config():
#         orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
