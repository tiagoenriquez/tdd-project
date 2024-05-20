from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Store API"
    ROOT_PATH: str = "../../"
    DATABASE_URL: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding='utf-8')


settings = Settings()