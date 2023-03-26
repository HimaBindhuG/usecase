import json
from sqlalchemy.orm import Session
from task1.database import get_db
from task1 import models, schemas
from fastapi import Depends, HTTPException, status
import requests

def get_all(db : Session):
    return db.query(models.Task).all()


def create_task(request: schemas.Task, db: Session):
    new_task = models.Task(title=request.title, body=request.body,creator_id = request.creator_id)
    db.add(new_task)
    db.commit() 
    db.refresh(new_task)
    return new_task


# def destroy(id: int, db: Session):
#     task = db.query(models.Task).filter(models.Task.id == id)

#     if not task.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Task with id {id} not found")

#     task.delete(synchronize_session=False)
#     db.commit()
#     return 'done'


def update_task(task_id: int, request: schemas.Task, db: Session== Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    task_payload = {
        "title": request.title,
        "body": request.body,
        "creator_id": request.creator_id
    }
    response = requests.post("http://127.0.0.1:9000/manager/task/", data=json.dumps(task_payload))
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {task_id} not found")
    updated_task = response.json()
    task.title = updated_task.get('title', task.title)
    task.body = updated_task.get('body', task.body)
    task.creator_id = updated_task.get('creator_id', task.creator_id)
    db.commit()
    return 'updated'




def create_leave(request: schemas.Leave, db: Session== Depends(get_db)):
    new_leave = models.Leave(type=request.type, body=request.body,days=request.days,from_d=request.from_d,to_d=request.to_d,status=request.status)
    db.add(new_leave)
    db.commit() 
    db.refresh(new_leave)
    leave_payload = {
        "type": new_leave.type,
        "body": new_leave.body,
        "days": new_leave.days,
        "from_d": new_leave.from_d,
        "to_d": new_leave.to_d,
        "status": new_leave.status
    }

    response=requests.post("http://127.0.0.1:9000/manager/leave/",data=json.dumps(leave_payload))
    return response.json()



def show_task(task_id: int, db: Session):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with the id {task_id} is not available")
    return task
