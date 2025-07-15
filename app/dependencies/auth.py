# app/dependencies/auth.py
from fastapi import Depends, HTTPException, Request
from app.core.config import settings
from app.core.logging import logger

def verify_api_key(request: Request):
    api_key = request.headers.get("X-API-Key")
    if not api_key or api_key != settings.api_key:
        logger.error("Unauthorized access attempt")
        raise HTTPException(status_code=401, detail="Unauthorized")
    return True