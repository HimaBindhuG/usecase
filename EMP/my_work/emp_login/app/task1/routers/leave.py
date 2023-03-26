from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from task1 import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from task1.repository import leave
from task1 import schemas

router = APIRouter(
    prefix="/employee/leave",
    tags=['Leaves']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowLeave])
def all(db: Session = Depends(get_db)):
    return leave.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Leave, db: Session = Depends(get_db)):
    return leave.create_leave(request, db)


@router.get('/{leave_id}', status_code=200, response_model=schemas.ShowLeave)
def show(leave_id: int, db: Session = Depends(get_db)):
    return leave.show_leave(leave_id, db)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.Employee = Depends(oauth2.get_current_user)):
#     return leave.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Task, db: Session = Depends(get_db), current_user: schemas.Employee = Depends(oauth2.get_current_user)):
    return leave.update(id, request, db)


