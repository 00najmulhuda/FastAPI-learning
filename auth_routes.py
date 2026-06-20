from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from auth_models import AuthUser
from auth_schemas import RegisterRequest
from security import hash_password

router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)

@router.post("/register")
def register_user(
    user : RegisterRequest,
    session : Session = Depends(get_session)
):
  check_email = session.exec(select(AuthUser).where(AuthUser.email == user.email)).first()
  
  hashed_pw = hash_password(user.password)
  db_user = AuthUser(
    username = user.username,
    email = user.email,
    hashed_password = hashed_pw
  )
  session.add(db_user)
  session.commit()
  session.refresh(db_user)

  return {
    "msg": "user registered successfully"
  }
