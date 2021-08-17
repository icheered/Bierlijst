from fastapi import APIRouter
from src.api.endpoints import item, login, person, transaction, user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(login.router, tags=["login"])
api_router.include_router(person.router, prefix="/person", tags=["people"])
api_router.include_router(item.router, prefix="/item", tags=["item"])
api_router.include_router(
    transaction.router, prefix="/transaction", tags=["transaction"]
)
