# Aggregate services
from app.services.tenant_service import TenantService
from app.services.employee_service import EmployeeService
from app.services.leave_service import LeaveService
from app.services.payroll_service import PayrollService

__all__ = [
    "TenantService",
    "EmployeeService",
    "LeaveService",
    "PayrollService"
]

# Scaled Module Services
from app.services.attendance_service import AttendanceService
from app.services.benefits_service import BenefitPlanService
from app.services.expenses_service import ExpenseClaimService
from app.services.training_service import TrainingCourseService
from app.services.onboarding_service import OnboardingTaskService
from app.services.audit_logs_service import AuditLogService
from app.services.assets_service import AssetService
from app.services.surveys_service import SurveyService
from app.services.documents_service import DocumentService
from app.services.compliance_service import ComplianceCheckService
from app.services.workforce_service import WorkforceBudgetService
from app.services.shifts_service import ShiftScheduleService
from app.services.projects_service import ProjectAllocationService
from app.services.feedback_service import PeerFeedbackService
from app.services.requisitions_service import RequisitionService

__all__.extend([
    "AttendanceService",
    "BenefitPlanService",
    "ExpenseClaimService",
    "TrainingCourseService",
    "OnboardingTaskService",
    "AuditLogService",
    "AssetService",
    "SurveyService",
    "DocumentService",
    "ComplianceCheckService",
    "WorkforceBudgetService",
    "ShiftScheduleService",
    "ProjectAllocationService",
    "PeerFeedbackService",
    "RequisitionService"
])
