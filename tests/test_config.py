"""Test suite for VeritasNet application configuration."""

import pytest
from veritasnet.config import Settings


def test_settings_default_values(monkeypatch: pytest.MonkeyPatch) -> None:
    """Verify settings loads default values in a clean environment."""
    # Ensure no environment variables interfere with our default test
    monkeypatch.delenv("VERITASNET_ENVIRONMENT", raising=False)
    monkeypatch.delenv("VERITASNET_PORT", raising=False)

    settings = Settings()

    assert settings.app_name == "VeritasNet"
    assert settings.environment == "development"
    assert settings.port == 8000