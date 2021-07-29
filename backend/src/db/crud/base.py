from typing import Any
from uuid import UUID, uuid4

from src.utils.config import settings
from tinydb import TinyDB, where

db = TinyDB(settings.DB_LOCATION)


class CRUDBase:
    def __init__(self, table: str):
        self.table = db.table(table)

    def get(self, id: UUID):
        return self.table.search(where("id") == id)

    def get_multi(self, query: dict):
        # use fragment: find all documents that match this dict
        pass

    def create(self, obj: dict):
        obj["id"] = str(uuid4())
        return self.table.insert(obj)

    def update(self, obj: dict):
        return self.table.update(cond=obj["id"], fields=obj)

    def delete(self, id: UUID):
        return self.table.remove(where("id") == id)

    def delete_all(self):
        return self.table.remove()
