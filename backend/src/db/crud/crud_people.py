from typing import List
from uuid import UUID, uuid4

from src import schemas
from src.db.crud.base import CRUDBase
from src.utils import misc


class CRUDPeople(CRUDBase):
    def add_people(self, userid: UUID, people: List[schemas.people.PersonCreate]):
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
            query = {"userid": str(userid), "id": str(personID)}
            retlist.append(super().get_multi(query))
            super().delete(query)
        return retlist

    def apply_transaction(self, user: dict, transaction: dict):
        if transaction["itemid"] not in user["balance"]:
            user["balance"][transaction["itemid"]] = transaction["change"].copy()
            return user

        if "container" in transaction["change"]:
            if "container" not in user["balance"][transaction["itemid"]]:
                user["balance"][transaction["itemid"]]["container"] = transaction[
                    "change"
                ]["container"].copy()
            else:
                user["balance"][transaction["itemid"]]["container"] = (
                    user["balance"][transaction["itemid"]]["container"]
                    + transaction["change"]["container"]
                )

        if "consumable" in transaction["change"]:
            if "consumable" not in user["balance"][transaction["itemid"]]:
                user["balance"][transaction["itemid"]]["consumable"] = transaction[
                    "change"
                ]["consumable"].copy()
            else:
                user["balance"][transaction["itemid"]]["consumable"] = (
                    user["balance"][transaction["itemid"]]["consumable"]
                    + transaction["change"]["consumable"]
                )
        return user


people = CRUDPeople(table="people")
