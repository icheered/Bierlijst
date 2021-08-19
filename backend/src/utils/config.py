import secrets

import dotenv
from pydantic import BaseSettings


class GeneralSettings(BaseSettings):
    # ================================
    # Project configuration
    # ================================
    PROJECT_NAME: str = "bierLijst"
    API_V1_STR: str = "/api"
    USERS_OPEN_REGISTRATION: bool = True
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_SECRET_KEY: str = secrets.token_urlsafe(32)

    # ================================
    # Database Configuration
    # ================================
    MONGO_ADDRESS: str
    MONGO_PORT: int
    MONGO_USERNAME: str
    MONGO_PASSWORD: str

    MONGO_DB: str = "bierlijst"

    # Supplement these config values with values from .env file
    class Config:
        case_sensitive = True
        env_file = dotenv.find_dotenv()
        env_file_encodig = "utf-8"


settings = GeneralSettings()
