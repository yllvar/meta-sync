# app/services/symbol_service.py
from app.core.logging import logger

class SymbolService:
    def __init__(self, mt5_conn):
        self.mt5_conn = mt5_conn

    def symbols_total(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        total = mt5.symbols_total()
        logger.info(f"Total symbols: {total}")
        return total

    def symbols_get(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        symbols = mt5.symbols_get()
        logger.info(f"Symbols retrieved: {len(symbols)}")
        return symbols

    def symbol_info(self, symbol):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        info = mt5.symbol_info(symbol)
        logger.info(f"Symbol info retrieved for {symbol}: {info}")
        return info

    def symbol_info_tick(self, symbol):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        tick = mt5.symbol_info_tick(symbol)
        logger.info(f"Symbol tick retrieved for {symbol}: {tick}")
        return tick
