from copy import copy
from typing import List
from uuid import UUID, uuid4

from src import schemas
from src.db.crud.base import CRUDBase
from src.utils import misc


class CRUDPerson(CRUDBase):
    def add_person(self, userid: UUID, person: schemas.PersonCreate, balance: list):
        # For each person, generate UUID, set USERID, generate color
        db_obj = schemas.PersonInDB(
            id=str(uuid4()),
            userid=userid,
            name=person.name,
            color=misc.get_random_color_hex(),
            balance=balance,
        )
        return super().create(obj=db_obj.dict())

    def delete_person(self, userid: UUID, personid: UUID):
        ret = super().get(str(personid))
        query = {"userid": str(userid), "id": str(personid)}
        super().delete(query)
        return ret

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

    def add_item(self, id: str, userid: str, enabled: bool):
        """
        Add an item to every person's balance

        :param id: Item ID
        :param userid: User ID to determine which people should be updated
        :param enabled: Whether to enable the item for the person
        """
        itemdict = {"id": id, "container": 0, "consumable": 0, "is_active": enabled}
        self.table.update_many({"userid": userid}, {"$push": {"balance": itemdict}})

    def set_item_active(
        self, itemid: str, userid: str, is_active: bool, personid: str = None
    ):
        if personid is None:
            self.table.update_many(
                {"userid": userid, "balance.id": itemid},
                {"$set": {"balance.$.is_active": is_active}},
            )
        else:
            self.table.update_one(
                {"userid": userid, "id": personid, "balance.id": itemid},
                {"$set": {"balance.$.is_active": is_active}},
            )

    def delete_item(self, itemid: str, userid: str):
        self.table.update_many(
            {"userid": userid}, {"$pull": {"balance": {"id": itemid}}}
        )


person = CRUDPerson(table="person")
