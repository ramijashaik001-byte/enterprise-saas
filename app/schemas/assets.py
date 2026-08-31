from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class AssetBase(BaseModel):
    name: str = Field(..., examples=['MacBook Pro 16'])
    serial_number: str = Field(..., examples=['C02GG5Z1MD6M'])
    category: str = Field(..., examples=['laptop'])
    assigned_to: Optional[str] = Field(None, examples=['EMP001'])
    assignment_date: Optional[date] = Field(None, examples=['2026-01-10'])
    status: str = Field('available', examples=['available', 'assigned', 'damaged'])
    cost: float = Field(0.0, examples=[2499.00])

class AssetCreate(AssetBase):
    pass

class AssetUpdate(BaseModel):
    name: Optional[str] = None
    serial_number: Optional[str] = None
    category: Optional[str] = None
    assigned_to: Optional[Optional[str]] = None
    assignment_date: Optional[Optional[date]] = None
    status: Optional[str] = None
    cost: Optional[float] = None

class AssetResponse(AssetBase):
    id: int
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class AssetPolicyConfig_1(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_1"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_1(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_2(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_2"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_2(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_3(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_3"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_3(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_4(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_4"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_4(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_5(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_5"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_5(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_6(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_6"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_6(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_7(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_7"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_7(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_8(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_8"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_8(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_9(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_9"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_9(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AssetPolicyConfig_10(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_10"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_10(self) -> bool:
        return self.is_active and len(self.rule_name) > 0

