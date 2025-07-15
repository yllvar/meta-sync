# app/services/position_service.py
from app.core.logging import logger

class PositionService:
    def __init__(self, mt5_conn):
        self.mt5_conn = mt5_conn

    def positions_total(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        total = mt5.positions_total()
        logger.info(f"Total positions: {total}")
        return total

    def positions_get(self, filter=None):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        positions = mt5.positions_get(filter=filter)
        logger.info(f"Positions retrieved: {len(positions)}")
        return [position._asdict() for position in positions]
