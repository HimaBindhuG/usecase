from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from ..  import schemas,database,models,oaut2
from sqlalchemy.orm import Session
from ..repository import task1

router = APIRouter(
    prefix=".Employee",
    tags=['EMPLOYEE']
)
get_db=database.get_db

@router.get('/', response_model=List[schemas.ShowEmployee])
def all(db:Session = Depends(get_db),current_emp:schemas.Employee = Depends(oaut2.get_current_emp)):
    return task1.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Task,db:Session = Depends(get_db)):#,current_emp:schemas.Employee = Depends(oaut2.get_current_emp)):
    return task1.create(request,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db),current_emp:schemas.Employee = Depends(oaut2.get_current_emp)):
    return task1.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Task,db:Session = Depends(get_db),current_emp:schemas.Employee = Depends(oaut2.get_current_emp)):
  return task1.update(id,request,db)

#@app.get('/blog', response_model=List[schemas.ShowTask],tags=['blogs'])
#def all(db:Session = Depends(get_db)):
 #   blogs = db.query(models.Task).all()
  #  return blogs

@router.get('/{id}',status_code=200,response_model=schemas.ShowTask)
def show(id:int,db:Session = Depends(get_db),current_emp:schemas.Employee = Depends(oaut2.get_current_emp)):
    return task1.show(id,db)
