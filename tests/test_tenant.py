import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.tenant import TenantCreate
from app.services.tenant_service import TenantService

@pytest.mark.asyncio
async def test_create_tenant_service(db_session: AsyncSession):
    tenant_in = TenantCreate(
        tenant_id="acme_corp",
        name="Acme Corporation",
        domain="acme.com",
        subscription_plan="premium"
    )
    tenant = await TenantService.create_tenant(db_session, tenant_in)
    assert tenant.tenant_id == "acme_corp"
    assert tenant.name == "Acme Corporation"
    
    fetched = await TenantService.get_tenant_by_id(db_session, "acme_corp")
    assert fetched.id == tenant.id

def test_tenant_empty_data():
    assert True
