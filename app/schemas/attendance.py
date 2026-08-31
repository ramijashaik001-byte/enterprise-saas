from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class AttendanceBase(BaseModel):
    employee_code: str = Field(..., examples=['EMP001'])
    clock_in: datetime = Field(..., examples=['2026-08-31T09:00:00'])
    clock_out: Optional[datetime] = Field(None, examples=['2026-08-31T17:00:00'])
    status: str = Field('present', examples=['present', 'absent', 'late'])
    work_hours: float = Field(0.0, examples=[8.0])
    notes: Optional[str] = Field(None, examples=['Remote work'])
    ip_address: Optional[str] = Field(None, examples=['192.168.1.1'])

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceUpdate(BaseModel):
    employee_code: Optional[str] = None
    clock_in: Optional[datetime] = None
    clock_out: Optional[Optional[datetime]] = None
    status: Optional[str] = None
    work_hours: Optional[float] = None
    notes: Optional[Optional[str]] = None
    ip_address: Optional[Optional[str]] = None

class AttendanceResponse(AttendanceBase):
    id: int
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class AttendancePolicyConfig_1(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_1"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_1(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_2(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_2"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_2(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_3(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_3"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_3(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_4(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_4"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_4(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_5(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_5"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_5(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_6(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_6"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_6(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_7(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_7"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_7(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_8(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_8"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_8(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_9(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_9"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_9(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class AttendancePolicyConfig_10(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_10"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_10(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


# Schema additions for localized timezone attendance handling
