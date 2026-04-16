from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")

    # Telegram
    bot_token: str
    webhook_url: str
    mini_app_url: str
    trainer_telegram_id: int

    # Database
    database_url: str
    test_database_url: str = ""

    # Redis
    redis_url: str = "redis://redis:6379/0"

    # Security
    secret_key: str

    # Payments
    lava_top_api_key: str = ""
    lava_top_secret_key: str = ""


settings = Settings()
