from typing import Any, List, Optional

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr
from src import schemas
from src.db import crud
from src.utils import user_auth
from src.utils.config import settings

router = APIRouter()


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    password: str = Body(...),
    email: EmailStr = Body(...),
    username: Optional[str] = Body(...),
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
            detail="The user with this email already exists in the system",
        )
    user = crud.user.get_by_username(username=username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(
        password=password, email=email, full_name=full_name, username=username
    )
    return crud.user.create(obj=user_in)


@router.get("/me", response_model=List[schemas.User])
def read_user_me(
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
) -> Any:
    """
    Retrieve user.
    """
    return [current_user]


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    password: str = Body(None),
    username: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
) -> Any:
    """
    Update own user.
    """
    user_in = schemas.UserUpdate(**current_user)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    if username is not None:
        user_in.username = username
    return crud.user.update(db_obj=current_user, obj_in=user_in)


@router.delete("/me", response_model=schemas.User)
def delete_user_me(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
) -> Any:
    """
    Update own user.
    """
    ret = crud.user.delete({"id": current_user["id"]})
    if ret:
        return current_user
    else:
        raise HTTPException(
            status_code=400,
            detail="Could not delete user",
        )
