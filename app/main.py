# app/main.py
from fastapi import FastAPI, Request, Depends
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.core.mt5 import MT5Connection
from app.core.logging import logger
from app.dependencies.auth import verify_api_key
from app.dependencies.mt5 import get_mt5_connection

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="MetaSync Solutions", description="API for interacting with MetaTrader 5", version="1.0.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

mt5_conn = MT5Connection()

@app.on_event("startup")
async def startup_event():
    try:
        mt5_conn.initialize()
        mt5_conn.login()
    except Exception as e:
        logger.error(f"Startup failed: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    mt5_conn.shutdown()

@app.middleware("http")
async def api_key_check(request: Request, call_next):
    await verify_api_key(request)
    response = await call_next(request)
    return response

@app.get("/ping", dependencies=[Depends(limiter.limit("10/minute"))])
async def ping(mt5_conn: MT5Connection = Depends(get_mt5_connection)):
    if mt5_conn.check_status():
        return {"status": "OK"}
    else:
        return {"status": "ERROR"}