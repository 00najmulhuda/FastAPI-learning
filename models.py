from sqlmodel import SQLModel, Field , Relationship


class Company(SQLModel, table = True):
    id:int | None = Field(default = None, primary_key = True)
    name :str
    typeofwork : str
    salary : int

class UserInfo(SQLModel, table = True):
    id:int | None = Field(default = None, primary_key = True)
    username:str
    email:str
    budget:int
    leads:list ["Lead"] = Relationship(back_populates = "user")


class LeadTag(SQLModel, table = True):
    lead_id: int = Field(primary_key = True, foreign_key = "lead.id")
    tag_id: int = Field(primary_key = True, foreign_key = "tag.id")


class Lead(SQLModel, table = True):
    id:int | None = Field(default = None, primary_key = True)
    name:str 
    email:str
    company:str
    message:str
    is_qualified:bool = Field(default = False)
    user_id:int = Field(foreign_key = "userinfo.id", ondelete = "CASCADE")
    user:"UserInfo" = Relationship(back_populates = "leads")
    tags: list["Tag"] = Relationship(back_populates = "leads", link_model = LeadTag)

class Tag(SQLModel, table = True):
    id: int | None = Field(default = None, primary_key = True)
    name: str
    leads: list["Lead"] = Relationship(back_populates = "tags", link_model = LeadTag)

