from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.api.deps import check_role, get_current_user
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import EmployeeService

router = APIRouter()

# HR managers and admins can create employees
@router.post("/", response_model=EmployeeResponse, dependencies=[Depends(check_role(["admin", "hr_manager"]))])
async def create_employee(
    employee_in: EmployeeCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Add a new employee record. Scoped to the active tenant.
    """
    employee = await EmployeeService.create_employee(db, employee_in)
    return employee

# HR managers, admins, and standard employees can list/read employees
@router.get("/", response_model=List[EmployeeResponse])
async def get_employees(
    skip: int = 0,
    limit: int = 100,
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve all employees. Scoped to the active tenant.
    """
    employees = await EmployeeService.get_employees(db, skip=skip, limit=limit)
    return employees

@router.get("/{employee_code}", response_model=EmployeeResponse)
async def get_employee_by_code(
    employee_code: str,
    current_user = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Retrieve a specific employee details by code.
    """
    employee = await EmployeeService.get_employee_by_code(db, employee_code)
    return employee

@router.put("/{employee_code}", response_model=EmployeeResponse, dependencies=[Depends(check_role(["admin", "hr_manager"]))])
async def update_employee(
    employee_code: str,
    employee_in: EmployeeUpdate,
    db: AsyncSession = Depends(get_db)
):
    """
    Update employee records. Restrained to HR Managers and Admins.
    """
    employee = await EmployeeService.update_employee(db, employee_code, employee_in)
    return employee
