import time
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Change(BaseModel):
    container: Optional[int]
    consumable: Optional[int]


class TransactionBase(BaseModel):
    timestamp: Optional[int] = int(time.time())
    is_active: Optional[bool] = True
    itemid: Optional[str] = None
    personid: Optional[str] = None
    change: Optional[Change]


class TransactionCreate(TransactionBase):
    itemid: str
    personid: str
    change: Change

    # change = {
    #     "container": 1,
    #     "consumable": 24
    # }


class TransactionUpdate(TransactionBase):
    id: str
    itemid: Optional[str] = None
    personid: Optional[str] = None
    change: Optional[dict] = None


class TransactionInDB(TransactionBase):
    id: Optional[str] = None
    userid: Optional[str] = None

    class Config:
        orm_mode = True
