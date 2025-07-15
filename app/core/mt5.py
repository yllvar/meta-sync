# app/core/mt5.py
import MetaTrader5 as mt5
from app.core.config import settings
from app.core.logging import logger

class MT5Connection:
    def __init__(self):
        self.connected = False

    def initialize(self):
        if not self.connected:
            if mt5.initialize(path=settings.mt5_path, login=settings.mt5_login, password=settings.mt5_password, server=settings.mt5_server):
                self.connected = True
                logger.info("MetaTrader 5 initialized successfully.")
            else:
                logger.error("Failed to initialize MetaTrader 5.")
                raise Exception("Failed to initialize MetaTrader 5.")

    def login(self):
        if not self.connected:
            self.initialize()
        if mt5.login(login=settings.mt5_login, password=settings.mt5_password, server=settings.mt5_server):
            logger.info("Logged in to MetaTrader 5 successfully.")
        else:
            logger.error("Failed to log in to MetaTrader 5.")
            raise Exception("Failed to log in to MetaTrader 5.")

    def shutdown(self):
        if self.connected:
            mt5.shutdown()
            self.connected = False
            logger.info("MetaTrader 5 shut down successfully.")
        else:
            logger.warning("MetaTrader 5 was not connected.")

    def check_status(self):
        if self.connected:
            logger.info("MetaTrader 5 is connected.")
            return True
        else:
            logger.warning("MetaTrader 5 is not connected.")
            return False