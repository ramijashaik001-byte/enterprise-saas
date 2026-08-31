from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.core.tenancy import get_tenant_context
from fastapi import HTTPException, status

class EmployeeService:
    @staticmethod
    async def create_employee(db: AsyncSession, employee_in: EmployeeCreate) -> Employee:
        tenant_id = get_tenant_context()
        
        # Check if employee code already exists for this tenant
        query = select(Employee).where(
            (Employee.employee_code == employee_in.employee_code) & 
            (Employee.tenant_id == tenant_id)
        )
        result = await db.execute(query)
        if result.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Employee code {employee_in.employee_code} already exists for this tenant"
            )
            
        db_employee = Employee(
            tenant_id=tenant_id,
            employee_code=employee_in.employee_code,
            first_name=employee_in.first_name,
            last_name=employee_in.last_name,
            email=employee_in.email,
            phone=employee_in.phone,
            department=employee_in.department,
            job_title=employee_in.job_title,
            hire_date=employee_in.hire_date,
            base_salary=employee_in.base_salary,
            bank_account=employee_in.bank_account,
            manager_code=employee_in.manager_code
        )
        db.add(db_employee)
        await db.flush()
        return db_employee

    @staticmethod
    async def get_employees(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Employee]:
        tenant_id = get_tenant_context()
        query = select(Employee).where(Employee.tenant_id == tenant_id).offset(skip).limit(limit)
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def get_employee_by_code(db: AsyncSession, employee_code: str) -> Employee:
        tenant_id = get_tenant_context()
        query = select(Employee).where(
            (Employee.employee_code == employee_code) & 
            (Employee.tenant_id == tenant_id)
        )
        result = await db.execute(query)
        employee = result.scalar_one_or_none()
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with code {employee_code} not found"
            )
        return employee

    @staticmethod
    async def update_employee(db: AsyncSession, employee_code: str, employee_in: EmployeeUpdate) -> Employee:
        employee = await EmployeeService.get_employee_by_code(db, employee_code)
        
        update_data = employee_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(employee, field, value)
            
        db.add(employee)
        await db.flush()
        return employee
