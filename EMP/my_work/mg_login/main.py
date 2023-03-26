from fastapi import FastAPI,status,HTTPException,Depends
from database import Base,engine, get_db
from models import Employee, Task
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from datetime import date as date_type
from passlib.context import CryptContext
import login,models,schemas


class EmployeeRequest(BaseModel):
    name:str
    email:str
    password:str
    address:str
    gender:str
    dob: date_type = Field(..., alias="date of birth")
    blood_group:str
    phone:int
    posting:str
    dept:str

#initialise app
app=FastAPI()

#create database
Base.metadata.create_all(engine)
models.Base.metadata.create_all(engine)



app.include_router(login.router)

@app.get('/',tags=["welcome page"])
def welcome():
    return "welcome! now try other methods to get employee details "

@app.get("/emp",tags=["Employee"])
def read_all_emp_list():
    #create new database session
    session = Session(bind=engine,expire_on_commit=False)
    #get all task
    emp_list=session.query(Employee).all()
    #close session
    session.close()
    
    return emp_list
    #return "read employee list"
    
@app.get('/task',tags=["Tasks"])
def read_all_tasks_from_manager(db: Session= Depends(get_db)):
    tasks=db.query(models.Task).all()
    return tasks

@app.get('/task/{id}',tags=["Tasks"])
def read_one_task_from_manager(id,db: Session= Depends(get_db)):
    tasks=db.query(models.Task).filter(models.Task.id == id).first()
    return tasks

@app.put("/task/{id}",tags=["Tasks"])
def update_tasks(id: int,title:str,body:str):
    #create new database session
    session = Session(bind=engine,expire_on_commit=False)
    #get task with given id
    task=session.query(Task).get(id)
    #update task with field when id is given
    if task:
        task.title=title
        task.body=body
        
        session.commit()
    session.close()
    
    if not task:
        raise HTTPException(status_code=404,detail=f" task with given {id} not found ")
    return task    
    #return "update employee with id {id}"
    


@app.post('/task',tags=["Tasks"])
def create_own_task(request:schemas.Task,db: Session= Depends(get_db)):
    new_task=models.Task(title=request.title,body=request.body)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@app.put("/emp/{id}",tags=["Employee"])
def update_emp(id: int,name:str,email:str,dept:str,age:int):
    #create new database session
    session = Session(bind=engine,expire_on_commit=False)
    #get emp with given id
    emp=session.query(Employee).get(id)
    #update emp with field when id is given
    if emp:
        emp.name=name
        emp.email=email
        emp.age=age
        emp.dept=dept
        session.commit()
    session.close()
    
    if not emp:
        raise HTTPException(status_code=404,detail=f"emp with given {id} not found")
    return emp    
    #return "update employee with id {id}"
    
    
pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

@app.post("/register",status_code=status.HTTP_201_CREATED,tags=["Employee"])
def create_emp(register:EmployeeRequest):
    hashedPassword = pwd_cxt.hash(register.password)
    #return "create new employee"
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)
    # create an instance of the ToDo database model
    emp_db = Employee(name = register.name,password=hashedPassword,
                        #password=register.password,
                        address=register.address,dept=register.dept,email=register.email,gender=register.gender,dob=register.dob,phone=register.phone,posting=register.posting,blood_group=register.blood_group)
    # add it to the session and commit it
    session.add(emp_db)
    session.commit()
    # grab the id given to the object from the database
    id = emp_db.id
    # close the session
    session.close()
    # return the id
    return f"created employee with id {id}"
    

@app.get("/emp/{id}",tags=["Employee"])
def get_one_emp(id: int):
    #return "read employee with id {id}"
    #create new database session
    session =Session(bind=engine, expire_on_commit=False)
    #get task with given id
    task = session.query(Employee).get(id)
    #close session
    session.close()
    #check if task exist with given id,if not raise exception
    if not task:
        raise HTTPException(status_code=404, detail=f"task with {id} not found")
    return task
    #return f"employee item with id : {task.id} and name: {task.name} and email: {task.email}"



# @app.delete("/task/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_emp(id: int):
#     #create new db session
#     session = Session(bind=engine,expire_on_commit=False)
#     #get task with id
#     task = session.query(Employee).get(id)
#     #if task exist, delete from db or raise exceptions
#     if task:
#         session.delete(task)
#         session.commit()
#         session.close()
#     else:
#         raise HTTPException(status_code=404,detail=f"task with given {id} not found")
#     return None
#     #return "delete employee with id {id}"


