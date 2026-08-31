from sqlalchemy import Column, String, Date, Float, ForeignKey
from app.models.base import TenantBase

class Employee(TenantBase):
    """
    Employee model representing core personal and professional records.
    """
    __tablename__ = "employees"
    
    employee_code = Column(String, unique=True, index=True, nullable=False) # e.g. EMP001
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    department = Column(String, index=True, nullable=False)
    job_title = Column(String, nullable=False)
    hire_date = Column(Date, nullable=False)
    status = Column(String, default="active") # active, inactive, terminated, suspended
    
    # Financial fields
    base_salary = Column(Float, default=0.0)
    bank_account = Column(String, nullable=True)
    
    # Hierarchy
    manager_code = Column(String, nullable=True)
