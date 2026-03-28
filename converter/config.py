"""Configuration loader for the Socratex PDF converter."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


class ConfigError(Exception):
    """Raised when required configuration is missing or invalid."""


@dataclass(frozen=True)
class ConverterConfig:
    api_token: str
    output_dir: Path
    model: str


_DEFAULT_OUTPUT_DIR = "books/"
_DEFAULT_MODEL = "vlm"


def _find_env_file() -> Path | None:
    """Walk up from cwd to locate a .env file."""
    current = Path.cwd()
    for directory in [current, *current.parents]:
        candidate = directory / ".env"
        if candidate.is_file():
            return candidate
    return None


def _read_token() -> str:
    token = os.environ.get("MINERU_API_TOKEN", "").strip()
    if not token:
        raise ConfigError(
            "MINERU_API_TOKEN is not set. "
            "Add it to your .env file or export it as an environment variable.\n"
            "Get a token at: https://mineru.net/apiManage"
        )
    return token


def load_config(
    *,
    output_dir: str | None = None,
    model: str | None = None,
) -> ConverterConfig:
    """Load and validate converter configuration.

    Environment is loaded from the nearest .env file. CLI overrides
    take precedence over defaults.
    """
    env_file = _find_env_file()
    if env_file is not None:
        load_dotenv(env_file, override=False)

    return ConverterConfig(
        api_token=_read_token(),
        output_dir=Path(output_dir or _DEFAULT_OUTPUT_DIR),
        model=model or _DEFAULT_MODEL,
    )
