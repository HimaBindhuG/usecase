from pydantic import BaseModel
from typing import List,Optional, Union


class TaskBase(BaseModel):
    title:str
    body:str
    class Config():
        orm_mode = True
    

class Task(TaskBase):
    class Config():
        orm_mode = True

class Employee(BaseModel):
    name:str
    phone:str
    address:str
    blood:str
    dept:str
    posting:str
    email:str
    password:str
    class Config():
        orm_mode = True

class LoginEmployee(BaseModel):
    name:str 
    email:str
    class Config():
        orm_mode = True

class ShowEmployee(LoginEmployee):
    
    Tasks:List[Task]
    class Config():
        orm_mode = True



class ShowTask(BaseModel):
    title:str
    body:str
    creator:ShowEmployee
    
    class Config():
        orm_mode = True
  
class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email:Optional[str]=None