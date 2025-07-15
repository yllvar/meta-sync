# app/services/order_service.py
from app.core.logging import logger
from app.models.orders import OrderRequest, OrderResponse
from app.services.account_service import AccountService
from app.services.symbol_service import SymbolService
from datetime import datetime
import pytz

class OrderService:
    def __init__(self, mt5_conn, account_service: "AccountService", symbol_service: "SymbolService"):
        self.mt5_conn = mt5_conn
        self.account_service = account_service
        self.symbol_service = symbol_service

    def orders_total(self):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        total = mt5.orders_total()
        logger.info(f"Total orders: {total}")
        return total

    def orders_get(self, filter=None):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        orders = mt5.orders_get(filter=filter)
        logger.info(f"Orders retrieved: {len(orders)}")
        return [order._asdict() for order in orders]

    def order_check(self, order_request):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        result = mt5.order_check(order_request)
        logger.info(f"Order check result: {result}")
        return result._asdict()

    def order_calc_margin(self, order_request):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        margin = mt5.order_calc_margin(order_request)
        logger.info(f"Order calc margin result: {margin}")
        return margin

    def order_calc_profit(self, order_request):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")
        profit = mt5.order_calc_profit(order_request)
        logger.info(f"Order calc profit result: {profit}")
        return profit

    def order_send(self, order_request: OrderRequest):
        import MetaTrader5 as mt5
        if not self.mt5_conn.check_status():
            logger.error("MetaTrader 5 is not connected.")
            raise Exception("MetaTrader 5 is not connected.")

        # Validate margin availability
        margin_required = self.order_calc_margin(order_request.dict(exclude={'dry_run'}))
        account_info = self.account_service.account_info()
        if account_info.free_margin < margin_required:
            logger.error(f"Insufficient margin for order: {order_request}")
            raise Exception("Insufficient margin for order")

        # Validate trading hours
        symbol_info = self.symbol_service.symbol_info(order_request.symbol)
        if symbol_info.trade_mode == mt5.SYMBOL_TRADE_MODE_DISABLED:
            logger.error(f"Trading is disabled for symbol {order_request.symbol}")
            raise Exception(f"Trading is disabled for symbol {order_request.symbol}")

        # Convert OrderRequest to dict for mt5.order_send
        order_dict = order_request.dict(exclude={'dry_run'})


        # Send order
        if order_request.dry_run:
            logger.info(f"Dry run order: {order_request}")
            # In a dry run, we can still check the order without sending it
            check_result = mt5.order_check(order_dict)
            return {"dry_run": True, "order_request": order_request.dict(), "check_result": check_result._asdict()}

        result = mt5.order_send(order_dict)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Order send failed: {result.comment}")
            raise Exception(f"Order send failed: {result.comment}")

        logger.info(f"Order sent successfully: {result}")
        return result._asdict()
