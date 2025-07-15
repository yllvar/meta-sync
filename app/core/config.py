# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    mt5_login: int
    mt5_password: str
    mt5_server: str
    mt5_path: str
    api_key: str
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()