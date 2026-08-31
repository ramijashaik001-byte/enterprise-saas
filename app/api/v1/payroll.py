from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import check_role, get_current_user
from app.schemas.payroll import PaySlipCreate, PaySlipUpdate, PaySlipResponse
from app.services.payroll_service import PayrollService

router = APIRouter()

@router.post("/", response_model=PaySlipResponse, dependencies=[Depends(check_role(["admin", "hr_manager"]))])
async def generate_payslip(
    payslip_in: PaySlipCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Generate a new payslip for an employee. Restricted to admin/hr_manager.
    """
    payslip = await PayrollService.create_payslip(db, payslip_in)
    return payslip

@router.get("/", response_model=List[PaySlipResponse])
async def list_payslips(
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all payslips for the tenant.
    """
    payslips = await PayrollService.get_payslips(db)
    return payslips

@router.put("/{payslip_id}", response_model=PaySlipResponse, dependencies=[Depends(check_role(["admin", "hr_manager"]))])
async def update_payslip(
    payslip_id: int,
    update_in: PaySlipUpdate,
    db: AsyncSession = Depends(get_db)
):
    """
    Update a payslip's processing or payment status.
    """
    payslip = await PayrollService.update_payslip_status(db, payslip_id, update_in)
    return payslip
