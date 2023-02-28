from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    APP_NAME: str
    MODE: str

    # database configuration variables
    MONGO_URI: str

    class Config:
        env_file = ".env"
