from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext
from passlib.utils import generate_password
from src.utils.config import settings

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
    argon2__type="ID",
    argon2__salt_size=32,
    argon2__rounds=4,
    argon2__digest_size=64,
    argon2__memory_cost=4096,
    argon2__parallelism=2,
)


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], domain: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject), "dom": str(domain)}
    encoded_jwt = jwt.encode(
        to_encode, settings.BACKEND_SECRET_KEY, algorithm=ALGORITHM
    )
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def generate_random_token() -> str:
    """Generates a random password with the passlib library.
    The used charset are all alphanumerical characters, except
    of the characters '1IiLl0OoS5'.
    """
    return generate_password(size=64)
