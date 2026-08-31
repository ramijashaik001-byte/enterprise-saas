# Import all models to ensure they are registered with Base metadata
from app.core.database import Base
from app.models.tenant import Tenant
from app.models.user import User
from app.models.employee import Employee
from app.models.leave import LeaveRequest
from app.models.payroll import PaySlip
from app.models.performance import PerformanceGoal
from app.models.recruitment import JobOpening, Applicant

__all__ = [
    "Base",
    "Tenant",
    "User",
    "Employee",
    "LeaveRequest",
    "PaySlip",
    "PerformanceGoal",
    "JobOpening",
    "Applicant"
]

# Scaled Module Models
from app.models.attendance import Attendance
from app.models.benefits import BenefitPlan
from app.models.expenses import ExpenseClaim
from app.models.training import TrainingCourse
from app.models.onboarding import OnboardingTask
from app.models.audit_logs import AuditLog
from app.models.assets import Asset
from app.models.surveys import Survey
from app.models.documents import Document
from app.models.compliance import ComplianceCheck
from app.models.workforce import WorkforceBudget
from app.models.shifts import ShiftSchedule
from app.models.projects import ProjectAllocation
from app.models.feedback import PeerFeedback
from app.models.requisitions import Requisition

__all__.extend([
    "Attendance",
    "BenefitPlan",
    "ExpenseClaim",
    "TrainingCourse",
    "OnboardingTask",
    "AuditLog",
    "Asset",
    "Survey",
    "Document",
    "ComplianceCheck",
    "WorkforceBudget",
    "ShiftSchedule",
    "ProjectAllocation",
    "PeerFeedback",
    "Requisition"
])
