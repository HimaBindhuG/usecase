from typing import List
from fastapi import APIRouter
from task_1 import database, oauth2, schemas, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from task_1.repository import manager
from .. import oauth2
from task_1.models import Manager

router = APIRouter(
    prefix="/manager",
    tags=['Managers']
)

get_db = database.get_db

@router.get('/')
def all(db: Session = Depends(get_db)):
    return manager.get_all(db)

@router.post('/', response_model=List[schemas.ShowManager])
def create_user(request: schemas.Manager, db: Session = Depends(get_db)):
    return manager.create_mag(request, db)


@router.get('/{mag_id}', response_model=schemas.ShowManager)
def get_user(mag_id: int, db: Session = Depends(get_db)):
    return manager.show_mag(mag_id, db)
#,current_user: schemas.Manager = Depends(oauth2.get_current_user)


@router.put('/{mag_id}', response_model=schemas.ShowManager)
def update_user(mag_id: int, request: schemas.Manager, db: Session = Depends(get_db)):
    return manager.update_mag(mag_id, request, db)
#,current_user: schemas.Manager = Depends(oauth2.get_current_user)


@router.get('/manager/{mag_id}/employees')
def get_assigned_employees(request, db: Session = Depends(get_db)):
    return manager.get_assigned_employees(request, db,mag_id=int)


