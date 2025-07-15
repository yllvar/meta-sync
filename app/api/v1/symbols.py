# app/api/v1/symbols.py
from fastapi import APIRouter, Depends, HTTPException
from app.services.symbol_service import SymbolService
from app.models.symbols import SymbolInfo, TickInfo
from app.dependencies.mt5 import get_mt5_connection

router = APIRouter(prefix="/symbols", tags=["symbols"])

@router.get("/total", response_model=int)
async def get_symbols_total(symbol_service: SymbolService = Depends(SymbolService)):
    try:
        return symbol_service.symbols_total()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get", response_model=list[SymbolInfo])
async def get_symbols_get(symbol_service: SymbolService = Depends(SymbolService)):
    try:
        symbols = symbol_service.symbols_get()
        return symbols
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/info", response_model=SymbolInfo)
async def get_symbol_info(symbol: str, symbol_service: SymbolService = Depends(SymbolService)):
    try:
        info = symbol_service.symbol_info(symbol)
        if not info:
            raise HTTPException(status_code=404, detail=f"Symbol {symbol} not found")
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/info_tick", response_model=TickInfo)
async def get_symbol_info_tick(symbol: str, symbol_service: SymbolService = Depends(SymbolService)):
    try:
        tick = symbol_service.symbol_info_tick(symbol)
        if not tick:
            raise HTTPException(status_code=404, detail=f"Tick for symbol {symbol} not found")
        return tick
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))