#from urllib import response
#from typing import List
#from fastapi import FastAPI,Depends,status,Response,HTTPException
from fastapi import FastAPI
#from . import schemas,models,hashing
from . import models
#from blog import database
#from .database import engine,get_db
from .database import engine
#from sqlalchemy.orm import Session
#from .hashing import Hash
from .routers import employee, task,authentication



app= FastAPI()


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(task.router)
app.include_router(employee.router)


"""def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""




