from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr = Field(..., examples=["hr@acme.com"])
    role: Optional[str] = Field("employee", examples=["admin", "hr_manager", "employee"])

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, examples=["secretpassword"])

class UserResponse(UserBase):
    id: int
    tenant_id: str
    is_active: bool
    employee_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr = Field(..., examples=["hr@acme.com"])
    password: str = Field(..., examples=["secretpassword"])

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
    tenant_id: str

class TokenData(BaseModel):
    email: Optional[str] = None
