from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr
    role: str  # "ADMIN", "HR", "USER"

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_disabled: bool

    class Config:
        from_attributes = True

class UserInDB(UserBase):
    id: int
    hashed_password: str
    is_disabled: bool = False
