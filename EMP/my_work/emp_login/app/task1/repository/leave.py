import json
import requests
from sqlalchemy.orm import Session
from task1.database import get_db
from task1 import models, schemas
from fastapi import Depends, HTTPException, status
from datetime import date


def get_all(db: Session):
    leaves = db.query(models.Leave).all()
    return leaves


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

    response=requests.post("http://127.0.0.1:9000/leave/",data=json.dumps(leave_payload))
    return response.json()



def show_leave(leave_id: int, db: Session):
    leave = db.query(models.Leave).filter(models.Leave.leave_id == leave_id).first()
    if not leave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Leave with the id {leave_id} is not available")
    return leave

# def destroy(id: int, db: Session):
#     leave = db.query(models.Task).filter(models.Task.id == id)

#     if not leave.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Task with id {id} not found")

#     leave.delete(synchronize_session=False)
#     db.commit()
#     return 'done'


def update(id: int, request: schemas.Task, db: Session):
    leave = db.query(models.Task).filter(models.Task.id == id)

    if not leave.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Task with id {id} not found")

    leave.update(request)
    db.commit()
    return 'updated'



