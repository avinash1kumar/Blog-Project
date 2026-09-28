import bcrypt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from sqlmodel import Session
from model.user import User
from db import get_session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()


# ? AUTHENTICATION PART (bcrypt to hash password)

def hash_password(password: str) ->str:
    password_bytes = password.encode("utf-8")
    
    salt = bcrypt.gensalt()
    
    hashed_password=bcrypt.hashpw(
        password_bytes,
        salt
    )
    
    return hashed_password.decode("utf-8")

def verify_password(user_password: str, db_password: str) -> bool:
    db_password = db_password.encode("utf-8")
    user_password = user_password.encode("utf-8")
    
    return bcrypt.checkpw(user_password, db_password)
    
# ! bcrypt.checkpw(loginpassword, db_hashed_password) if you don't follow this structure then it give error


# ? AUTHORIZATION PART (jwt)

SECRET_KEY = os.getenv("JWT_SECRET_KEY")   
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data: dict):
    # * copy data first
    to_encode = data.copy()
    
    # * create expiration time for token
    expire = datetime.now(timezone.utc)+timedelta(minutes=30)
    
    to_encode.update({
        "exp": expire
    })
    
    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return token

# ? verify_token function

security = HTTPBearer()
def verify_token(credentials: HTTPAuthorizationCredentials):
    token = credentials.credentials
    
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
        

# ? get user by verifying token
# * i am writing this function here because this content will be use in every protected routes. So instead of writing same thing again and again make it a function and call it when required

def get_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
):
    payload = verify_token(credentials)
    
    user_id = payload.get("sub")
    
    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail= "Invalid token"
        )
        
    user = session.get(User, int(user_id))
    
    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    
    return user