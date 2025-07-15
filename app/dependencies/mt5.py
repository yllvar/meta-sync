# app/dependencies/mt5.py
import MetaTrader5 as mt5
from app.core.config import settings
from app.core.logging import logger
from app.services.mt5_service import MT5Service

_mt5_service = MT5Service()

def get_mt5_connection():
    try:
        _mt5_service.initialize()
        _mt5_service.login()
        return _mt5_service
    except Exception as e:
        logger.error(f"Failed to connect to MetaTrader 5: {e}")
        raise e

def get_account_service(mt5_conn=Depends(get_mt5_connection)):
    return AccountService(mt5_conn)

def get_symbol_service(mt5_conn=Depends(get_mt5_connection)):
    return SymbolService(mt5_conn)

def get_order_service(mt5_conn=Depends(get_mt5_connection),
                      account_service=Depends(get_account_service),
                      symbol_service=Depends(get_symbol_service)):
    return OrderService(mt5_conn, account_service, symbol_service)