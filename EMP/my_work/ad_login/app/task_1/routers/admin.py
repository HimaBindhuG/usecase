from typing import List
from fastapi import APIRouter
from task_1 import database, oauth2, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from task_1.repository import admin
from .. import oauth2

router = APIRouter()

get_db = database.get_db


@router.get('/admin',response_model=List[schemas.ShowAdmin],tags=['Admins'])
def all(db: Session = Depends(get_db)):
    return admin.get_all_admins(db)


@router.get('/admin/employee',response_model=List[schemas.ShowEmployee],tags=['Employee'])
def all(db: Session = Depends(get_db)):
    return admin.get_all_employees(db)


@router.get('/admin/manager',response_model=List[schemas.ShowManager],tags=['Manager'])
def all(db: Session = Depends(get_db)):
    return admin.get_all_managers(db)

@router.post('/admin', response_model=schemas.ShowAdmin,tags=['Admins'])
def create_admin(request: schemas.Admin, db: Session = Depends(get_db)):
    return admin.create_admin(request, db)


@router.get('/admin/{admin_id}', response_model=schemas.ShowAdmin,tags=['Admins'])
def get_admin(admin_id: int, db: Session = Depends(get_db)):
    return admin.show_admin(admin_id, db)
#,current_user: schemas.Admin = Depends(oauth2.get_current_user)


# @router.put('/admin/{id}', response_model=schemas.ShowAdmin,tags=['Admins'])
# def update_user(id: int, request: schemas.Admin, db: Session = Depends(get_db),current_user: schemas.Admin = Depends(oauth2.get_current_user)):
#     return admin.update(id, request, db)




@router.post('/admin/employee', response_model=schemas.ShowEmployee, tags=['Employee'])
def create_emp(request: schemas.Employee, db: Session = Depends(get_db)):
    return admin.create_employee(request, db)

#,current_user: schemas.Employee = Depends(oauth2.get_current_user),,response_model=schemas.ShowEmployee,


@router.get('/admin/employee/{emp_id}', response_model=List[schemas.ShowEmployee], tags=['Employee'])
def get_emp(emp_id: int, db: Session = Depends(get_db)):
    return admin.show_employee(emp_id, db)


#,current_user: schemas.Employee = Depends(oauth2.get_current_user)



@router.post('/admin/manager',response_model=List[schemas.ShowManager],tags=['Manager'])
def create_mag(request: schemas.Manager, db: Session = Depends(get_db)):
    return admin.create_manager(request, db)

@router.get('admin/manager/{mag_id}', response_model=schemas.ShowManager, tags=['Manager'])
def get_mag(mag_id: int, db: Session = Depends(get_db)):
    return admin.show_mag(mag_id, db)



# @router.put('/employee/{emp_id}/manager/{mag_id}',tags=['Assign'])
# def create_emp(request, db: Session = Depends(get_db)):
#     return admin.assign_manager(request, db,mag_id=int,emp_id=int)