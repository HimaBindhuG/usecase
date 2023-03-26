from fastapi import APIRouter,Depends, HTTPException,status
import schemas,database,models
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(tags=["Authentication"])

@router.post('/login')
def login1(request:schemas.Login,db:Session = Depends(database.get_db)):
    empl = db.query(models.Employee).filter(models.Employee.name == request.username).first()
    if not empl:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Invalid Credentials")
        
    return empl












































































































# from datetime import date
# import uvicorn
# from fastapi import FastAPI
# import py_functions
# import config
# import pyodbc
# import json
# import pywhatkit


# app=FastAPI()

# def connect_db(pwd):
#     driver = config.DRIVER
#     server = config.SERVER
#     database = config.DATABASE
#     uid = config.UID
#     pwd = pwd
#     trust = config.TRUST
#     con_string = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd}"
#     cnxn=pyodbc.connection(con_string)
#     cnxn.autocommit = True
#     cursor = cnxn.cursor()
#     print("connection successful with database")
#     return cnxn,cursor

# with open("SQL/password.json") as f:
#     data =json.load(f)
# pwd=data['pass']

# cnxn,cursor=connect_db(pwd)

# @app.get('/')
# def get_data(search:str = ""):
#     df = py_functions.fetch_data(search,cnxn)
#     return df.to_dict('r')

# @app.post('/search/')
# def search_video(search:str):
#     pywhatkit.playonyt(str(search))
    
# @app.post('/signup')
# def signup(name = str,address=str,dept=str,email=str,gender=str,dob=date,phone=int,posting=str,blood_group=str,password=str):
#     if "@" not in email:
#         return{"email not valid"}
#     if len(password) <5 or "#" not in password: 
#         return{"password not secure input 6 digit and add # for security"}
#     user_exist = py_functions.check_user_exist(email,cnxn)
#     if user_exist ==0:
#         signup_query =py_functions.signup_data(name,email,phone,password,dept,gender,dob,posting,blood_group,address)
#         cursor.execute(signup_query)
#         return{"status":"Sign up successful, please login with same credentials"}
#     else:
#         return {"status":"email id already exist"}
    
# @app.post("/login")
# def login(email:str,password:str):
#     user_exist = py_functions.check_user_details(email,password,cnxn)
#     if user_exist>0:
#         return {"status","login successful access granted"}
#     else:
#         return {"status","login error acces not granted"}
    
    
# @app.post('/auth/')
# def get_user_auth(email: str):
#     passcode = py_functions.send_auth_code(email,cursor)
#     py_functions.generate_auth_email(passcode,[email])
#     return {"status":'Sent Passcode'}


# @app.post('/forget/')
# def forget(email: str,passcode:int,new_pass:str):
#     validate=py_functions.validate_passcode(email,passcode,cnxn)
#     if validate:
#         passcode = py_functions.update_password(email,new_pass,cursor)
#         py_functions.generate_password_change_email([email])
#         return {"status":'Success'}
#     else:
#         return {"status":"Passcode is wrong"}


# if __name__ == "__login__":
#     uvicorn.run(app,host ="127.0.0.1",port = 8000)

    
    