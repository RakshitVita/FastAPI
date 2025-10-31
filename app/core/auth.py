# app/core/auth.py

from typing import Annotated
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from app.core.config import settings
from app.core.security import oauth2_scheme
from app.schemas.user import UserInDB

# Temporary fake database - replace with real DB
from app.db.database import fake_users_db


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserInDB:
    """Dependency to get the current authenticated user"""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        role: str = payload.get("role")
        if email is None or role is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    # Replace with real database query
    user = fake_users_db.get(email)
    if user is None:
        raise credentials_exception
    
    return UserInDB(**user)


async def get_current_active_user(
    current_user: Annotated[UserInDB, Depends(get_current_user)]
) -> UserInDB:
    """Ensure the user is active"""
    if current_user.is_disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


class RoleChecker:
    """Dependency class for role-based access control"""
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles
    
    def __call__(self, user: Annotated[UserInDB, Depends(get_current_active_user)]) -> bool:
        if user.role in self.allowed_roles:
            return True
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have permission to access this resource"
        )
