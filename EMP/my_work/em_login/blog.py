from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException,status

def get_all_tasks(db: Session):
    tasks = db.query(models.Task).all()
    return tasks

def get_all_emp(db: Session):
    emp = db.query(models.Employee).all()
    return emp

def create_task(request: schemas.Task,db: Session):
    new_task = models.Task(title=request.title, body=request.body,user_id=1)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def create_emp(request: schemas.Employee,db: Session):
    new_emp = models.Employee(name=request.name, email=request.email,user_id=1)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

# def destroy(id:int,db: Session):
#     task = db.query(models.Task).filter(models.Task.id == id)

#     if not task.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Task with id {id} not found")

#     task.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

def update_task(id:int,request:schemas.Task, db:Session):
    task = db.query(models.Task).filter(models.Task.id == id)

    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with id {id} not found")

    task.update(request)
    db.commit()
    return 'updated'

def update_emp(id:int,request:schemas.Employee, db:Session):
    emp = db.query(models.Employee).filter(models.Employee.id == id)

    if not emp.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Employee with id {id} not found")

    emp.update(request)
    db.commit()
    return 'updated'

def show_task(id:int,db:Session):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with the id {id} is not available")
    return task

def show_emp(id:int,db:Session):
    emp = db.query(models.Employee).filter(models.Employee.id == id).first()
    if not emp:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Employee with the id {id} is not available")
    return emp