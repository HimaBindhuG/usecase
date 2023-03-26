from fastapi import FastAPI
import uvicorn
from task1 import  models
from task1.database import engine
from task1.routers import task, employee, authentication,leave
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

# @app.post("/employee/")
# async def employee_login(username: str, password: str):
#     # Perform employee login validation
#     if username != "employee" or password != "password":
#         raise HTTPException(status_code=401, detail="Incorrect username or password")
#     return {"message": "Employee login successful"}


models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(task.router)
app.include_router(employee.router)
app.include_router(leave.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3000)
