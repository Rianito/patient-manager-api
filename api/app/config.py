from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "patient-manager"
    DEBUG_MODE: bool = True
    HOST: str = "192.168.0.7"
    PORT: int = 8000
    DB_URL: str = "mongodb+srv://riangsilva:7Hs8igqwOUmcAdjr@cluster0.vgcybig.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME: str = "patients"


settings = Settings()
