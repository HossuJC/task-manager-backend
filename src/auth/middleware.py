from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from src.auth.jwt_handler import verify_jwt

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Retrieves the authenticated user from the JWT token.
    
    **Parameters:**
    - **credentials (HTTPAuthorizationCredentials):** HTTP credentials containing the JWT token.
    
    **Returns:**
    - **dict:** User data if the token is valid.
    - **HTTPException:** 401 error if the token is invalid.
    """
    token = credentials.credentials
    decoded = verify_jwt(token)
    if not decoded:
        raise HTTPException(status_code=401, detail="Invalid token")
    return decoded
