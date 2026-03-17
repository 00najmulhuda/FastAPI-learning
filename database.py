from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:admin123@localhost/fastapi_learning"
engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session :
        yield session 
