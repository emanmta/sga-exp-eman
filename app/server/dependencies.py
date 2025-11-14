from functools import lru_cache
from pydantic_settings import BaseSettings

from typing import Optional

class Settings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    
    # Database variables from your .env
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    
    # Other variables from your .env
    SECRET_KEY: str
    GOOGLE_API_KEY: str
    LETTA_API_KEY: str
    LETTA_BASE_URL: str

    class Config:
        env_file = ".env"
        extra = 'ignore' # This will ignore any extra variables in .env

@lru_cache()
def get_settings():
    return Settings()