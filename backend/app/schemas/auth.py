from pydantic import BaseModel, EmailStr

class AuthResponse(BaseModel):
    access_token: str
    token_type: str

class AuthLogin(BaseModel):
    email: EmailStr
    password: str