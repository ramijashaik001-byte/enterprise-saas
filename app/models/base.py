from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base

class TenantBase(Base):
    """
    Abstract base class for multi-tenant models.
    Automatically includes a tenant_id column.
    """
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
