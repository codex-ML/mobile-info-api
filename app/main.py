from fastapi import FastAPI, HTTPException
from .database import get_user_by_mobile
from .config import settings

app = FastAPI(
    title="User Lookup API",
    description="API for finding users by mobile number",
    version="1.0.0"
)

@app.get("/search", summary="Find users by mobile number")
async def search_users(mobile: str):
    """
    Search users by their mobile number
    
    - **mobile**: 10-digit mobile number to search (e.g., 9999998732)
    """
    users = get_user_by_mobile(mobile)
    if not users:
        raise HTTPException(
            status_code=404,
            detail=f"No users found for mobile: {mobile}"
        )
    return {"results": users}

@app.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "healthy", "database": settings.DB_NAME}
