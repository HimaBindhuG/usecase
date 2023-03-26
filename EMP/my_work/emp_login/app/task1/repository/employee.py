
from sqlalchemy.orm import Session
from task1 import models, schemas
from fastapi import HTTPException, status
from task1.hashing import Hash
from task1.models import Employee, Manager

def get_all(db : Session):
    return db.query(models.Employee).all()


def create_emp(request: schemas.Employee, db: Session):
    new_emp = models.Employee(
        emp_name=request.emp_name,
        email=request.email,
        password=request.password,
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
    return new_emp


def show_emp(emp_id: int, db: Session):
    emp = db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee with the id {emp_id} is not available")
    return emp


def update_emp(emp_id: int, request: schemas.Employee, db: Session):
    upd_emp = db.query(models.Employee).filter(models.Employee.emp_id == emp_id)

    if not upd_emp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Employee with id {emp_id} not found")

    upd_emp.update(dict(request))
    db.commit()
    return 'updated'