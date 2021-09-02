from typing import List
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
from src import schemas
from src.db import crud
from src.utils import user_auth

router = APIRouter()


@router.get("/{itemid}", response_model=schemas.Item)
def get_item(
    *, current_user: schemas.UserBase = Depends(user_auth.get_current_user), itemid
):
    return crud.item.get(id=itemid)


@router.get("", response_model=List[schemas.Item])
def get_items(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    return crud.item.get_multi(query={"userid": current_user["id"]})


@router.post("", response_model=schemas.Item)
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
    crud.person.add_item(
        id=new_item.id, userid=current_user["id"], enabled=item.enable_for_everyone
    )
    return crud.item.create(obj=new_item.dict())


@router.patch("", response_model=schemas.Item)
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


@router.patch("/{itemid}", response_model=schemas.Item)
def toggle_item_active(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    itemid: UUID,
):
    current_item = crud.item.get(id=itemid)
    if not current_item:
        raise HTTPException(
            status_code=404,
            detail="This item could not be found",
        )
    if current_item["is_active"]:
        # If item is disabled, disable the item on all persons
        crud.person.set_item_active(
            itemid=str(itemid), userid=current_user["id"], is_active=False
        )

    item_in = {"id": str(itemid), "userid": current_user["id"]}
    item_in["is_active"] = not current_item["is_active"]
    return crud.item.update(db_obj=current_item, obj_in=item_in)


@router.delete("/{itemid}", response_model=schemas.Item)
def delete_item(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    itemid: UUID,
):
    current_item = crud.item.get(id=itemid)
    if not current_item:
        raise HTTPException(
            status_code=404,
            detail="This item could not be found",
        )

    # Delete item from all persons, delete all transactions with that item, delete item
    crud.person.delete_item(itemid=str(itemid), userid=current_user["id"])
    crud.transaction.delete_many({"userid": current_user["id"], "itemid": str(itemid)})
    return crud.item.delete(query={"id": str(itemid), "userid": current_user["id"]})
