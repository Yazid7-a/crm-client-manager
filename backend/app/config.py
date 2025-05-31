from pydantic import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "clave_super_secreta_123"  # cámbiala por seguridad
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
