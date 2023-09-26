import os

from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict


class DBModel(BaseModel):
    host: str
    port: str
    name: str
    user: str
    password: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        env_file='prostir/.env',
        env_file_encoding='utf-8',
    )

    db: DBModel


settings = Settings()
