from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import check_role, get_current_user
from app.schemas.leave import LeaveRequestCreate, LeaveRequestUpdate, LeaveRequestResponse
from app.services.leave_service import LeaveService

router = APIRouter()

@router.post("/", response_model=LeaveRequestResponse)
async def create_leave_request(
    leave_in: LeaveRequestCreate,
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    File a new leave request.
    """
    # In a real scenario, check that current_user has employee permissions for employee_code
    leave = await LeaveService.create_leave_request(db, leave_in)
    return leave

@router.get("/", response_model=List[LeaveRequestResponse])
async def list_leave_requests(
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Get all leave requests.
    """
    leaves = await LeaveService.get_leave_requests(db)
    return leaves

@router.put("/{leave_id}", response_model=LeaveRequestResponse, dependencies=[Depends(check_role(["admin", "hr_manager"]))])
async def approve_or_reject_leave(
    leave_id: int,
    status_in: LeaveRequestUpdate,
    db: AsyncSession = Depends(get_db)
):
    """
    Approve or reject a leave request. Restricted to HR Managers and Admins.
    """
    leave = await LeaveService.update_leave_status(db, leave_id, status_in)
    return leave
