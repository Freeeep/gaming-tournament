from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# Schema for creating a user (what the client sends)
class UserCreate(BaseModel):
    password: str
    email: EmailStr
    display_name: str

#Schema for upadting a user
class UserUpdate(BaseModel):
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

#Schema for returning a user (what the server sends back)
class UserResponse(BaseModel):
    id: int
    display_name: str
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True

class UserPrivateResponse(UserResponse):
    email: EmailStr
