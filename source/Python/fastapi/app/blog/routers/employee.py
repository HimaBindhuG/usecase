from fastapi import APIRouter
from .. import database,schemas,models
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException
#from ..hashing import Hash
from ..repository import employee1


router=APIRouter(
    prefix="/employee",
    tags=['employees']
)
get_db=database.get_db

@router.post('{prefix}', response_model=schemas.LoginEmployee)
def create_user(request: schemas.Employee,db:Session = Depends(get_db)):
   employee1.create(request,db)

@router.get('{prefix}/{id}',response_model=schemas.ShowEmployee)
def get_user(id:int,db:Session = Depends(get_db)):
    return employee1.show(id,db)