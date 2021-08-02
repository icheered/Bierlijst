from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from src import schemas
from src.db import crud
from src.utils import user_auth

router = APIRouter()


@router.get("/")
def get_people(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    return crud.people.get_multi({"userid": current_user["id"]})


@router.post("/")
def add_people(
    *,
    people: List[schemas.people.PersonCreate],
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
):
    return crud.people.add_people(userid=current_user["id"], people=people)


@router.put("/")
def update_person(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    person: schemas.PersonInDB,
):
    current_person = crud.people.get_multi(
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
    return crud.people.update(db_obj=current_person, obj_in=user_in)


@router.delete("/")
def delete_people(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    people: List[UUID],
):
    return crud.people.delete_people(userid=current_user["id"], people=people)
