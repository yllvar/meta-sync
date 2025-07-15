# tests/integration/test_positions.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.dependencies.auth import verify_api_key
from app.dependencies.mt5 import get_mt5_connection

client = TestClient(app)

def test_get_positions_total():
    response = client.get("/positions/total", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    total = response.json()
    assert isinstance(total, int)

def test_get_positions_get():
    response = client.get("/positions/get", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    positions = response.json()
    assert isinstance(positions, list)