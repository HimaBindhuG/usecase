from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models,token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
    employee = db.query(models.Employee).filter(models.Employee.email == request.username).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(employee.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": employee.email})
    return {"access_token": access_token, "token_type": "bearer"}
#generate a jwt token and return
    #return employee