from sqlmodel import SQLModel, Field

#response_model ---------------------------------------------
#input model
class RegisterRequest(SQLModel):
    username : str
    email : str
    password : str

class LoginRequest(SQLModel):
    email : str
    password : str