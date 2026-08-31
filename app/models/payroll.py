from sqlalchemy import Column, String, Date, Float
from app.models.base import TenantBase

class PaySlip(TenantBase):
    """
    Pay slips generated per employee for payroll cycles.
    """
    __tablename__ = "pay_slips"
    
    employee_code = Column(String, nullable=False, index=True)
    period_start = Column(Date, nullable=False)
    period_end = Column(Date, nullable=False)
    base_salary = Column(Float, nullable=False)
    allowances = Column(Float, default=0.0)
    deductions = Column(Float, default=0.0)
    net_pay = Column(Float, nullable=False)
    status = Column(String, default="draft") # draft, processed, paid, cancelled
    payment_date = Column(Date, nullable=True)
