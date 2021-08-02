from typing import Any
from uuid import UUID, uuid4

from src.utils.config import settings
from tinydb import Query, TinyDB, where

db = TinyDB(settings.DB_LOCATION)


class CRUDBase:
    def __init__(self, table: str):
        self.table = db.table(table)

    def get(self, id: UUID):
        return self.table.get(where("id") == str(id))

    def get_multi(self, query: dict):
        return self.table.search(Query().fragment(query))

    def create(self, obj: dict):
        if "id" not in obj:
            obj["id"] = str(uuid4())
        self.table.insert(obj)
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
        self.table.update(cond=where("id") == db_obj["id"], fields=obj_in)
        return obj_in

    def delete(self, query: dict):
        return self.table.remove(Query().fragment(query))

    def delete_all(self):
        return self.table.remove()
