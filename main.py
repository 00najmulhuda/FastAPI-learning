from fastapi import FastAPI, Depends, HTTPException, Header, Body
from database import engine, get_session
from models import Lead, UserInfo, Tag, LeadTag
from schemas import LeadCreate, LeadResponse,UserInfoCreate, LoginRequest
from sqlmodel import SQLModel, Session , select
from security import create_access_token , verify_token, pwd_context


app = FastAPI()

SQLModel.metadata.create_all(engine)
@app.post("/leads")
def create_lead(lead: LeadCreate , session:Session = Depends(get_session)):
    db_lead = Lead.model_validate(lead)
    session.add(db_lead)
    session.commit()
    session.refresh(db_lead)
    return db_lead

@app.get("/leads")
def get_leads(session:Session = Depends(get_session)):
    leads = session.exec(select(Lead)).all()
    return leads

@app.put("/leads/{lead_id}")
def update_lead(lead_id:int, lead:LeadCreate, session:Session = Depends(get_session)):
    db_lead = session.get(Lead, lead_id)
    if not db_lead:
        raise HTTPException(status_code = 404 , detail = "lead not found")
    
    lead_data = lead.model_dump()
    for key, value in lead_data.items():
        setattr(db_lead, key, value)
    session.add(db_lead)
    session.commit()
    session.refresh(db_lead)
    return db_lead

@app.delete("/leads/{lead_id}")
def delete_lead(lead_id:int, session:Session = Depends(get_session)):
    db_lead = session.get(Lead, lead_id)
    if not db_lead:
        raise HTTPException(status_code = 404, detail = "lead not found")
    session.delete(db_lead)
    session.commit()
    return {"message": "Lead delete successfully"}


@app.post("/users")
def create_user(user:UserInfoCreate, session:Session = Depends(get_session)):
    #password hash
    hashed_password = pwd_context.hash(user.password)
    #user data convert in dict
    user_data = user.model_dump()
    #replace plain pass 
    user_data["password"] = hashed_password
    #create DB object
    db_user = UserInfo(**user_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
    

@app.get("/users/{user_id}/leads")
def get_user_leads(user_id:int, session:Session = Depends(get_session)):
    leads = session.exec(select(Lead).where(Lead.user_id == user_id)).all()
    return leads

@app.delete("/users/{user_id}")
def delete_user(user_id:int, session:Session = Depends(get_session)):
    db_user = session.get(UserInfo, user_id)
    if not db_user:
        raise HTTPException(status_code = 404, detail = "user not found")
    session.delete(db_user)
    session.commit() 
    return {"message": "user delete successfully"}

@app.post("/tags") 
def create_tag(tag: Tag, session:Session = Depends(get_session)):
    session.add(tag)
    session.commit()
    session.refresh(tag)
    return tag

@app.post("/lead-tag")
def create_lead_tag(lead_tag: LeadTag, session:Session = Depends(get_session)):
    db_lead = session.get(Lead, lead_tag.lead_id)
    db_tag = session.get(Tag, lead_tag.tag_id)
    if not db_lead:
        raise HTTPException(status_code = 404, detail = "lead not found")
    if not db_tag:
        raise HTTPException(status_code = 404, detail = "tag not found")
    session.add(lead_tag)
    session.commit()
    session.refresh(lead_tag)
    return lead_tag

@app.get("/leads/{lead_id}/tags")
def get_lead_tags(lead_id: int, session:Session = Depends(get_session)):
    db_lead = session.get(Lead, lead_id)
    if not db_lead:
        raise HTTPException(status_code = 404, detail = "lead not found")
    return db_lead.tags

@app.get("/token")
def get_token():
    token = create_access_token({"sub":"1"})
    return {"access_token": token}

# @app.get("/protected")
# def protected_route(authorization: str = Header()):
#     token = authorization.split(" ")[1] #bearer token split and get token (split in 2 parts), [1] means split beare get only token which is in index 1 
#     user_id = verify_token(token) #token verify
#     return {"message": "access granted", "user_id": user_id}
#UPDATE AND FIX PROTECTED ROUTE
@app.get("/protected")
def protected_route(authorization: str = Header(...)):
    print("Auth:", authorization)
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code = 401, detail = "invalid token")
    token = authorization.split(" ")[1]
    print("Token:", token)
    user_id = verify_token(token)
    return {"message": "access granted", "user_id": user_id}
    
    

@app.post("/login")
def login(data: LoginRequest, session:Session = Depends(get_session)):
    user = session.exec(
        select(UserInfo).where(UserInfo.email == data.email)
    ).first()

    if not user:
        raise HTTPException(status_code = 404, detail = "user not found")

    is_valid = pwd_context.verify(data.password, user.password)

    if not is_valid:
        raise HTTPException(status_code = 404, detail = "invalid password")
    
    token = create_access_token({"sub": str(user.id)})
    return {"access_token": token}