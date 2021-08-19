from copy import copy
from typing import List
from uuid import UUID, uuid4

from src import schemas
from src.db.crud.base import CRUDBase
from src.utils import misc


class CRUDPerson(CRUDBase):
    def add_people(self, userid: UUID, people: List[schemas.PersonCreate]):
        # For each person, generate UUID, set USERID, generate color
        retlist = []
        for person in people:
            db_obj = schemas.PersonInDB(
                id=str(uuid4()),
                userid=userid,
                name=person.name,
                color=misc.get_random_color_hex(),
            )
            ret = super().create(obj=db_obj.dict())
            retlist.append(ret)
        return retlist

    def delete_people(self, userid: UUID, people: List[UUID]):
        retlist = []
        for personID in people:

            retlist.append(super().get(str(personID)))
            query = {"userid": str(userid), "id": str(personID)}
            super().delete(query)
        return retlist

    def apply_transaction(self, user: dict, transaction: dict):
        user_items = [val["id"] for val in user["balance"]]
        if transaction["itemid"] not in user_items:
            user["balance"].append(
                dict(
                    list({"id": transaction["itemid"]}.items())
                    + list(copy(transaction["change"]).items())
                )
            )
            return user

        item_balance = next(
            (item for item in user["balance"] if item["id"] == transaction["itemid"])
        )  # Not explicitly copied, REFERENCES the item balance in user["balance"]

        if (
            "container" in transaction["change"]
            and transaction["change"]["container"] is not None
        ):
            if "container" not in item_balance:
                item_balance["container"] = copy(transaction["change"]["container"])
            else:
                item_balance["container"] += transaction["change"]["container"]

        if (
            "consumable" in transaction["change"]
            and transaction["change"]["consumable"] is not None
        ):
            if "consumable" not in item_balance:
                item_balance["consumable"] = copy(transaction["change"]["consumable"])
            else:
                item_balance["consumable"] += transaction["change"]["consumable"]
        return user


person = CRUDPerson(table="person")
