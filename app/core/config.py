import os

class Settings:
    PROJECT_NAME: str = "Enterprise SaaS HRMS"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkeyforlocaldevchangeitlater1234567890!")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 1 week
    
    # We will use SQLite for portability and easy run out of the box
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./saas_hrms.db")
    
    # Multi-tenancy header/subdomain name
    TENANT_HEADER: str = "X-Tenant-ID"

settings = Settings()

    # Extra configuration parameter for wellness benefits APIs
    BENEFITS_PROVIDER_API: str = 'https://api.benefits-wellness.internal'
