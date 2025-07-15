# tests/integration/test_symbols.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.dependencies.auth import verify_api_key
from app.dependencies.mt5 import get_mt5_connection

client = TestClient(app)

def test_get_symbols_total():
    response = client.get("/symbols/total", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    assert response.json() > 0

def test_get_symbols_get():
    response = client.get("/symbols/get", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    symbols = response.json()
    assert len(symbols) > 0

def test_get_symbol_info():
    response = client.get("/symbols/info?symbol=EURUSD", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    symbol_info = response.json()
    assert symbol_info['name'] == 'EURUSD'

def test_get_symbol_info_tick():
    response = client.get("/symbols/info_tick?symbol=EURUSD", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    tick_info = response.json()
    assert 'time' in tick_info
    assert 'bid' in tick_info
    assert 'ask' in tick_info