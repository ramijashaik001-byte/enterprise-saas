from fastapi import APIRouter
from app.api.v1 import auth, tenants, employees, leave, payroll
from app.api.v1 import attendance
from app.api.v1 import benefits
from app.api.v1 import expenses
from app.api.v1 import training
from app.api.v1 import onboarding
from app.api.v1 import audit_logs
from app.api.v1 import assets
from app.api.v1 import surveys
from app.api.v1 import documents
from app.api.v1 import compliance
from app.api.v1 import workforce
from app.api.v1 import shifts
from app.api.v1 import projects
from app.api.v1 import feedback
from app.api.v1 import requisitions

api_router = APIRouter()
api_router.include_router(tenants.router, prefix="/tenants", tags=["tenants"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(employees.router, prefix="/employees", tags=["employees"])
api_router.include_router(leave.router, prefix="/leaves", tags=["leaves"])
api_router.include_router(payroll.router, prefix="/payroll", tags=["payroll"])

# Scaled API Routers
api_router.include_router(attendance.router, prefix="/attendance", tags=["attendance"])
api_router.include_router(benefits.router, prefix="/benefits", tags=["benefits"])
api_router.include_router(expenses.router, prefix="/expenses", tags=["expenses"])
api_router.include_router(training.router, prefix="/training", tags=["training"])
api_router.include_router(onboarding.router, prefix="/onboarding", tags=["onboarding"])
api_router.include_router(audit_logs.router, prefix="/audit_logs", tags=["audit_logs"])
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])
api_router.include_router(surveys.router, prefix="/surveys", tags=["surveys"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(compliance.router, prefix="/compliance", tags=["compliance"])
api_router.include_router(workforce.router, prefix="/workforce", tags=["workforce"])
api_router.include_router(shifts.router, prefix="/shifts", tags=["shifts"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(feedback.router, prefix="/feedback", tags=["feedback"])
api_router.include_router(requisitions.router, prefix="/requisitions", tags=["requisitions"])
