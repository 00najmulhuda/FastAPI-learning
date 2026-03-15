#SQLModel learning
from sqlmodel import SQLModel,Field,create_engine,Session 

class Lead(SQLModel,table = True):
    id: int | None = Field(default = None, primary_key = True)
    name:str
    company:str
    budget:int

DATABASE_URL = "postgresql://postgres:admin123@localhost/fastapi_learning"
engine = create_engine(DATABASE_URL)

def create_table():
    SQLModel.metadata.create_all(engine)

create_table()