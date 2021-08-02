from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# Shared properties
class PersonBase(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    is_active: Optional[bool] = True
    balance: Optional[dict] = {}


# Properties to receive via API on creation
class PersonCreate(PersonBase):
    name: str


# Properties to receive via API on update
class PersonUpdate(PersonBase):
    id: str
    name: Optional[str] = None
    color: Optional[str] = None
    is_active: Optional[bool] = None
    balance: Optional[dict] = None


# Additional properties stored in DB
class PersonInDB(PersonBase):
    id: Optional[str] = None
    userid: Optional[str] = None

    class Config:
        orm_mode = True
