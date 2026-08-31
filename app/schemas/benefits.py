from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class BenefitPlanBase(BaseModel):
    name: str = Field(..., examples=['Premium Health Plan'])
    type: str = Field(..., examples=['health'])
    provider: str = Field(..., examples=['Aetna'])
    description: Optional[str] = Field(None, examples=['Full medical coverage'])
    cost_sharing_percentage: float = Field(0.0, examples=[20.0])
    monthly_premium: float = Field(0.0, examples=[350.0])
    is_active: bool = Field(True, examples=[True])

class BenefitPlanCreate(BenefitPlanBase):
    pass

class BenefitPlanUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    provider: Optional[str] = None
    description: Optional[Optional[str]] = None
    cost_sharing_percentage: Optional[float] = None
    monthly_premium: Optional[float] = None
    is_active: Optional[bool] = None

class BenefitPlanResponse(BenefitPlanBase):
    id: int
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class BenefitPlanPolicyConfig_1(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_1"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_1(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_2(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_2"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_2(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_3(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_3"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_3(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_4(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_4"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_4(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_5(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_5"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_5(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_6(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_6"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_6(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_7(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_7"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_7(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_8(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_8"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_8(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_9(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_9"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_9(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class BenefitPlanPolicyConfig_10(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_10"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_10(self) -> bool:
        return self.is_active and len(self.rule_name) > 0

