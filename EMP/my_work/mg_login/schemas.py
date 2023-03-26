from typing import List, Optional
from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    body: str

class Task(TaskBase):
    class Config():
        orm_mode = True

class Employee(BaseModel):
    name:str
    email:str
    password:str

class ShowEmployee(BaseModel):
    name:str
    email:str
    tasks : List[Task] =[]
    class Config():
        orm_mode = True

class ShowTask(BaseModel):
    title: str
    body:str
    creator: ShowEmployee

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
