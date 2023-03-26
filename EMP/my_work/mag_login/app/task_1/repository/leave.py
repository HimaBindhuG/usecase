import json
import requests
from sqlalchemy.orm import Session
from task_1.database import get_db
from task_1 import models, schemas
from fastapi import Depends, HTTPException, status


def get_all(db: Session):
    leaves = db.query(models.Leave).all()
    return leaves


def create_leave(request: schemas.Leave, db: Session):
    new_leave = models.Leave(type=request.type, body=request.body,days=request.days,from_d=request.from_d,to_d=request.to_d,status=request.status)
    db.add(new_leave)
    db.commit() 
    db.refresh(new_leave)
    return new_leave


def update_leave(leave_id: int, request: schemas.Leave, db: Session== Depends(get_db)):
    leaves = db.query(models.Leave).filter(models.Leave.leave_id == leave_id).first()
    leave_payload = {
        "type": request.type,
        "body": request.body,
        "days":request.days,
        "from_d":request.from_d,
        "to_d":request.to_d,
        "status":request.status
    }
    response = requests.post("http://127.0.0.1:3000/employee/leave/", data=json.dumps(leave_payload))
    if not leaves:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Leave with id {leave_id} not found")

    # leaves.update(request)
    updated_leave = response.json()
    leaves.type = updated_leave.get('type', leaves.type)
    leaves.body = updated_leave.get('body', leaves.body)
    leaves.days = updated_leave.get('days', leaves.days)
    leaves.from_d = updated_leave.get('from_d', leaves.from_d)
    leaves.to_d = updated_leave.get('to_d', leaves.to_d)
    leaves.status = updated_leave.get('status', leaves.status)
    db.commit()
    return 'updated'




def show_leave(leave_id: int, db: Session):
    leave = db.query(models.Leave).filter(models.Leave.leave_id == leave_id).first()
    if not leave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Leave with the id {leave_id} is not available")
    return leave

# def destroy(id: int, db: Session):
#     leave = db.query(models.Leave).filter(models.Leave.id == id)

#     if not leave.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Leave with id {id} not found")

#     leave.delete(synchronize_session=False)
#     db.commit()
#     return 'done'


# def update(id: int, request: schemas.Leave, db: Session):
#     leave = db.query(models.Leave).filter(models.Leave.id == id)

#     if not leave.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Leave with id {id} not found")

#     leave.update(request)
#     db.commit()
#     return 'updated'



