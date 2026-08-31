from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.models.payroll import PaySlip
from app.schemas.payroll import PaySlipCreate, PaySlipUpdate
from app.core.tenancy import get_tenant_context
from fastapi import HTTPException, status

class PayrollService:
    @staticmethod
    async def create_payslip(db: AsyncSession, payslip_in: PaySlipCreate) -> PaySlip:
        tenant_id = get_tenant_context()
        
        # Calculate net pay
        net_pay = payslip_in.base_salary + payslip_in.allowances - payslip_in.deductions
        
        db_payslip = PaySlip(
            tenant_id=tenant_id,
            employee_code=payslip_in.employee_code,
            period_start=payslip_in.period_start,
            period_end=payslip_in.period_end,
            base_salary=payslip_in.base_salary,
            allowances=payslip_in.allowances,
            deductions=payslip_in.deductions,
            net_pay=net_pay,
            status="draft"
        )
        db.add(db_payslip)
        await db.flush()
        return db_payslip

    @staticmethod
    async def get_payslips(db: AsyncSession) -> List[PaySlip]:
        tenant_id = get_tenant_context()
        query = select(PaySlip).where(PaySlip.tenant_id == tenant_id)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def update_payslip_status(db: AsyncSession, payslip_id: int, update_in: PaySlipUpdate) -> PaySlip:
        tenant_id = get_tenant_context()
        query = select(PaySlip).where(
            (PaySlip.id == payslip_id) & 
            (PaySlip.tenant_id == tenant_id)
        )
        result = await db.execute(query)
        payslip = result.scalar_one_or_none()
        if not payslip:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Pay slip not found"
            )
            
        payslip.status = update_in.status
        if update_in.payment_date:
            payslip.payment_date = update_in.payment_date
            
        db.add(payslip)
        await db.flush()
        return payslip
