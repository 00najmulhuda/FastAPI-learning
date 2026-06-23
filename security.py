from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, Depends
import os
from dotenv import load_dotenv
from sqlmodel import Session, select
from database import get_session
from auth_models import AuthUser
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
  tokenUrl = "/auth/login"
)



load_dotenv()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
    )
#hash_password -----------------------
def hash_password(password :str):
    return pwd_context.hash(password)


#verify_password-----------------------
def verify_password(
    plain_password : str,
    hash_password :str):

    return pwd_context.verify(
        plain_password,
        hash_password
    )



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire}) #expiry add in payload
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM) #token build here
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM]) #token verifying jwt.decode means token is valid , expire or not , do secret key match
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code = 401, detail = "Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code = 401, detail = "Invalid token")

#RBAC this function - as a reusable dependency-------------------------------------
def get_current_user(
    token : str = Depends(oauth2_scheme),
    session : Session = Depends(get_session)
):
   user_id = verify_token(token)

   db_user = session.exec(
    select(AuthUser)
    .where(AuthUser.id == int(user_id))
   ).first()

   if not db_user:
    raise HTTPException(status_code = 401, detail = "user not found")

   return db_user


def require_role(required_role : str):
    def role_checker(current_user : AuthUser = Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(
                status_code = 403,
                detail = "access denied"
            )
            return current_user
    return role_checker
