from typing import Any, Dict, Union
from uuid import uuid4

from pydantic import EmailStr
from src import schemas
from src.db.crud.base import CRUDBase
from src.schemas.user import UserCreate, UserInDB
from src.utils.security import get_password_hash, verify_password
from tinydb import where


class CRUDUser(CRUDBase):
    def get_by_email(self, email: EmailStr):
        return self.table.get(where("email") == email)

    def get_by_username(self, username: str):
        return self.table.get(where("username") == username)

    def create(self, obj: UserCreate):
        db_obj = UserInDB(
            id=str(uuid4()),
            email=obj.email,
            full_name=obj.full_name,
            username=obj.username,
            hashed_password=get_password_hash(obj.password),
        )
        return super().create(obj=db_obj.dict())

    def authenticate(self, username: str, password: str):
        user = self.get_by_email(email=username)
        if not user:
            user = self.get_by_username(username=username)
            if not user:
                return None
        if not verify_password(password, user["hashed_password"]):
            return None
        return user

    def is_active(self, user: UserInDB) -> bool:
        return user["is_active"]

    def is_verified(self, user: UserInDB) -> bool:
        return user["is_verified"]

    def update(self, db_obj: dict, obj_in: Union[schemas.UserUpdate, Dict[str, Any]]):
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data.get("password") is not None:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db_obj=db_obj, obj_in=update_data)


user = CRUDUser(table="user")
