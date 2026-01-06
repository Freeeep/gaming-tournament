from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Base Schema with shared files
class UserBase(BaseModel):
    email: EmailStr
    display_name: str

# Schema for creating a user (what the client sends)
class UserCreate(UserBase):
    password: str

#Schema for upadting a user
class UserUpdate(BaseModel):
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None

#Schema for returning a user (what the server sends back)
class UserResponse(UserBase):
    id: int
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
