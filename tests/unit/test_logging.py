# tests/unit/test_logging.py
import logging
from app.core.logging import logger

def test_logger():
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.INFO
    assert len(logger.handlers) == 2  # Console and file handlers