
from sqlalchemy.orm import Session
from task_1 import database
from task_1 import models, schemas
from fastapi import HTTPException, status
from task_1.hashing import Hash
from task_1.models import Employee

get_db = database.get_db


def get_all(db : Session):
    return db.query(models.Manager).all()

def create_mag(request: schemas.Manager, db: Session):
    new_mag = models.Manager(
        mag_name=request.mag_name, 
        email=request.email, 
        password=request.password,
        dept=request.dept,
        address=request.address,
        gender=request.gender,
        dob=request.dob,
        phone=request.phone,
        posting=request.posting)
    db.add(new_mag)
    db.commit()
    db.refresh(new_mag)
    return new_mag




def show_mag(mag_id: int, db: Session):
    mag = db.query(models.Manager).filter(models.Manager.mag_id == mag_id).first()
    if not mag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Manager with the id {mag_id} is not available")
    return mag


def update_mag(mag_id: int, request: schemas.Manager, db: Session):
    upd_mag = db.query(models.Manager).filter(models.Manager.mag_id == mag_id)

    if not upd_mag.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Manager with id {mag_id} not found")

    upd_mag.update(request)
    db.commit()
    return 'updated'
########################

def get_assigned_employees(request,mag_id:int, db: Session):
    emp=db.query(Employee).filter_by(emp_mag_id=mag_id).all()
    return {'employees':emp}