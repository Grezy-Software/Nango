"""Generate secrets for .django file of .env.

Run the script with the .env name as the first argument.
    backend/config/secret_generator.py <env_name>
"""  # noqa: INP001

import os
import sys
from pathlib import Path

from cryptography.fernet import Fernet


def _generate_key(multiplier: int = 1) -> str:
    """Generate a key with a multiplier."""
    return "".join([Fernet.generate_key().decode()[:-1] for _ in range(multiplier)])


def get_or_generate_key(name: str, multiplier: int = 1) -> str:
    """Return the key if it exists, otherwise generate a new key."""
    result = os.environ.get(name, None)
    if result is None or result == "":
        result = _generate_key(multiplier)
    return result


def make_folder(env_name: str) -> Path:
    """Build .envs folder."""
    root_dir: Path = Path(__file__).resolve(strict=True).parent.parent.joinpath("backend")
    if not root_dir.is_dir():
        root_dir.mkdir(parents=True)
    folder = root_dir.joinpath(f".envs/.{env_name}")
    if not folder.is_dir():
        folder.mkdir(parents=True)
    return folder


def build_postgres_env(env_name: str) -> None:
    """Build .postgres file of .env."""
    folder: Path = make_folder(env_name)
    path: Path = folder.joinpath(".postgres")
    if path.is_file():
        return

    content: str = "# PostgreSQL\n"
    content += "# ------------------------------------------------------------------------------\n"
    content += 'POSTGRES_HOST = "postgres"\n'
    content += "POSTGRES_PORT = 5432\n"
    content += 'POSTGRES_DB = "Nango"\n'
    content += f'POSTGRES_USER = "{get_or_generate_key(name="POSTGRES_USER")}"\n'
    content += f'POSTGRES_PASSWORD = "{get_or_generate_key(name="POSTGRES_PASSWORD", multiplier=2)}" # noqa: S105\n'

    postgres_env_file = path.open("w+")
    postgres_env_file.writelines(content)
    postgres_env_file.close()


def build_django_secrets(env_name: str) -> None:
    """Build secrets for .django file of .env."""
    folder: Path = make_folder(env_name)
    path: Path = folder.joinpath(".django")

    content: str = "# General\n"
    content += "# ------------------------------------------------------------------------------\n"
    content += 'USE_DOCKER="yes"\n'
    content += 'IPYTHONDIR="/app/.ipython"\n'
    content += 'REDIS_URL="redis://redis:6379/0"\n'
    content += "\n# Django\n"
    content += "# ------------------------------------------------------------------------------\n"
    content += f'DJANGO_SECRET_KEY="{get_or_generate_key(name="DJANGO_SECRET_KEY")}" # noqa: S105\n'
    content += "DJANGO_DEBUG=True\n"
    content += "IS_LOCAL=True\n"
    content += f'CELERY_FLOWER_USER="{get_or_generate_key(name="CELERY_FLOWER_USER")}"\n'
    content += f'CELERY_FLOWER_PASSWORD="{get_or_generate_key(name= "CELERY_FLOWER_PASSWORD", multiplier=2)}" # noqa: S105\n'

    django_env_file = path.open("w+")
    django_env_file.writelines(content)
    django_env_file.close()


if __name__ == "__main__":
    env_name = sys.argv[1]
    build_postgres_env(env_name)
    build_django_secrets(env_name)
