from sqlmodel import SQLModel, Field


class Company(SQLModel, table = True):
    id:int | None = Field(default = None, primary_key = True)
    name :str
    typeofwork : str
    salary : int

class UserInfo(SQLModel, table = True):
    id:int | None = Field(default = None, primary_key = True)
    username:str
    email:str
    budget:int

class Lead(SQLModel, table = True):
    id:int | None = Field(default = None, primary_key = True)
    name:str 
    email:str
    company:str
    message:str
    is_qualified:bool = Field(default = False)