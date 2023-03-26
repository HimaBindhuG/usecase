import json
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.responses import JSONResponse
import requests
from jose import jwt
from task_1 import database
from task_1.database import get_db
from task_1 import models, schemas
from task_1.hashing import Hash

from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta

get_db = database.get_db


def get_all_admins(db: Session):
    return db.query(models.Admin).all()


def get_all_employees(db: Session):
    return db.query(models.Employee).all()


def get_all_managers(db: Session):
    return db.query(models.Manager).all()


def create_admin(request: schemas.Admin, db: Session):
    new_ad = models.Admin(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
        dept=request.dept,
        address=request.address,
        gender=request.gender,
        dob=request.dob,
        phone=request.phone,
        posting=request.posting
    )
    db.add(new_ad)
    db.commit()
    db.refresh(new_ad)
    return new_ad


def show_admin(admin_id: int, db: Session):
    ad = db.query(models.Admin).filter(models.Admin.admin_id == admin_id).first()
    if not ad:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Admin with the id {admin_id} is not available"
        )
    return ad.__dict__


def create_employee(request: schemas.Employee, db: Session = Depends(get_db)):
    new_emp = models.Employee(
        emp_name=request.emp_name,
        email=request.email,
        password=Hash.bcrypt(request.password),
        dept=request.dept,
        address=request.address,
        gender=request.gender,
        dob=request.dob,
        phone=request.phone,
        posting=request.posting,
        emp_mag_id=request.emp_mag_id
    )
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)

    emp_login_payload = {
        "emp_name": new_emp.emp_name,
        "email": new_emp.email,
        "password": new_emp.password,
        "dept": new_emp.dept,
        "address": new_emp.address,
        "gender": new_emp.gender,
        "dob": new_emp.dob,
        "phone": new_emp.phone,
        "posting": new_emp.posting,
        "emp_mag_id": new_emp.emp_mag_id
    }
    response = requests.post("http://127.0.0.1:3000/employee/", data=json.dumps(emp_login_payload))
    return response.json()


# def show_employee(emp_id: int, db: Session):
#     emp = db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()
#     if not emp:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Employee with the id {emp_id} is not available"
#         )
#     return emp



def show_employee(emp_id: int, db: Session):
    emp = db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()
    if not emp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with the id {emp_id} is not available"
        )
    return emp




def create_manager(request=schemas.Manager, db: Session = Depends(get_db)):
    new_mag = models.Manager(
        mag_name=request.mag_name,
        email=request.email,
        password=Hash.bcrypt(request.password),
        dept=request.dept,
        address=request.address,
        gender=request.gender,
        dob=request.dob,
        phone=request.phone,
        posting=request.posting
    )
    db.add(new_mag)
    db.commit()
    db.refresh(new_mag)
    mag_login_payload = {
        "mag_name": new_mag.mag_name,
        "email": new_mag.email,
        "password": new_mag.password,
        "dept": new_mag.dept,
        "address": new_mag.address,
        "gender": new_mag.gender,
        "dob":new_mag.dob,
        "phone":new_mag.phone,
        "posting":new_mag.posting
    }
    response=requests.post("http://127.0.0.1:9000/manager/",data=json.dumps(mag_login_payload))
    data = request.get_json()
    print(data)
    return response.json()


def show_mag(mag_id: int, db: Session = Depends(get_db)):
    mag = db.query(models.Manager).filter(models.Manager.mag_id == mag_id).first()
    if not mag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Manager with the id {mag_id} is not available")
    return mag


# def assign_manager(request,emp_id:int,mag_id:int, db: Session):
#     emp = db.query(Employee).filter_by(id=emp_id).first()
#     mag=db.query(Manager).filter_by(id=mag_id).first()
#     Employee.emp_mag_id=mag_id
#     db.commit()
#     return JSONResponse(content={'message': f'Manager assigned to employee {emp_id}'})


