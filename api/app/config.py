from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "patient-manager"
    DEBUG_MODE: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 80
    DB_URL: str = ""
    DB_NAME: str = ""


settings = Settings()
