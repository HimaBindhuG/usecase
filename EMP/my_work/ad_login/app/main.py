import uvicorn
from task_1 import  models
from task_1.database import engine
from task_1.routers import  admin, authentication
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200"
]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:4200"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
    
# )
# @app.post("/admin/")
# async def admin_login(username: str, password: str):
#     # Perform admin login validation
#     if username != "admin" or password != "password":
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     return {"message": "Admin login successful"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(admin.router)



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
