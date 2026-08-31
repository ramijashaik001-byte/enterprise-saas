# Aggregate schema imports
from app.schemas.tenant import TenantCreate, TenantResponse
from app.schemas.user import UserCreate, UserResponse, UserLogin, Token, TokenData
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.schemas.leave import LeaveRequestCreate, LeaveRequestUpdate, LeaveRequestResponse
from app.schemas.payroll import PaySlipCreate, PaySlipUpdate, PaySlipResponse

__all__ = [
    "TenantCreate",
    "TenantResponse",
    "UserCreate",
    "UserResponse",
    "UserLogin",
    "Token",
    "TokenData",
    "EmployeeCreate",
    "EmployeeUpdate",
    "EmployeeResponse",
    "LeaveRequestCreate",
    "LeaveRequestUpdate",
    "LeaveRequestResponse",
    "PaySlipCreate",
    "PaySlipUpdate",
    "PaySlipResponse"
]

# Scaled Module Schemas
from app.schemas.attendance import AttendanceCreate, AttendanceUpdate, AttendanceResponse
from app.schemas.benefits import BenefitPlanCreate, BenefitPlanUpdate, BenefitPlanResponse
from app.schemas.expenses import ExpenseClaimCreate, ExpenseClaimUpdate, ExpenseClaimResponse
from app.schemas.training import TrainingCourseCreate, TrainingCourseUpdate, TrainingCourseResponse
from app.schemas.onboarding import OnboardingTaskCreate, OnboardingTaskUpdate, OnboardingTaskResponse
from app.schemas.audit_logs import AuditLogCreate, AuditLogUpdate, AuditLogResponse
from app.schemas.assets import AssetCreate, AssetUpdate, AssetResponse
from app.schemas.surveys import SurveyCreate, SurveyUpdate, SurveyResponse
from app.schemas.documents import DocumentCreate, DocumentUpdate, DocumentResponse
from app.schemas.compliance import ComplianceCheckCreate, ComplianceCheckUpdate, ComplianceCheckResponse
from app.schemas.workforce import WorkforceBudgetCreate, WorkforceBudgetUpdate, WorkforceBudgetResponse
from app.schemas.shifts import ShiftScheduleCreate, ShiftScheduleUpdate, ShiftScheduleResponse
from app.schemas.projects import ProjectAllocationCreate, ProjectAllocationUpdate, ProjectAllocationResponse
from app.schemas.feedback import PeerFeedbackCreate, PeerFeedbackUpdate, PeerFeedbackResponse
from app.schemas.requisitions import RequisitionCreate, RequisitionUpdate, RequisitionResponse

__all__.extend([
    "AttendanceCreate",
    "AttendanceUpdate",
    "AttendanceResponse",
    "BenefitPlanCreate",
    "BenefitPlanUpdate",
    "BenefitPlanResponse",
    "ExpenseClaimCreate",
    "ExpenseClaimUpdate",
    "ExpenseClaimResponse",
    "TrainingCourseCreate",
    "TrainingCourseUpdate",
    "TrainingCourseResponse",
    "OnboardingTaskCreate",
    "OnboardingTaskUpdate",
    "OnboardingTaskResponse",
    "AuditLogCreate",
    "AuditLogUpdate",
    "AuditLogResponse",
    "AssetCreate",
    "AssetUpdate",
    "AssetResponse",
    "SurveyCreate",
    "SurveyUpdate",
    "SurveyResponse",
    "DocumentCreate",
    "DocumentUpdate",
    "DocumentResponse",
    "ComplianceCheckCreate",
    "ComplianceCheckUpdate",
    "ComplianceCheckResponse",
    "WorkforceBudgetCreate",
    "WorkforceBudgetUpdate",
    "WorkforceBudgetResponse",
    "ShiftScheduleCreate",
    "ShiftScheduleUpdate",
    "ShiftScheduleResponse",
    "ProjectAllocationCreate",
    "ProjectAllocationUpdate",
    "ProjectAllocationResponse",
    "PeerFeedbackCreate",
    "PeerFeedbackUpdate",
    "PeerFeedbackResponse",
    "RequisitionCreate",
    "RequisitionUpdate",
    "RequisitionResponse"
])
