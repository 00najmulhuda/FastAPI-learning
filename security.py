from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "mysecretkey"
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