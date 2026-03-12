from fastapi import FastAPI
app = FastAPI()

@app.get("/leads")
def get_leads():
    return {"message": "this is a leads"}

@app.post("/leads")
def create_leads():
    return {"message": "create new leads"}

@app.delete("/leads")
def delete_leads():
    return {"message":"delete leads"}