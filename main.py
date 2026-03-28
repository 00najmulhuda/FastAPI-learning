from fastapi import FastAPI, Depends, HTTPException
from database import engine, get_session
from models import SQLModel, Lead
from schemas import LeadCreate, LeadResponse
from sqlmodel import Session , select

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