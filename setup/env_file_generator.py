"""Generate secrets for .django file of .env.

Run the script with the .env name as the first argument.
    backend/config/secret_generator.py <env_name>
"""  # noqa: INP001

import sys
from pathlib import Path

from cryptography.fernet import Fernet


def _generate_key(multiplier: int = 1) -> str:
    """Generate a key with a multiplier."""
    return "".join([Fernet.generate_key().decode()[:-1] for _ in range(multiplier)])


def _make_folder(env_name: str) -> Path:
    root_dir: Path = Path(__file__).resolve(strict=True).parent.parent.joinpath("backend")
    if not root_dir.is_dir():
        root_dir.mkdir(parents=True)
    folder = root_dir.joinpath(f".envs/.{env_name}")
    if not folder.is_dir():
        folder.mkdir(parents=True)
    return folder


def build_postgres_env(env_name: str) -> None:
    """Build .postgres file of .env."""
    folder: Path = _make_folder(env_name)
    path: Path = folder.joinpath(".postgres")
    if path.is_file():
        return

    content: str = "# PostgreSQL\n"
    content += "# ------------------------------------------------------------------------------\n"
    content += 'POSTGRES_HOST = "postgres"\n'
    content += "POSTGRES_PORT = 5432\n"
    content += 'POSTGRES_DB = "napse_developer_toolkit"\n'
    content += f'POSTGRES_USER = "{_generate_key()}"\n'
    content += f'POSTGRES_PASSWORD = "{_generate_key(2)}" # noqa: S105\n'

    postgres_env_file = path.open("w+")
    postgres_env_file.writelines(content)
    postgres_env_file.close()


def build_django_secrets(env_name: str) -> None:
    """Build secrets for .django file of .env."""
    folder: Path = _make_folder(env_name)
    path: Path = folder.joinpath(".django")

    content: str = "# General\n"
    content += "# ------------------------------------------------------------------------------\n"
    content += 'USE_DOCKER="yes"\n'
    content += 'IPYTHONDIR="/app/.ipython"\n'
    content += 'REDIS_URL="redis://redis:6379/0"\n'
    content += "\n# Django\n"
    content += "# ------------------------------------------------------------------------------\n"
    content += f'DJANGO_SECRET_KEY="{_generate_key()}" # noqa: S105\n'
    content += "DJANGO_DEBUG=True\n"
    content += "IS_LOCAL=True\n"
    content += f'CELERY_FLOWER_USER="{_generate_key()}"\n'
    content += f'CELERY_FLOWER_PASSWORD="{_generate_key(2)}" # noqa: S105\n'

    django_env_file = path.open("w+")
    django_env_file.writelines(content)
    django_env_file.close()


if __name__ == "__main__":
    env_name = sys.argv[1]
    build_postgres_env(env_name)
    build_django_secrets(env_name)
