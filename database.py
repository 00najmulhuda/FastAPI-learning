import os  #python tool for read data
from dotenv import load_dotenv #this read .env file 
from sqlmodel import SQLModel, create_engine, Session

load_dotenv() #means load .env 
DATABASE_URL = os.getenv("DATABASE_URL") #in .env file find DATABASE_URL and give me

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session :
        yield session 
