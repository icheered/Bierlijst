from pymongo import MongoClient
from src.utils.config import settings

db = MongoClient(
    settings.MONGO_ADDRESS,
    port=settings.MONGO_PORT,
    username=settings.MONGO_USERNAME,
    password=settings.MONGO_PASSWORD,
)[settings.PROJECT_NAME]

from .crud_item import item
from .crud_person import person
from .crud_transaction import transaction
from .crud_user import user
