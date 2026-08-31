from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.models.leave import LeaveRequest
from app.schemas.leave import LeaveRequestCreate, LeaveRequestUpdate
from app.core.tenancy import get_tenant_context
from fastapi import HTTPException, status

class LeaveService:
    @staticmethod
    async def create_leave_request(db: AsyncSession, leave_in: LeaveRequestCreate) -> LeaveRequest:
        tenant_id = get_tenant_context()
        
        db_leave = LeaveRequest(
            tenant_id=tenant_id,
            employee_code=leave_in.employee_code,
            leave_type=leave_in.leave_type,
            start_date=leave_in.start_date,
            end_date=leave_in.end_date,
            days_count=leave_in.days_count,
            reason=leave_in.reason,
            status="pending"
        )
        db.add(db_leave)
        await db.flush()
        return db_leave

    @staticmethod
    async def get_leave_requests(db: AsyncSession) -> List[LeaveRequest]:
        tenant_id = get_tenant_context()
        query = select(LeaveRequest).where(LeaveRequest.tenant_id == tenant_id)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def update_leave_status(db: AsyncSession, leave_id: int, status_in: LeaveRequestUpdate) -> LeaveRequest:
        tenant_id = get_tenant_context()
        query = select(LeaveRequest).where(
            (LeaveRequest.id == leave_id) & 
            (LeaveRequest.tenant_id == tenant_id)
        )
        result = await db.execute(query)
        leave = result.scalar_one_or_none()
        if not leave:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Leave request not found"
            )
            
        leave.status = status_in.status
        leave.approved_by = status_in.approved_by
        db.add(leave)
        await db.flush()
        return leave
