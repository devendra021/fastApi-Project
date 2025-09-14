from sqlalchemy import table
from sqlmodel import SQLModel,Field
from typing import Annotated
from typing import Optional
from datetime import datetime

class CoursesBase(SQLModel):
    course_name:str=Field(lt=20,gt=5)
    department_id:Annotated[int,Field(default=None)]
    semester:str
    class_name:str
    lecture_hour:str
    submitted_by:str
    updated_at:datetime=Field(default_factory=datetime.now)


class Course(CoursesBase,table=True):
    id: int | None = Field(default=None, primary_key=True)


