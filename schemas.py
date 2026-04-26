from pydantic import BaseModel
from typing import Optional


class LeadCreate(BaseModel):
    name:str
    email:str
    company:str
    message:str
    user_id:int

class LeadResponse(BaseModel):
    id:int 
    name:str
    email:str
    company:str
    message:str
    is_qualified:bool

class UserInfoCreate(BaseModel):
    username:str
    email:str
    budget:int
    password:str

class LoginRequest(BaseModel):
    email: str
    password: str