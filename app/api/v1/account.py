# app/api/v1/account.py
from fastapi import APIRouter, Depends, HTTPException
from app.services.account_service import AccountService
from app.models.account import AccountInfo
from app.dependencies.mt5 import get_mt5_connection

router = APIRouter(prefix="/account", tags=["account"])

@router.get("/info", response_model=AccountInfo)
async def get_account_info(account_service: AccountService = Depends(lambda: AccountService(Depends(get_mt5_connection)))):
    try:
        info = account_service.account_info()
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))