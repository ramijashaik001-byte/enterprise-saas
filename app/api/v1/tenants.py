from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.tenant import TenantCreate, TenantResponse
from app.services.tenant_service import TenantService

router = APIRouter()

@router.post("/register", response_model=TenantResponse)
async def register_tenant(
    tenant_in: TenantCreate,
    db: AsyncSession = Depends(get_db)
):
    """
    Onboard a new tenant to the SaaS application.
    """
    tenant = await TenantService.create_tenant(db, tenant_in)
    return tenant
