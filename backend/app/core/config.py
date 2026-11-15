from functools import lru_cache
from typing import Literal, Self

from pydantic import SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """All app settings. Values come from environment variables or a .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # General settings
    app_name: str = "AgentForge"
    app_version: str = "0.1.0"
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"

    # Browser security settings
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"

    # LLM settings
    llm_provider: Literal["mock", "anthropic"] = "mock"
    anthropic_api_key: SecretStr | None = None

    @property
    def cors_origin_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.cors_origins.split(",")
            if origin.strip()
        ]

    @model_validator(mode="after")
    def check_llm_settings(self) -> Self:
        if self.llm_provider == "anthropic":
            if (
                not self.anthropic_api_key
                or not self.anthropic_api_key.get_secret_value().strip()
            ):
                raise ValueError(
                    "ANTHROPIC_API_KEY is required when LLM_PROVIDER=anthropic"
                )
        return self


@lru_cache
def get_settings() -> Settings:
    return Settings()
