# tests/unit/test_dependencies.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.dependencies.auth import verify_api_key
from app.dependencies.mt5 import get_mt5_connection
from unittest.mock import patch

client = TestClient(app)

def test_verify_api_key():
    request = client.get("/ping", headers={"X-API-Key": settings.api_key})
    assert request.status_code == 200

    request = client.get("/ping", headers={"X-API-Key": "invalid_key"})
    assert request.status_code == 401

@patch('app.dependencies.mt5.MT5Connection')
def test_get_mt5_connection(mock_mt5):
    mock_instance = mock_mt5.return_value
    mock_instance.initialize.return_value = True
    mock_instance.login.return_value = True
    mock_instance.check_status.return_value = True

    mt5_conn = get_mt5_connection()
    assert mt5_conn.check_status() is True

    mock_instance.initialize.return_value = False
    try:
        get_mt5_connection()
    except Exception as e:
        assert str(e) == "Failed to connect to MetaTrader 5"