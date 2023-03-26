from fastapi import FastAPI,status,HTTPException
from database import Base,engine,Employee
from pydantic import BaseModel
from sqlalchemy.orm import Session

class EmployeeRequest(BaseModel):
    name:str
    email:str
    age:int
    dept:str

#create database
Base.metadata.create_all(engine)

#initialise app
app=FastAPI()

@app.get('/')
def emp():
    return "welcome! now try other methods to get employee details "

@app.get("/emp")
def read_emp_list():
    #create new database session
    session = Session(bind=engine,expire_on_commit=False)
    #get all emp
    emp_list=session.query(Employee).all()
    #close session
    session.close()
    
    return emp_list
    #return "read employee list"

@app.post("/emp",status_code=status.HTTP_201_CREATED)
def create_emp(emp:EmployeeRequest):
    #return "create new employee"
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)
    # create an instance of the ToDo database model
    emp_db = Employee(name = emp.name,age=emp.age,dept=emp.dept,email=emp.email)
    # add it to the session and commit it
    session.add(emp_db)
    session.commit()
    # grab the id given to the object from the database
    id = emp_db.id
    # close the session
    session.close()
    # return the id
    return f"created employee with id {id}"
    

@app.get("/emp/{id}")
def get_emp(id: int):
    #return "read employee with id {id}"
    #create new database session
    session =Session(bind=engine, expire_on_commit=False)
    #get emp with given id
    emp = session.query(Employee).get(id)
    #close session
    session.close()
    #check if emp exist with given id,if not raise exception
    if not emp:
        raise HTTPException(status_code=404, detail=f"emp with {id} not found")
    return emp
    #return f"employee item with id : {emp.id} and name: {emp.name} and email: {emp.email}"

@app.put("/emp/{id}")
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

@app.delete("/emp/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_emp(id: int):
    #create new db session
    session = Session(bind=engine,expire_on_commit=False)
    #get emp with id
    emp = session.query(Employee).get(id)
    #if emp exist, delete from db or raise exceptions
    if emp:
        session.delete(emp)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404,detail=f"emp with given {id} not found")
    return None
    #return "delete employee with id {id}"


