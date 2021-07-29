import secrets

from pydantic import BaseSettings


class GeneralSettings(BaseSettings):
    # ================================
    # Project configuration
    # ================================
    PROJECT_NAME: str = "BierLijst"
    API_V1_STR: str = "/api"
    DB_LOCATION: str = "src/db/db.json"
    USERS_OPEN_REGISTRATION: bool = True
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_SECRET_KEY: str = secrets.token_urlsafe(32)


settings = GeneralSettings()
