from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_KEY: str
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
