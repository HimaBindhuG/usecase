from sqlalchemy.orm import Session
from task_1.database import get_db
from task_1 import models, schemas
from fastapi import Depends, HTTPException, status
from task_1.database import SessionLocal, engine
import requests, json

def get_all(db: Session):
    tasks = db.query(models.Task).all()
    return tasks

def create_task(request: schemas.Task, db: Session= Depends(get_db)):
    new_task = models.Task(title=request.title, body=request.body,creator_id=request.creator_id)
    db.add(new_task)
    db.commit() 
    db.refresh(new_task)
    task_payload = {
        "title": new_task.title,
        "body": new_task.body,
        "creator_id": new_task.creator_id
    }
    response=requests.post("http://127.0.0.1:3000/employee/task/",data=json.dumps(task_payload))
    # try:
    #     response_data = json.loads(response.text)
    # except json.JSONDecodeError:
    #     print(f"Error occurs while decoding response")
    #     response_data = None
    # return response_data
    return response.json()

def show_task(task_id: int, db: Session):
    task = db.query(models.Task).filter(models.Task.task_id == task_id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with the id {task_id} is not available")
    return task

def update_task(id: int, request: schemas.Task, db: Session):
    task = db.query(models.Task).filter(models.Task.id == id)

    if not task.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {id} not found")

    task.update(request)
    db.commit()
    return 'updated'

# def connect_tasks():
    

# def destroy(id: int, db: Session):
#     task = db.query(models.Task).filter(models.Task.id == id)

#     if not task.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Task with id {id} not found")

#     task.delete(synchronize_session=False)
#     db.commit()
#     return 'done'