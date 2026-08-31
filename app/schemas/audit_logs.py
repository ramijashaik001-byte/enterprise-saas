from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class AuditLogBase(BaseModel):
    user_email: str = Field(..., examples=['admin@acme.com'])
    action: str = Field(..., examples=['UPDATE'])
    entity: str = Field(..., examples=['Employee'])
    entity_id: Optional[str] = Field(None, examples=['EMP001'])
    details: Optional[str] = Field(None, examples=['Changed salary from 80k to 90k'])
    ip_address: Optional[str] = Field(None, examples=['127.0.0.1'])
    timestamp: datetime = Field(..., examples=['2026-08-31T11:00:00'])

class AuditLogCreate(AuditLogBase):
    pass

class AuditLogUpdate(BaseModel):
    user_email: Optional[str] = None
    action: Optional[str] = None
    entity: Optional[str] = None
    entity_id: Optional[Optional[str]] = None
    details: Optional[Optional[str]] = None
    ip_address: Optional[Optional[str]] = None
    timestamp: Optional[datetime] = None

class AuditLogResponse(AuditLogBase):
    id: int
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class AuditLogPolicyConfig_1(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_1"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_1(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_2(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_2"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_2(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_3(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_3"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_3(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_4(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_4"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_4(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_5(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_5"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_5(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_6(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_6"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_6(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_7(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_7"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_7(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_8(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_8"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_8(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_9(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_9"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_9(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AuditLogPolicyConfig_10(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_10"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_10(self) -> bool:
        return self.is_active and len(self.rule_name) > 0

