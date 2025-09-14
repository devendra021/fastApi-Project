from fastapi import FastAPI,Depends
from sqlmodel import SQLModel,create_engine,Session
import uvicorn
from Users import User,BaseUser
from Departments import Department,DepartmentBase

app=FastAPI()

engine=create_engine('sqlite:///attendance.db',echo=True)
SQLModel.metadata.create_all(engine)

def getSession():
    with Session(engine) as session:
        yield session

@app.post('/createuser')
async def createuser(user:BaseUser,session:Session=Depends(getSession)):
    db_user=User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@app.post('/add_depart')
async def adddepartment(department:DepartmentBase,session:Session=Depends(getSession)):
    department_db=Department.model_validate(department)
    session.add(department_db)
    session.commit()
    session.refresh(department_db)
    return department_db

@app.get('/getuser/{id}')
async def getUser(id:int,session:Session=Depends(getSession)):
    user=session.get(User,id)
    session.commit()
    session.refresh(user)
    return user


if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=3000)