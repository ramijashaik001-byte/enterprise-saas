from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.core.database import Base

class Tenant(Base):
    """
    SaaS Tenant Registry. Stores metadata for each tenant organization.
    """
    __tablename__ = "tenants"
    
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    schema_name = Column(String, unique=True, nullable=True) # for schema-based systems if needed
    domain = Column(String, unique=True, nullable=True)
    is_active = Column(Boolean, default=True)
    subscription_plan = Column(String, default="basic") # basic, premium, enterprise
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
