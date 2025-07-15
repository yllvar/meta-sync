# app/services/account_service.py
from app.core.logging import logger

class AccountService:
    def __init__(self, mt5_conn):
        self.mt5_conn = mt5_conn

    def account_info(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        info = mt5.account_info()
        if not info:
            logger.error("Account info not found")
            raise Exception("Account info not found")
        logger.info(f"Account info retrieved: {info}")
        return info._asdict()
