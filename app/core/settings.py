"""
Settings.
"""
import toml

from pydantic import BaseSettings

with open("../pyproject.toml", "r") as pyproject:
    pyproject_content = pyproject.read()
    pyproject_parsed = toml.loads(pyproject_content)
    VERSION = pyproject_parsed["tool"]["poetry"]["version"]

class DbConfig(BaseSettings):
    """
    Table Name Settings.
    """

    mongodb_database: str
    mongodb_host: str
    mongodb_port: str
    mongodb_collection: str

    class Config:
        """.env configuration"""

        env_file = ".env"


class Settings(BaseSettings):
    """
    Application settings.
    """

    app_name: str = "Example API"
    app_version: str = VERSION
    api_prefix: str = "/api"
    is_debug: bool = True

    db_config: DbConfig = DbConfig()

settings = Settings()
