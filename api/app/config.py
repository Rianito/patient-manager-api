from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "patient-manager"
    DEBUG_MODE: bool = False
    HOST: str = "0.0.0.0"
    PORT: int = 80
    DB_URL: str = "mongodb+srv://riangsilva:7Hs8igqwOUmcAdjr@cluster0.vgcybig.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME: str = "patients_manager"


settings = Settings()
