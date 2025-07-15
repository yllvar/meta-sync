# app/api/v1/orders.py
from fastapi import APIRouter, Depends, HTTPException, Body, Query
from app.services.order_service import OrderService
from app.models.orders import OrderRequest, OrderResponse
from app.dependencies.mt5 import get_mt5_connection
from app.services.account_service import AccountService
from app.services.symbol_service import SymbolService

router = APIRouter(prefix="/orders", tags=["orders"])

def get_order_service(mt5_conn=Depends(get_mt5_connection),
                      account_service: AccountService = Depends(),
                      symbol_service: SymbolService = Depends()):
    return OrderService(mt5_conn, account_service, symbol_service)

@router.get("/total", response_model=int)
async def get_orders_total(order_service: OrderService = Depends(get_order_service)):
    try:
        return order_service.orders_total()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get", response_model=list[OrderResponse])
async def get_orders_get(order_service: OrderService = Depends(get_order_service)):
    try:
        orders = order_service.orders_get()
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/check", response_model=OrderResponse)
async def post_order_check(order_request: OrderRequest = Body(...), order_service: OrderService = Depends(get_order_service)):
    try:
        result = order_service.order_check(order_request.dict(exclude={'dry_run'}))
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/calc_margin", response_model=float)
async def post_order_calc_margin(order_request: OrderRequest = Body(...), order_service: OrderService = Depends(get_order_service)):
    try:
        margin = order_service.order_calc_margin(order_request.dict(exclude={'dry_run'}))
        return margin
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/calc_profit", response_model=OrderResponse)
async def post_order_calc_profit(order_request: OrderRequest = Body(...), order_service: OrderService = Depends(get_order_service)):
    try:
        profit = order_service.order_calc_profit(order_request.dict(exclude={'dry_run'}))
        return profit
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/send", response_model=OrderResponse)
async def post_order_send(order_request: OrderRequest = Body(...), order_service: OrderService = Depends(get_order_service)):
    try:
        result = order_service.order_send(order_request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
