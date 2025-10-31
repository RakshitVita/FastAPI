from typing import Annotated
from fastapi import APIRouter, Depends
from app.core.auth import RoleChecker, get_current_active_user
from app.schemas.user import UserResponse

router = APIRouter(prefix="/api/admin", tags=["Admin"])

# Only ADMIN can access
allow_admin = RoleChecker(allowed_roles=["ADMIN"])

@router.get("/users", dependencies=[Depends(allow_admin)])
async def get_all_users():
    return {"message": "List of all users", "users": []}

@router.post("/users", dependencies=[Depends(allow_admin)])
async def create_user():
    return {"message": "User created by admin"}

@router.delete("/users/{user_id}", dependencies=[Depends(allow_admin)])
async def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}
