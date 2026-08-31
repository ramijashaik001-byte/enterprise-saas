from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TenantBaseSchema(BaseModel):
    name: str = Field(..., examples=["Acme Corp"])
    domain: Optional[str] = Field(None, examples=["acme.com"])
    subscription_plan: Optional[str] = Field("basic", examples=["basic", "premium", "enterprise"])

class TenantCreate(TenantBaseSchema):
    tenant_id: str = Field(..., examples=["acme"])

class TenantResponse(TenantBaseSchema):
    id: int
    tenant_id: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        # Pydantic v2 configuration
        orm_mode = True
