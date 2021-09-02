from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from src import schemas
from src.db import crud
from src.utils import user_auth

router = APIRouter()


@router.get("/{personid}", response_model=schemas.Person)
def get_person(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    personid: str,
):
    return crud.person.get(id=personid)


@router.get("", response_model=List[schemas.Person])
def get_people(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    return crud.person.get_multi({"userid": current_user["id"]})


@router.post("", response_model=schemas.Person)
def add_person(
    *,
    person: schemas.PersonCreate,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    items = crud.item.get_multi({"userid": current_user["id"]})
    balance = []
    for item in items:
        balance.append(
            {
                "id": item["id"],
                "container": 0,
                "consumable": 0,
                "is_active": item["is_active"],
            }
        )
    return crud.person.add_person(
        userid=current_user["id"], person=person, balance=balance
    )


@router.patch("", response_model=schemas.Person)
def update_person(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    person: schemas.PersonInDB,
):
    current_person = crud.person.get_multi(
        {"id": person.id, "userid": current_user["id"]}
    )
    if not current_person:
        raise HTTPException(
            status_code=404,
            detail="This person could not be found",
        )
    current_person = current_person[0]
    user_in = {
        "userid": current_user["id"],
        "id": person.id,
    }

    if person.name is not None:
        user_in["name"] = person.name
    if person.color is not None:
        user_in["color"] = person.color
    if person.balance is not None:
        user_in["balance"] = person.balance
    if person.is_active is not None:
        user_in["is_active"] = person.is_active
    return crud.person.update(db_obj=current_person, obj_in=user_in)


@router.patch("/{personid}", response_model=schemas.Person)
def toggle_person_active(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    personid: UUID,
):
    current_person = crud.person.get(id=personid)
    if not current_person:
        raise HTTPException(
            status_code=404,
            detail="This person could not be found",
        )
    person_in = {"id": str(personid), "userid": current_user["id"]}
    person_in["is_active"] = not current_person["is_active"]
    return crud.person.update(db_obj=current_person, obj_in=person_in)


@router.patch("/{personid}/{itemid}", response_model=schemas.Person)
def toggle_item(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    personid: UUID,
    itemid: UUID,
):
    itemid = str(itemid)
    personid = str(personid)
    current_person = crud.person.get(id=personid)
    if not current_person:
        raise HTTPException(
            status_code=404,
            detail="This person could not be found",
        )
    current_item = crud.item.get(id=itemid)
    if not current_item:
        raise HTTPException(
            status_code=404,
            detail="This item could not be found",
        )

    for item in current_person["balance"]:
        if item["id"] == itemid:

            # If a user enabled a disabled item, enable the item
            if not item["is_active"] and not current_item["is_active"]:
                item_in = {"id": str(itemid), "userid": current_user["id"]}
                item_in["is_active"] = not current_item["is_active"]
                crud.item.update(db_obj=current_item, obj_in=item_in)

            crud.person.set_item_active(
                itemid=itemid,
                userid=current_user["id"],
                is_active=not item["is_active"],
                personid=personid,
            )

    return crud.person.get(id=personid)


@router.delete("/{personID}", response_model=schemas.Person)
def delete_person(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    personID: UUID,
):
    return crud.person.delete_person(userid=current_user["id"], personid=personID)
