# app/services/system_service.py
from app.core.logging import logger

class SystemService:
    def __init__(self, mt5_conn):
        self.mt5_conn = mt5_conn

    def version(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        version = mt5.version()
        logger.info(f"MetaTrader 5 version: {version}")
        return version

    def last_error(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        error = mt5.last_error()
        logger.info(f"Last error: {error}")
        return error

    def terminal_info(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        info = mt5.terminal_info()
        logger.info(f"Terminal info: {info}")
        return info
