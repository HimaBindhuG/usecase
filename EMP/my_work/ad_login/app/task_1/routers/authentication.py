from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from task_1 import schemas, database, models, token
from task_1.hashing import Hash
from sqlalchemy.orm import Session
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta


router = APIRouter(tags=['Authentication'])

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from task_1 import schemas, database, models, token
from task_1.hashing import Hash
from sqlalchemy.orm import Session
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

router = APIRouter(tags=['Authentication'])

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)

@router.post('/admin/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    ad = db.query(models.Admin).filter(
        models.Admin.email == request.username).first()
    if not ad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(ad.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": ad.email})
    return {"access_token": access_token, "token_type": "bearer"}

def authenticate_admin(db: Session, email: str, password: str):
    admin = db.query(models.Admin).filter(models.Admin.email == email).first()
    if not admin:
        return False
    if not Hash.verify(admin.password, password):
        return False
    return admin



# @router.post('/login')
# def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
#     ad = db.query(models.Admin).filter(
#         models.Admin.email == request.username).first()
#     if not ad:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Invalid Credentials")
#     if not Hash.verify(ad.password, request.password):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Incorrect password")

#     access_token = token.create_access_token(data={"sub": ad.email})
#     return {"access_token": access_token, "token_type": "bearer"}
