# app/services/history_service.py
from app.core.logging import logger
from datetime import datetime
import pytz

class HistoryService:
    def __init__(self, mt5_conn):
        self.mt5_conn = mt5_conn

    def copy_rates_from(self, symbol, timeframe, date_from, count):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        rates = mt5.copy_rates_from(symbol, timeframe, date_from, count)
        if not rates:
            logger.error(f"No rates found for symbol {symbol} from {date_from} with count {count}")
            raise Exception(f"No rates found for symbol {symbol} from {date_from} with count {count}")
        logger.info(f"Rates retrieved for symbol {symbol}: {len(rates)}")
        return [rate._asdict() for rate in rates]

    def copy_rates_from_pos(self, symbol, timeframe, pos, count):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        rates = mt5.copy_rates_from_pos(symbol, timeframe, pos, count)
        if not rates:
            logger.error(f"No rates found for symbol {symbol} from position {pos} with count {count}")
            raise Exception(f"No rates found for symbol {symbol} from position {pos} with count {count}")
        logger.info(f"Rates retrieved for symbol {symbol}: {len(rates)}")
        return [rate._asdict() for rate in rates]

    def copy_rates_range(self, symbol, timeframe, date_from, date_to):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        rates = mt5.copy_rates_range(symbol, timeframe, date_from, date_to)
        if not rates:
            logger.error(f"No rates found for symbol {symbol} from {date_from} to {date_to}")
            raise Exception(f"No rates found for symbol {symbol} from {date_from} to {date_to}")
        logger.info(f"Rates retrieved for symbol {symbol}: {len(rates)}")
        return [rate._asdict() for rate in rates]

    def copy_ticks_from(self, symbol, date_from, flags):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        ticks = mt5.copy_ticks_from(symbol, date_from, flags)
        if not ticks:
            logger.error(f"No ticks found for symbol {symbol} from {date_from} with flags {flags}")
            raise Exception(f"No ticks found for symbol {symbol} from {date_from} with flags {flags}")
        logger.info(f"Ticks retrieved for symbol {symbol}: {len(ticks)}")
        return [tick._asdict() for tick in ticks]

    def copy_ticks_range(self, symbol, date_from, date_to, flags):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        ticks = mt5.copy_ticks_range(symbol, date_from, date_to, flags)
        if not ticks:
            logger.error(f"No ticks found for symbol {symbol} from {date_from} to {date_to} with flags {flags}")
            raise Exception(f"No ticks found for symbol {symbol} from {date_from} to {date_to} with flags {flags}")
        logger.info(f"Ticks retrieved for symbol {symbol}: {len(ticks)}")
        return [tick._asdict() for tick in ticks]
