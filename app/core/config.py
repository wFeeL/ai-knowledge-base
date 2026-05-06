from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Knowledge Base"
    debug: bool = True
    environment: str = "local"

    model_config = SettingsConfigDict(env_file=".env")
    database_url: str = "postgresql+psycopg2://<username>:<password>@<host>:<port>/<database_name>"


settings = Settings()