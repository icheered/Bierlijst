import time
from copy import deepcopy
from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends, HTTPException
from src import schemas
from src.db import crud
from src.utils import user_auth

router = APIRouter()


@router.get("/{transactionid}", response_model=schemas.Person)
def get_transaction(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    transactionid: str,
):
    return crud.transaction.get(id=transactionid)


@router.get("", response_model=List[schemas.Transaction])
def get_transactions(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    skip: int = 0,
    limit: int = 20,
):
    return crud.transaction.get_multi(
        query={"userid": current_user["id"]}, skip=skip, limit=limit
    )


@router.post("", response_model=schemas.Transaction)
def add_transaction(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    transaction: schemas.TransactionCreate,
):
    if not crud.item.get(id=transaction.itemid):
        raise HTTPException(
            status_code=404,
            detail="Unknown item",
        )
    old_person = crud.person.get(id=transaction.personid)
    if not old_person:
        raise HTTPException(
            status_code=404,
            detail="This person could not be found",
        )

    new_transaction = schemas.TransactionInDB(
        id=str(uuid4()),
        userid=current_user["id"],
        change=transaction.change,
        personid=transaction.personid,
        itemid=transaction.itemid,
        is_active=transaction.is_active if hasattr(transaction, "is_active") else True,
    ).dict(exclude_none=True)
    if not new_transaction["change"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid transaction",
        )

    new_person = crud.person.apply_transaction(
        user=deepcopy(old_person), transaction=new_transaction
    )
    crud.person.update(db_obj=old_person, obj_in=new_person)
    return crud.transaction.create(obj=new_transaction)


@router.patch("", response_model=schemas.Transaction)
def update_transaction(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    transaction: schemas.TransactionUpdate,
):
    current_transaction = crud.transaction.get(id=transaction.id)
    if not current_transaction:
        raise HTTPException(
            status_code=404,
            detail="This transaction could not be found",
        )
    if not crud.item.get(id=transaction.itemid):
        raise HTTPException(
            status_code=404,
            detail="Unknown item",
        )

    transaction_in = {"id": id, "userid": current_user["id"]}
    if transaction.itemid is not None:
        transaction_in["itemid"] = transaction.itemid
    if transaction.personid is not None:
        transaction_in["personid"] = transaction.personid
    if transaction.change is not None:
        transaction_in["change"] = transaction.change

    return crud.transaction.update(db_obj=current_transaction, obj_in=transaction_in)


@router.patch("/{transactionid}", response_model=schemas.Transaction)
def toggle_transaction(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    transactionid: str,
):
    current_transaction = dict(crud.transaction.get(id=transactionid))
    if not current_transaction:
        raise HTTPException(
            status_code=404,
            detail="This transaction could not be found",
        )
    transaction_in = {
        "id": str(transactionid),
        "userid": current_user["id"],
        "is_active": not current_transaction["is_active"],
    }

    # When going from active to inactive, revert the transaction changes
    old_person = dict(crud.person.get(id=current_transaction["personid"]))
    if current_transaction["is_active"]:
        c = deepcopy(current_transaction)
        if "container" in c["change"]:
            c["change"]["container"] *= -1
        if "consumable" in c["change"]:
            c["change"]["consumable"] *= -1
        new_person = crud.person.apply_transaction(
            user=deepcopy(old_person), transaction=c
        )
    if not current_transaction["is_active"]:
        c = deepcopy(current_transaction)
        new_person = crud.person.apply_transaction(
            user=deepcopy(old_person), transaction=c
        )
    crud.person.update(db_obj=old_person, obj_in=new_person)

    return crud.transaction.update(db_obj=current_transaction, obj_in=transaction_in)


@router.delete("", response_model=schemas.Transaction)
def delete_transaction(
    *,
    current_user: schemas.UserBase = Depends(user_auth.get_current_user),
    transaction_id: UUID,
):
    current_transaction = dict(crud.transaction.get(id=str(transaction_id)))
    if not current_transaction:
        raise HTTPException(
            status_code=404,
            detail="This transaction could not be found",
        )

    # When going from active to inactive, revert the transaction changes
    if current_transaction["is_active"]:
        old_person = dict(crud.person.get(id=current_transaction["personid"]))
        c = deepcopy(current_transaction)
        if "container" in c["change"]:
            c["change"]["container"] *= -1
        if "consumable" in c["change"]:
            c["change"]["consumable"] *= -1
        new_person = crud.person.apply_transaction(
            user=deepcopy(old_person), transaction=c
        )
        crud.person.update(db_obj=old_person, obj_in=new_person)

    query = {"id": str(transaction_id), "userid": current_user["id"]}
    return crud.transaction.delete(query=query)


@router.delete("/all")
def delete_transaction_all(
    *, current_user: schemas.UserBase = Depends(user_auth.get_current_user)
):
    crud.transaction.delete_all()
