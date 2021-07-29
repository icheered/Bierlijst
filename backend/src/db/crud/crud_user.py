from uuid import uuid4

from pydantic import EmailStr
from src.db.crud.base import CRUDBase
from src.schemas.user import UserCreate, UserInDB
from src.utils.security import get_password_hash
from tinydb import where


class CRUDUser(CRUDBase):
    def get_by_email(self, email: EmailStr):
        return self.table.search(where("email") == email)

    def create(self, obj: UserCreate):
        db_obj = UserInDB(
            id=str(uuid4()),
            email=obj.email,
            full_name=obj.full_name,
            hashed_password=get_password_hash(obj.password),
        )
        return self.table.insert(db_obj.dict())


user = CRUDUser(table="user")
