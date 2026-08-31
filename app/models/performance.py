from sqlalchemy import Column, String, Float, Integer
from app.models.base import TenantBase

class PerformanceGoal(TenantBase):
    """
    Performance Goals or OKRs assigned to employees.
    """
    __tablename__ = "performance_goals"
    
    employee_code = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    target_date = Column(String, nullable=True) # e.g. "Q3 2026" or date string
    weight = Column(Float, default=1.0) # weight in overall score
    progress = Column(Float, default=0.0) # 0 to 100 percentage
    status = Column(String, default="not_started") # not_started, in_progress, achieved, deferred
    reviewer_code = Column(String, nullable=True)
