from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from src import schemas
from src.db import crud
from src.utils import user_auth

router = APIRouter()


@router.get("/{personid}", response_model=schemas.Person)
def get_person(
    *, current_user: schemas.UserBase = Depends(user_auth.get_current_user), personid
):
    return crud.person.get(id=personid)


@router.get("", response_model=List[schemas.Person])
def get_people(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):

    return crud.person.get_multi({"userid": current_user["id"]})


@router.post("", response_model=List[schemas.Person])
def add_people(
    *,
    people: List[schemas.PersonCreate],
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    return crud.person.add_people(userid=current_user["id"], people=people)


@router.put("", response_model=schemas.Person)
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


@router.delete("", response_model=List[schemas.Person])
def delete_people(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    people: List[UUID],
):
    return crud.person.delete_people(userid=current_user["id"], people=people)
