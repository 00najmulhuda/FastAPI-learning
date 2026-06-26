from sqlmodel import SQLModel, Field
from pydantic import Field, EmailStr

#response_model ---------------------------------------------
#input model
class RegisterRequest(SQLModel):
    username : str = Field(min_length = 3, max_length = 30, pattern = r"^[a-zA-Z0-9_]+$")
    email : EmailStr 
    password : str = Field(min_length = 8, max_length = 24)

class LoginRequest(SQLModel):
    email : EmailStr
    password : str = Field(min_length = 8, max_length = 24)