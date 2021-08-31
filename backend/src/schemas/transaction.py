from time import time
from typing import Optional

from pydantic import BaseModel, Field


class Change(BaseModel):
    container: Optional[int]
    consumable: Optional[int]


class TransactionBase(BaseModel):
    timestamp: int = Field(default_factory=time)
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


class Transaction(TransactionBase):
    id: str


class TransactionInDB(TransactionBase):
    id: Optional[str] = None
    userid: Optional[str] = None

    class Config:
        orm_mode = True
