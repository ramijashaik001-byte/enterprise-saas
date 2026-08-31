from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.core.database import get_db
from app.core.security import verify_password, get_password_hash, create_access_token
from app.core.tenancy import tenant_dependency, get_tenant_context
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.tenant_service import TenantService

router = APIRouter()

@router.post("/register-admin", response_model=UserResponse)
async def register_tenant_admin(
    user_in: UserCreate,
    tenant_id: str = Depends(tenant_dependency),
    db: AsyncSession = Depends(get_db)
):
    """
    Bootstrap the first admin user for a tenant.
    Requires the X-Tenant-ID header to identify the tenant.
    """
    # Verify the tenant exists first
    await TenantService.get_tenant_by_id(db, tenant_id)
    
    # Check if any admin exists for this tenant
    query = select(User).where(
        (User.tenant_id == tenant_id) & 
        (User.role == "admin")
    )
    result = await db.execute(query)
    if result.scalars().first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Admin user already registered for this tenant"
        )
        
    db_user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
        role="admin",
        tenant_id=tenant_id
    )
    db.add(db_user)
    await db.flush()
    return db_user

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    tenant_id: str = Depends(tenant_dependency),
    db: AsyncSession = Depends(get_db)
):
    """
    Authenticate a tenant user and return an access token.
    Requires X-Tenant-ID header.
    """
    query = select(User).where(
        (User.email == form_data.username) & 
        (User.tenant_id == tenant_id)
    )
    result = await db.execute(query)
    user = result.scalar_one_or_none()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
        
    access_token = create_access_token(subject=user.email)
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user.role,
        "tenant_id": user.tenant_id
    }
