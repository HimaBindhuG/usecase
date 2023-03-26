from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from .. import schemas
from .. import models
from ..hashing import Hash
#from ..repository import emplo

def create(request: schemas.Employee,db:Session):
    new_empl=models.Employee(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_empl)
    db.commit()
    db.refresh(new_empl)
    return new_empl

def show(id:int,db:Session):
    emplo=db.query(models.Employee).filter(models.Employee.id==id).first()
    if not emplo:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Employee with the {id} is not available")
    return emplo