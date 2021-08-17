from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: Optional[str] = None
    container_size: Optional[int] = 24
    is_active: Optional[bool] = True


class ItemCreate(ItemBase):
    name: str
    container_size: int = 24


class ItemUpdate(ItemBase):
    id: str
    container_size: Optional[int] = None
    is_active: Optional[bool] = None


class Item(ItemBase):
    id: str


class ItemInDB(ItemBase):
    id: Optional[str] = None
    userid: Optional[str] = None

    class Config:
        orm_mode = True
