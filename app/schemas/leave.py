from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class LeaveRequestBase(BaseModel):
    leave_type: str = Field(..., examples=["annual", "sick", "unpaid"])
    start_date: date = Field(..., examples=["2026-09-01"])
    end_date: date = Field(..., examples=["2026-09-05"])
    days_count: float = Field(..., examples=[4.0])
    reason: Optional[str] = Field(None, examples=["Family vacation"])

class LeaveRequestCreate(LeaveRequestBase):
    employee_code: str = Field(..., examples=["EMP002"])

class LeaveRequestUpdate(BaseModel):
    status: str = Field(..., examples=["approved", "rejected"])
    approved_by: Optional[str] = Field(None, examples=["EMP001"])

class LeaveRequestResponse(LeaveRequestBase):
    id: int
    tenant_id: str
    employee_code: str
    status: str
    approved_by: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True
