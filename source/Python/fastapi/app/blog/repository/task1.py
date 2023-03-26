from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from .. import schemas
from .. import models

def get_all(db: Session):
    tasks = db.query(models.Task).all()
    return tasks


def create(request: schemas.Task,db:Session):
    new_tasks = models.Task(title=request.title,body=request.body,user_id=1)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    return new_tasks

def destroy(id:int, db:Session):
    task = db.query(models.Task).filter(models.Task.id == id)
    
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with id {id} not found")
    db.query(models.Task).filter(models.Task.id == id)
    task.delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(id:int,request:schemas.Task, db:Session):
    task = db.query(models.Task).filter(models.Task.id == id)
   
    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with id {id} not found")
    task.update({'title':'updated title'})
    db.commit()
    return 'updated'

def show(id:int, db:Session):
    task = db.query(models.Task).filter(models.Task.id ==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Task with the {id} is not available")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail':f"Task with the {id} is not available"}
    return task