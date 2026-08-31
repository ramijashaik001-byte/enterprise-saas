from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime

class PaySlipBase(BaseModel):
    employee_code: str = Field(..., examples=["EMP002"])
    period_start: date = Field(..., examples=["2026-08-01"])
    period_end: date = Field(..., examples=["2026-08-31"])
    base_salary: float = Field(..., examples=[5000.0])
    allowances: Optional[float] = Field(0.0, examples=[500.0])
    deductions: Optional[float] = Field(0.0, examples=[200.0])

class PaySlipCreate(PaySlipBase):
    pass

class PaySlipUpdate(BaseModel):
    status: str = Field(..., examples=["processed", "paid", "cancelled"])
    payment_date: Optional[date] = None

class PaySlipResponse(PaySlipBase):
    id: int
    tenant_id: str
    net_pay: float
    status: str
    payment_date: Optional[date] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True
