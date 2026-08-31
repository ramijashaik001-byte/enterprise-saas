from sqlalchemy import Column, String, Boolean
from app.models.base import TenantBase

class User(TenantBase):
    """
    User model representing individuals who can authenticate.
    Associated with a specific tenant.
    """
    __tablename__ = "users"
    
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(String, default="employee") # admin, hr_manager, employee
    
    # Optional field linking to full employee record
    employee_id = Column(String, nullable=True) 
