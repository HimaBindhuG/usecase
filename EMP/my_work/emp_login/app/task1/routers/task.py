from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from task1 import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from task1.repository import task
from task1 import schemas
import requests
import json
from task1.models import Task

router = APIRouter(
    prefix="/employee/task",
    tags=['Tasks']
)

get_db = database.get_db



# url = "http://127.0.0.1:9000/task/"
# # Send the new task to microservice1
# response = requests.post(url)
# # Check the response status code
# if response.status_code == 200:
#     # The task was successfully created in microservice1
#     tasks = response.json()
#     # Deserialize the received tasks using the Task schema
#     task_list = [schemas.Task(**task) for task in tasks]
#     print(task_list)
# else:
#     # There was an error retrieving the tasks from manager_microservice
#     pass


@router.get('/', response_model=List[schemas.ShowTask])
def all(db: Session = Depends(get_db)):
    return task.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Task, db: Session = Depends(get_db)):
    return task.create_task(request, db)

@router.get('/{task_id}', status_code=200, response_model=schemas.ShowTask)
def show(id: int, db: Session = Depends(get_db)):
    return task.show_task(id, db)

@router.put('/{task_id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Task, db: Session = Depends(get_db)):
    return task.update_task(id, request, db)









@router.post('/', status_code=status.HTTP_201_CREATED,)
#current_user: schemas.Employee = Depends(oauth2.get_current_user)
def create(request: schemas.Task, db: Session = Depends(get_db) ):
    return task.create_task(request, db)


# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.Employee = Depends(oauth2.get_current_user)):
#     return task.destroy(id, db)
