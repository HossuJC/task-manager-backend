from fastapi import APIRouter, HTTPException
from src.models.user import User, UserLogin, UserResponse
from src.auth.jwt_handler import create_jwt
from src.services.auth_service import create_user, authenticate_user

router = APIRouter()

@router.post("/register")
async def register(user: User):
    """
    Registers a new user.
    
    **Parameters:**
    - **user (User):** User data to register.
    
    **Returns:**
    - **dict:** ID of the registered user and confirmation message.
    - **HTTPException:** Error 400 if the user already exists.
    """
    user_id = await create_user(user)
    if not user_id:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    return {"id": user_id, "message": "User successfully registered"}

@router.post("/login")
async def login(user: UserLogin):
    """
    Logs in and generates a JWT token.
    
    **Parameters:**
    - **user (UserLogin):** User credentials.
    
    **Returns:**
    - **dict:** Access token and token type.
    - **HTTPException:** Error 401 if the credentials are incorrect.
    """
    db_user = await authenticate_user(user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Wrong credentials")
    payload = {"id": str(db_user["_id"]), "username": db_user["username"], "email": db_user["email"]}
    token = create_jwt(payload)
    return {"access_token": token, "token_type": "bearer", "user": payload}
