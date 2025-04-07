from fastapi import Depends
from src.config import db
from motor.motor_asyncio import AsyncIOMotorClient
from src.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def create_user(user: User):
    """
    Creates a new user in the database.
    
    **Parameters:**
    - **user (User):** User data to register.
    
    **Returns:**
    - **str:** ID of the created user or None if the user already exists.
    """
    existing_user = await db.users.find_one({"username": user.username})
    existing_email = await db.users.find_one({"email": user.email})
    if existing_user or existing_email:
        return None

    hashed_password = pwd_context.hash(user.password)
    user_data = user.model_dump()
    user_data["password"] = hashed_password
    result = await db.users.insert_one(user_data)
    
    return str(result.inserted_id)

async def authenticate_user(username: str, password: str):
    """
    Verifies user credentials.
    
    **Parameters:**
    - **username (str):** Username or user email.
    - **password (str):** User password.
    
    **Returns:**
    - **dict:** User data if authentication is successful.
    - **None:** If authentication fails.
    """
    user = await db.users.find_one({"username": username})
    if not user:
        user = await db.users.find_one({"email": username})
    if user and pwd_context.verify(password, user["password"]):
        return user
    return None
