from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date, datetime

class EmployeeBase(BaseModel):
    first_name: str = Field(..., examples=["John"])
    last_name: str = Field(..., examples=["Doe"])
    email: EmailStr = Field(..., examples=["john.doe@acme.com"])
    phone: Optional[str] = Field(None, examples=["+1234567890"])
    department: str = Field(..., examples=["Engineering"])
    job_title: str = Field(..., examples=["Software Engineer"])
    hire_date: date = Field(..., examples=["2025-01-15"])
    base_salary: Optional[float] = Field(0.0, examples=[85000.0])
    bank_account: Optional[str] = Field(None, examples=["US1234567890"])
    manager_code: Optional[str] = Field(None, examples=["EMP001"])

class EmployeeCreate(EmployeeBase):
    employee_code: str = Field(..., examples=["EMP002"])

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    department: Optional[str] = None
    job_title: Optional[str] = None
    status: Optional[str] = None
    base_salary: Optional[float] = None
    bank_account: Optional[str] = None
    manager_code: Optional[str] = None

class EmployeeResponse(EmployeeBase):
    id: int
    tenant_id: str
    employee_code: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True
