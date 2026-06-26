from pydantic import BaseModel, Field, EmailStr
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
    username:str = Field(min_length = 3, max_length = 30, pattern = r"^[a-zA-Z0-9_]+$")
    email: EmailStr = Field(max_length = 200)
    budget:int
    password:str = Field(min_length = 8, max_length = 24)

class LoginRequest(BaseModel):
    email: str
    password: str