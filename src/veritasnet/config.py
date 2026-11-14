"""Application configuration module using pydantic-settings v2."""

from typing import Literal
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Global immutable application settings loaded from environment."""

    model_config = SettingsConfigDict(
        env_prefix="VERITASNET_",
        env_file=".env",
        env_file_encoding="utf-8",
        frozen=True,
        extra="ignore",
    )

    app_name: str = Field(default="VeritasNet", description="Application service name")
    environment: Literal["development", "testing", "staging", "production"] = Field(
        default="development",
        description="Deployment runtime environment",
    )
    port: int = Field(
        default=8000,
        description="Application network port",
    )