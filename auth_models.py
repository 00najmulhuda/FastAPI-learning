from sqlmodel import SQLModel, Field

#AuthUser model -----------------------------------------------------
class AuthUser(SQLModel, table = True):
    id : int | None = Field(
        default = None,
        primary_key = True
    )
    username : str
    email : str
    hashed_password : str
    role : str = "user"