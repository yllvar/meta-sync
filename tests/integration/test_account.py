# tests/integration/test_account.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.dependencies.auth import verify_api_key
from app.dependencies.mt5 import get_mt5_connection

client = TestClient(app)

def test_get_account_info():
    response = client.get("/account/info", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    account_info = response.json()
    assert 'login' in account_info
    assert 'trade_mode' in account_info
    assert 'leverage' in account_info
    assert 'balance' in account_info
    assert 'equity' in account_info