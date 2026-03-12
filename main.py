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

@app.get("/users/{user_id}")
def get_user(user_id:int, page:int = 1):
    return{"user_id":user_id, "page":page}

@app.get("/products/{product_id}")
def get_product(product_id: int, category: str = "all"):
    return {"product_id":product_id, "category":category}

@app.get("/orders/{order_id}")
def get_order(order_id: int , status: str = "pending"):
    return{"order_id":order_id, "status":status}
