from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    MONGO_URI: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
