from contextvars import ContextVar
from fastapi import Request, HTTPException, status
from app.core.config import settings

# Thread/coroutine-safe context variable to store tenant identifier
_tenant_context: ContextVar[str] = ContextVar("tenant_id", default="")

def set_tenant_context(tenant_id: str) -> None:
    _tenant_context.set(tenant_id)

def get_tenant_context() -> str:
    return _tenant_context.get()

async def tenant_dependency(request: Request) -> str:
    """
    Dependency to retrieve the tenant ID from request headers.
    In production, this could also be retrieved from the subdomain (e.g. tenant.domain.com).
    """
    tenant_id = request.headers.get(settings.TENANT_HEADER)
    
    # Allow some endpoints to pass without tenant (like system-wide admin or registering a new tenant)
    # But for standard tenant operations, we enforce this.
    if not tenant_id:
        # Check query parameters as fallback
        tenant_id = request.query_params.get("tenant_id")
        
    if not tenant_id:
        # We can also check if the path is an open path like tenant signup
        path = request.url.path
        if path.startswith("/api/v1/auth") or path.startswith("/api/v1/tenants/register"):
            return ""
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Missing tenant header: {settings.TENANT_HEADER}"
        )
        
    set_tenant_context(tenant_id)
    return tenant_id
