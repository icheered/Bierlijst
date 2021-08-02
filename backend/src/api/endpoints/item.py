from typing import Optional
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
from src import schemas
from src.db import crud
from src.utils import user_auth

router = APIRouter()


@router.get("/")
def get_items(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    return crud.item.get_multi(query={"userid": current_user["id"]})


@router.post("/")
def add_item(
    *,
    item: schemas.ItemCreate,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    new_item = schemas.ItemInDB(
        name=item.name,
        container_size=item.container_size,
        id=str(uuid4()),
        userid=current_user["id"],
    )
    return crud.item.create(obj=new_item.dict(exclude_unset=True))


@router.put("/")
def update_item(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    item: schemas.ItemUpdate,
):
    current_item = crud.item.get(id=item.id)
    if not current_item:
        raise HTTPException(
            status_code=404,
            detail="This item could not be found",
        )

    item_in = {"id": item.id, "userid": current_user["id"]}
    if item.container_size is not None:
        item_in["container_size"] = item.container_size
    if item.name is not None:
        item_in["name"] = item.name
    if item.is_active is not None:
        item_in["is_active"] = item.is_active

    return crud.item.update(db_obj=current_item, obj_in=item_in)


@router.delete("/")
def delete_item(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    item_id: UUID,
):
    query = {"id": str(item_id), "userid": current_user["id"]}
    return crud.item.delete(query=query)
