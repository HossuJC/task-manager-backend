from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

class User(BaseModel):
    """
    Data model for creating a user.
    
    **Attributes:**
    - **username (str):** Username.
    - **email (EmailStr):** User's email address.
    - **password (str):** User's password.
    """
    username: Annotated[str, Field(min_length=3)]
    email: Annotated[EmailStr, Field(min_length=3)]
    password: Annotated[str, Field(min_length=3)]

class UserLogin(BaseModel):
    """
    Data model for user authentication.
    
    **Attributes:**
    - **username (str):** Username.
    - **password (str):** User's password.
    """
    username: Annotated[str | EmailStr, Field(min_length=3)]
    password: Annotated[str, Field(min_length=3)]

class UserResponse(BaseModel):
    """
    Response model for user data.
    
    **Attributes:**
    - **id (str):** User ID.
    - **username (str):** Username.
    - **email (str):** User's email address.
    """
    id: str
    username: str
    email: str
