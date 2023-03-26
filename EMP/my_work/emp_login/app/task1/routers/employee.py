from typing import List
from fastapi import APIRouter
from task1 import database, oauth2, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from task1.repository import employee
from .. import oauth2
from task1.models import Employee, Manager


router = APIRouter(
    prefix="/employee",
    tags=['Employees']
)

get_db = database.get_db

@router.get('/',response_model=List[schemas.ShowEmployee])
def all(db: Session = Depends(get_db)):
    return employee.get_all(db)

@router.post('/', response_model=List[schemas.ShowEmployee], status_code=status.HTTP_201_CREATED,)
def create_emp(request: schemas.Employee, db: Session = Depends(get_db)):
    return employee.create_emp(request, db)
# response_model=schemas.ShowEmployee

@router.get('/{emp_id}', response_model=schemas.ShowEmployee)
def get_emp(emp_id: int, db: Session = Depends(get_db)):
    return employee.show_emp(emp_id, db)
#,current_user: schemas.Employee = Depends(oauth2.get_current_user)

@router.put('/{emp_id}', response_model=schemas.ShowEmployee)
def update_emp(emp_id: int, request: schemas.Employee, db: Session = Depends(get_db)):
    return employee.update_emp(emp_id, request, db)
