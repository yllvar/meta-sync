# app/api/v1/positions.py
from fastapi import APIRouter, Depends, HTTPException
from app.services.position_service import PositionService
from app.models.orders import OrderCheckResult
from app.dependencies.mt5 import get_mt5_connection

router = APIRouter(prefix="/positions", tags=["positions"])

@router.get("/total", response_model=int)
async def get_positions_total(position_service: PositionService = Depends(lambda: PositionService(Depends(get_mt5_connection)))):
    try:
        return position_service.positions_total()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get", response_model=list[OrderCheckResult])
async def get_positions_get(position_service: PositionService = Depends(lambda: PositionService(Depends(get_mt5_connection)))):
    try:
        positions = position_service.positions_get()
        return positions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))