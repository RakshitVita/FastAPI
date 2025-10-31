from typing import Annotated
from fastapi import APIRouter, Depends
from app.core.auth import get_current_active_user
from app.schemas.user import UserResponse

router = APIRouter(prefix="/api/user", tags=["User"])

@router.get("/profile", response_model=UserResponse)
async def get_profile(
    current_user: Annotated[UserResponse, Depends(get_current_active_user)]
):
    return current_user

@router.post("/applications")
async def submit_application(
    current_user: Annotated[UserResponse, Depends(get_current_active_user)]
):
    return {"message": "Application submitted"}

@router.get("/jobs")
async def get_available_jobs():
    # Public endpoint - no authentication required
    return {"message": "List of available jobs", "jobs": []}
