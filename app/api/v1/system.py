# app/api/v1/system.py
from fastapi import APIRouter, Depends, HTTPException
from app.services.system_service import SystemService
from app.models.system import TerminalInfo
from app.dependencies.mt5 import get_mt5_connection

router = APIRouter(prefix="/system", tags=["system"])

@router.get("/version", response_model=dict)
async def get_version(system_service: SystemService = Depends(SystemService)):
    try:
        return system_service.version()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/last_error", response_model=dict)
async def get_last_error(system_service: SystemService = Depends(SystemService)):
    try:
        return system_service.last_error()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/terminal_info", response_model=TerminalInfo)
async def get_terminal_info(system_service: SystemService = Depends(SystemService)):
    try:
        return system_service.terminal_info()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))