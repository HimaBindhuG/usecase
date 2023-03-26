from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
import schemas, database, models, oauth2,blog
from sqlalchemy.orm import Session

router = APIRouter()


get_db = database.get_db

@router.get('/emp', response_model=List[schemas.ShowEmployee])
def all(db: Session = Depends(get_db),current_user: schemas.Employee = Depends(oauth2.get_current_user)):
    return blog.get_all_emp(db)

@router.get('/task', response_model=List[schemas.ShowTask])
def all(db: Session = Depends(get_db),current_user: schemas.Task = Depends(oauth2.get_current_user)):
    return blog.get_all_tasks(db)

###########################################

@router.get('task/{id}/', status_code=200, response_model=schemas.ShowTask)
def show(id:int, db: Session = Depends(get_db),current_user: schemas.Task = Depends(oauth2.get_current_user)):
     return blog.show_task(id,db)

@router.get('emp/{id}/', status_code=200, response_model=schemas.ShowEmployee)
def show(id:int, db: Session = Depends(get_db),current_user: schemas.Employee = Depends(oauth2.get_current_user)):
    return blog.show_emp(id,db)

###########################################

@router.post('/register', status_code=status.HTTP_201_CREATED,)
def create(request: schemas.Employee, db: Session = Depends(get_db),current_user: schemas.Employee = Depends(oauth2.get_current_user)):
    return blog.create_emp(request, db)

######################################


@router.put('task/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Task, db: Session = Depends(get_db),current_user: schemas.Task = Depends(oauth2.get_current_user)):
    return blog.update_task(id,request, db)

@router.put('emp/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Employee, db: Session = Depends(get_db),current_user: schemas.Employee = Depends(oauth2.get_current_user)):
    return blog.update_emp(id,request, db)

######################################

# @router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def destroy(id:int, db: Session = Depends(get_db),current_user: schemas.Employee = Depends(oauth2.get_current_user)):
#     return Task.destroy(id,db)