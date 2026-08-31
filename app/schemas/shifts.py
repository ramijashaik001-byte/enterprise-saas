from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date, datetime

class ShiftScheduleBase(BaseModel):
    employee_code: str = Field(..., examples=['EMP001'])
    shift_date: date = Field(..., examples=['2026-08-31'])
    start_time: str = Field(..., examples=['08:00'])
    end_time: str = Field(..., examples=['16:00'])
    break_duration_minutes: int = Field(30, examples=[30])
    location: str = Field('HQ', examples=['HQ', 'Warehouse 1'])

class ShiftScheduleCreate(ShiftScheduleBase):
    pass

class ShiftScheduleUpdate(BaseModel):
    employee_code: Optional[str] = None
    shift_date: Optional[date] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    break_duration_minutes: Optional[int] = None
    location: Optional[str] = None

class ShiftScheduleResponse(ShiftScheduleBase):
    id: int
    tenant_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True

class ShiftSchedulePolicyConfig_1(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_1"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_1(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_2(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_2"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_2(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_3(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_3"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_3(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_4(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_4"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_4(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_5(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_5"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_5(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_6(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_6"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_6(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_7(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_7"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_7(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_8(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_8"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_8(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_9(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_9"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_9(self) -> bool:
        return self.is_active and len(self.rule_name) > 0


class ShiftSchedulePolicyConfig_10(BaseModel):
    policy_id: int
    rule_name: str = Field(..., examples=["rule_10"])
    is_active: bool = True
    metadata_values: Optional[dict] = None
    
    def validate_rule_10(self) -> bool:
        return self.is_active and len(self.rule_name) > 0

