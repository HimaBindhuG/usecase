from typing import List, Optional
from pydantic import BaseModel
from task1.models import Employee, Manager


class TaskBase(BaseModel):
    title: str
    body: str
    creator_id:int

class Task(TaskBase):
    class Config():
        orm_mode = True

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
   

class Leave(BaseModel):
    type: str
    body: str
    days:int
    from_d:str
    to_d:str
    status:str
    
    
    


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

class ShowTask(BaseModel):
    title: str
    body:str
    creator_id:int
    # creator: ShowEmployee

    class Config():
        orm_mode = True
        
class ShowLeave(BaseModel):
    type: str
    body: str
    days:int
    from_d:str
    to_d:str
    status:str
    leaves : List[Leave] =[]
    # creator: ShowEmployee

    class Config():
        orm_mode = True


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
    

class ShowAdmin(BaseModel):
    name:str
    email:str
    dept :str
    address:str
    gender:str
    dob:str
    phone:str
    posting:str
    emp : List[Employee] =[]
    class Config():
        orm_mode = True    
    
    
class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
