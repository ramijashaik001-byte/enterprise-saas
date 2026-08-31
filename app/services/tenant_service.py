from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.tenant import Tenant
from app.models.user import User
from app.schemas.tenant import TenantCreate
from app.schemas.user import UserCreate
from app.core.security import get_password_hash
from fastapi import HTTPException, status

class TenantService:
    @staticmethod
    async def create_tenant(db: AsyncSession, tenant_in: TenantCreate) -> Tenant:
        # Check if tenant_id is already taken
        query = select(Tenant).where(Tenant.tenant_id == tenant_in.tenant_id)
        result = await db.execute(query)
        if result.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tenant identifier already registered"
            )
        
        db_tenant = Tenant(
            tenant_id=tenant_in.tenant_id,
            name=tenant_in.name,
            domain=tenant_in.domain,
            subscription_plan=tenant_in.subscription_plan
        )
        db.add(db_tenant)
        await db.flush()
        return db_tenant

    @staticmethod
    async def get_tenant_by_id(db: AsyncSession, tenant_id: str) -> Tenant:
        query = select(Tenant).where(Tenant.tenant_id == tenant_id)
        result = await db.execute(query)
        tenant = result.scalar_one_or_none()
        if not tenant:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Tenant not found"
            )
        return tenant
