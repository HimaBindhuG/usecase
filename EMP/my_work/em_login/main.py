from fastapi import FastAPI,status,HTTPException,Depends
import requests
from database import Base,engine, get_db
from models import Employee, Task
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from datetime import date as date_type
from passlib.context import CryptContext
import login,models,schemas


class EmployeeRequest(BaseModel):
    name:str
    email:str
    password:str
    address:str
    gender:str
    dob: date_type = Field(..., alias="date of birth")
    blood_group:str
    phone:int
    posting:str
    dept:str

#initialise app
app=FastAPI()

#create database
Base.metadata.create_all(engine)
models.Base.metadata.create_all(engine)



app.include_router(login.router)




# @app.delete("/task/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_emp(id: int):
#     #create new db session
#     session = Session(bind=engine,expire_on_commit=False)
#     #get task with id
#     task = session.query(Employee).get(id)
#     #if task exist, delete from db or raise exceptions
#     if task:
#         session.delete(task)
#         session.commit()
#         session.close()
#     else:
#         raise HTTPException(status_code=404,detail=f"task with given {id} not found")
#     return None
#     #return "delete employee with id {id}"


