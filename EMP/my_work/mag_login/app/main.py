from fastapi import FastAPI
import uvicorn
from task_1 import  models
from task_1.database import engine
from task_1.routers import task, manager, authentication,leave
from flask import Flask, jsonify, request
from flask_cors import CORS
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# origins = [
#     "http://localhost",
#     "http://localhost:4200"
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.post("/manager/")
# async def manager_login(username: str, password: str):
#     # Perform manager login validation
#     if username != "manager" or password != "password":
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     return {"message": "manager login successful"}

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(task.router)
app.include_router(manager.router)
app.include_router(leave.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)
