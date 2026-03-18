from sqlmodel import SQLModel, Field, create_engine, Session

class Company(SQLModel, table = True):
    id:int | None = Field(default = None, primary_key = True)
    name:str
    typeofwork:str
    salary:int

class UserInfo(SQLModel,table=True):
    id:int | None = Field(default = None, primary_key=True)
    email:str
    username:str
    budget:int

DATABASE_URL = "postgresql://postgres:admin123@localhost/fastapi_learning"
engine = create_engine(DATABASE_URL)

def create_table():
    SQLModel.metadata.create_all(engine)

create_table()