from sqlmodel import SQLModel,Field,Session
from datetime import datetime

class StudentBase(SQLModel):
    full_Name:str
    departmentid:int
    class_name:str
    submittedby:str
    updatedat:datetime=Field(default_factory=datetime.now)


class Student(StudentBase,table=True):
    id: int | None = Field(default=None, primary_key=True)
