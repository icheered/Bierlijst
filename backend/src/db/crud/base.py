from typing import Any
from uuid import UUID, uuid4

from src.utils.config import settings
from tinydb import Query, TinyDB, where

from . import db


class CRUDBase:
    def __init__(self, table: str):
        self.table = db[table]

    def get(self, id: UUID):
        return self.table.find_one({"id": str(id)})

    def get_multi(self, query: dict):
        retl = []
        for ret in self.table.find(query):
            retl.append(ret)
        return retl

    def create(self, obj: dict):
        if "id" not in obj:
            obj_id = uuid4()
            while self.get(id=obj_id):
                obj_id = uuid4()
            obj["id"] = str(obj_id)
        self.table.insert_one(obj)
        return obj

    def update(self, db_obj: dict, obj_in: dict):
        """
        Update a field in the database

        Args:
            db_obj (dict): Current object that exists in database
            obj_in (dict): Updated object to be inserted

        Returns:
            [schema]: Updated model
        """
        self.table.update_one(filter=db_obj, update={"$set": obj_in})
        return obj_in

    def delete(self, query: dict):
        item = self.get(id=query["id"])
        self.table.delete_one(query)
        return item

    def delete_all(self):
        return self.table.delete_many({})
