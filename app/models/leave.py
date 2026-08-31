from sqlalchemy import Column, String, Date, Float, ForeignKey
from app.models.base import TenantBase

class LeaveRequest(TenantBase):
    """
    Leave requests filed by employees.
    """
    __tablename__ = "leave_requests"
    
    employee_code = Column(String, nullable=False, index=True)
    leave_type = Column(String, nullable=False) # sick, annual, unpaid, parental
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    days_count = Column(Float, nullable=False)
    reason = Column(String, nullable=True)
    status = Column(String, default="pending") # pending, approved, rejected
    approved_by = Column(String, nullable=True) # employee_code of approver
