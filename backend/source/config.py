from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_URL: str
    SECRET_KEY: str
    REDIS_URL: str

    model_config = SettingsConfigDict(
        env_file="backend/.env",
        extra="ignore"
    )


Config = Settings()