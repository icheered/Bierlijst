from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = True
    is_verified: Optional[bool] = True
    is_premium: Optional[bool] = False
    username: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    username: Optional[str]


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


# Additional properties stored in DB
class UserInDBBase(UserBase):
    id: Optional[str] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    # Create user for consistency in OpenAPI
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
