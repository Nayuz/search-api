from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    PROJECT_NAME: str = "SearchAPI"

    class Config:
        env_file = ".env"

setting = Setting()