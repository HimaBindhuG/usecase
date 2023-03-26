from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from task_1 import token, database
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = None
    try:
        db = database.SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    email = token.verify_token(token, credentials_exception)
    admin = token.authenticate_admin(db, email)
    if admin is None:
        raise credentials_exception
    return admin







# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from task_1 import token

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# def get_current_user(data: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     return token.verify_token(data, credentials_exception)
