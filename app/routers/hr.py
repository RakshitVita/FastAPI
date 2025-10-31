from typing import Annotated
from fastapi import APIRouter, Depends
from app.core.auth import RoleChecker

router = APIRouter(prefix="/api/hr", tags=["HR"])

# ADMIN and HR can access
allow_hr = RoleChecker(allowed_roles=["ADMIN", "HR"])

@router.post("/jobs", dependencies=[Depends(allow_hr)])
async def create_job_posting():
    return {"message": "Job posting created"}

@router.get("/applications", dependencies=[Depends(allow_hr)])
async def view_applications():
    return {"message": "List of applications", "applications": []}

@router.put("/applications/{app_id}/status", dependencies=[Depends(allow_hr)])
async def update_application_status(app_id: int, status: str):
    return {"message": f"Application {app_id} status updated to {status}"}
