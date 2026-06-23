from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from auth_models import AuthUser
from auth_schemas import RegisterRequest, LoginRequest
from security import hash_password, create_access_token, verify_password, verify_token
from security import get_current_user
from security import oauth2_scheme, require_role


router = APIRouter(
    prefix = "/auth",
    tags = ["Authentication"]
)

#Register route ------------------------------------------------------------------
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


#Login route ----------------------------------------------
@router.post("/login")
def login_user(user : LoginRequest, session : Session = Depends(get_session)):
  check_email = session.exec(
    select(AuthUser)
    .where(AuthUser.email == user.email)
  ).first()
  if not check_email:
    raise HTTPException(
      status_code = 401,
      detail = "invalid email or password"
    )
  
  if not verify_password(
    user.password,
    check_email.hashed_password
  ):
    raise HTTPException(status_code = 401, detail = "invalid email or password")

  access_token = create_access_token(
    {
      "sub" : str(check_email.id),
      "role" : check_email.role
    }
  )

  return {
    "access_token" : access_token,
    "token_type" : "Bearer"
  }

#Profile - protected route-----------------------------------------------------------
@router.get("/profile")
def get_profile(token : str = Depends(oauth2_scheme)):
  user_id = verify_token(token)

  return {
    "message" : "protected route access granted",
    "user_id" : user_id
  }

#get user detail Me route --------------------------------------
@router.get("/me")
def get_me(
  current_user = Depends(get_current_user)
):
   return{
    "id" : current_user.id,
    "username" : current_user.username,
    "email" : current_user.email,
    "role" : current_user.role
   }

#admin - only route----------------------------------------
@router.get("/admin")
def admin_dashboard(
  current_user : AuthUser = Depends(require_role("admin"))
):
   return {
    "message" : "welcome admin",
    "user" : current_user.username
   }