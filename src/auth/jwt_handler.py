from datetime import datetime, timedelta, timezone
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "secrettestkey")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

def create_jwt(data: dict):
    """
    Generates a JWT token with the provided data.
    
    **Parameters:**
    - **data (dict):** Information to include in the token.
    
    **Returns:**
    - **str:** Encoded JWT token.
    """
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_jwt(token: str):
    """
    Verifies and decodes a JWT token.
    
    **Parameters:**
    - **token (str):** JWT token to verify.
    
    **Returns:**
    - **dict:** Decoded data if the token is valid.
    - **None:** If the token is invalid.
    """
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except:
        return None
