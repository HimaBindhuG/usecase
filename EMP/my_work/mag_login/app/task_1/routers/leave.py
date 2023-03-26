from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from task_1 import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from task_1.repository import leave
from task_1 import schemas

router = APIRouter(
    prefix="/manager/leave",
    tags=['Leaves']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowLeave])
def all(db: Session = Depends(get_db)):
    return leave.get_all(db)
#, current_user: schemas.Manager = Depends(oauth2.get_current_user)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Leave, db: Session = Depends(get_db)):
    return leave.create_leave(request, db)
#, current_user: schemas.Employee = Depends(oauth2.get_current_user)

@router.put('/{leave_id}', status_code=status.HTTP_202_ACCEPTED)
def update(leave_id: int, request: schemas.Leave, db: Session = Depends(get_db)):
    return leave.update_leave(leave_id, request, db)
#, current_user: schemas.Manager = Depends(oauth2.get_current_user)

@router.get('/{leave_id}', status_code=200, response_model=schemas.ShowLeave)
def show(leave_id: int, db: Session = Depends(get_db)):
    return leave.show_leave(leave_id, db)
#, current_user: schemas.Manager = Depends(oauth2.get_current_user)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.Employee = Depends(oauth2.get_current_user)):
#     return leave.destroy(id, db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, request: schemas.Task, db: Session = Depends(get_db), current_user: schemas.Employee = Depends(oauth2.get_current_user)):
#     return leave.update(id, request, db)


