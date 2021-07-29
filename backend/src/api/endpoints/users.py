from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from pydantic import EmailStr
from src import schemas
from src.db import crud
from src.utils.config import settings

router = APIRouter()


@router.post("/open")
def create_user_open(
    *,
    password: str = Body(...),
    email: EmailStr = Body(...),
    full_name: str = Body(None),
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password, email=email, full_name=full_name)
    user = crud.user.create(obj=user_in)
    return user
