from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from task_1 import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from task_1.repository import task
from task_1 import schemas


router = APIRouter(
    prefix="/manager/task",
    tags=['Tasks']
)

get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowTask])
def all(db: Session = Depends(get_db)):
    #tasks=db.query(models.Task).all()
    return task.get_all(db)
#, current_user: schemas.Manager = Depends(oauth2.get_current_user)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Task, db: Session = Depends(get_db)):
    return task.create_task(request, db)
#, current_user: schemas.Manager = Depends(oauth2.get_current_user)

@router.get('/{task_id}', status_code=200, response_model=schemas.ShowTask)
def show(task_id: int, db: Session = Depends(get_db)):
    return task.show_task(task_id, db)
#, current_user: schemas.Manager = Depends(oauth2.get_current_user)

# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, request: schemas.Task, db: Session = Depends(get_db)):
#     return task.update_task(id, request, db)
    
# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.Manager = Depends(oauth2.get_current_user)):
#     return task.destroy(id, db)


# @router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, request: schemas.Task, db: Session = Depends(get_db), current_user: schemas.Manager = Depends(oauth2.get_current_user)):
#     return task.update_task(id, request, db)


