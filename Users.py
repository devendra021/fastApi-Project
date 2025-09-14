from sqlalchemy import table
from sqlmodel import SQLModel,Field
from typing import Optional
from datetime import datetime

class BaseUser(SQLModel):
    utype:str
    full_name:str
    username:str
    emai:str
    password:str
    submittedby:str
    updatedate: datetime = Field(default_factory=datetime.now)

class User(BaseUser,table=True):
    id:int | None=Field(default=None,primary_key=True)



