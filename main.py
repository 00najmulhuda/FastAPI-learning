from fastapi import FastAPI
app = FastAPI()


@app.post("/leads")
def create_leads():
    return {"message": "create new leads"}

@app.delete("/leads")
def delete_leads():
    return {"message":"delete leads"}

@app.get("/leads/{lead_id}")
def get_lead(lead_id: int):
    return{"lead_id":lead_id}

@app.get("/leads")
def get_leads(page: int = 1):
    return{"page":page, "message":f"page {page} leads"}