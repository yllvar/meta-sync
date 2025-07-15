# app/core/logging.py
import logging
from typing import Optional

from app.core.config import settings

def setup_logging():
    logger = logging.getLogger("metasync")
    logger.setLevel(settings.log_level.upper())

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(settings.log_level.upper())
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # File handler
    file_handler = logging.FileHandler("metasync.log")
    file_handler.setLevel(settings.log_level.upper())
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger

logger = setup_logging()