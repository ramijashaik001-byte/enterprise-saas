from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class ComplianceCheckBase(BaseModel):
    title: str = Field(..., examples=['GDPR Compliance Review'])
    description: Optional[str] = Field(None, examples=['Review company data access control logs'])
    governing_body: Optional[str] = Field(None, examples=['EU Data Protection Board'])
    last_checked: Optional[date] = Field(None, examples=['2026-06-30'])
    next_due: date = Field(..., examples=['2026-12-31'])
    status: str = Field('compliant', examples=['compliant', 'warning', 'non_compliant'])
    assigned_officer: Optional[str] = Field(None, examples=['EMP002'])

class ComplianceCheckCreate(ComplianceCheckBase):
    pass

class ComplianceCheckUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[Optional[str]] = None
    governing_body: Optional[Optional[str]] = None
    last_checked: Optional[Optional[date]] = None
    next_due: Optional[date] = None
    status: Optional[str] = None
    assigned_officer: Optional[Optional[str]] = None

class ComplianceCheckResponse(ComplianceCheckBase):
    id: int
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class ComplianceCheckPolicyConfig_1(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_1"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_1(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_2(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_2"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_2(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_3(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_3"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_3(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_4(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_4"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_4(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_5(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_5"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_5(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_6(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_6"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_6(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_7(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_7"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_7(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_8(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_8"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_8(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_9(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_9"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_9(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ComplianceCheckPolicyConfig_10(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_10"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_10(self) -> bool:
        return self.is_active and len(self.rule_name) > 0

