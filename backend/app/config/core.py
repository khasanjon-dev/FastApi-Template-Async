import logging
import os

from dotenv import load_dotenv

load_dotenv("/app/.env")

logger = logging.getLogger(__name__)


class Settings:
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True if os.getenv("DEBUG") == "True" else False
    PROJECT_NAME: str = "Template API"

    # DATABASE
    SQL_URL: str = os.getenv("SQL_URL")
    SQL_ECHO: bool = True


settings = Settings()
