from sqlalchemy import table
from sqlmodel import SQLModel,Field,DateTime
from typing import Optional
from datetime import datetime

class DepartmentBase(SQLModel):
    depart_name:str
    submittedby:str
    updatedat:datetime=Field(default_factory=datetime.now)


class Department(DepartmentBase,table=True):
    id: int | None = Field(default=None, primary_key=True)
