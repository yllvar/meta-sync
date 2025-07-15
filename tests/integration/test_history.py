# tests/integration/test_history.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.dependencies.auth import verify_api_key
from app.dependencies.mt5 import get_mt5_connection
from datetime import datetime
import pytz

client = TestClient(app)

def test_get_copy_rates_from():
    date_from = pytz.utc.localize(datetime(2020, 1, 29, 12, 1, 0)).isoformat()
    response = client.get(f"/history/copy_rates_from?symbol=EURUSD&timeframe={mt5.TIMEFRAME_M1}&date_from={date_from}&count=2", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    rates = response.json()
    assert len(rates) == 2
    assert 'time' in rates[0]
    assert 'open' in rates[0]
    assert 'high' in rates[0]
    assert 'low' in rates[0]
    assert 'close' in rates[0]
    assert 'tick_volume' in rates[0]
    assert 'spread' in rates[0]
    assert 'real_volume' in rates[0]

def test_get_copy_rates_from_pos():
    response = client.get(f"/history/copy_rates_from_pos?symbol=EURUSD&timeframe={mt5.TIMEFRAME_M1}&pos=0&count=2", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    rates = response.json()
    assert len(rates) == 2
    assert 'time' in rates[0]
    assert 'open' in rates[0]
    assert 'high' in rates[0]
    assert 'low' in rates[0]
    assert 'close' in rates[0]
    assert 'tick_volume' in rates[0]
    assert 'spread' in rates[0]
    assert 'real_volume' in rates[0]

def test_get_copy_rates_range():
    date_from = pytz.utc.localize(datetime(2020, 1, 29, 12, 1, 0)).isoformat()
    date_to = pytz.utc.localize(datetime(2020, 1, 29, 12, 2, 0)).isoformat()
    response = client.get(f"/history/copy_rates_range?symbol=EURUSD&timeframe={mt5.TIMEFRAME_M1}&date_from={date_from}&date_to={date_to}", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    rates = response.json()
    assert len(rates) == 2
    assert 'time' in rates[0]
    assert 'open' in rates[0]
    assert 'high' in rates[0]
    assert 'low' in rates[0]
    assert 'close' in rates[0]
    assert 'tick_volume' in rates[0]
    assert 'spread' in rates[0]
    assert 'real_volume' in rates[0]

def test_get_copy_ticks_from():
    date_from = pytz.utc.localize(datetime(2020, 1, 31, 12, 0, 0)).isoformat()
    response = client.get(f"/history/copy_ticks_from?symbol=EURUSD&date_from={date_from}&flags={mt5.COPY_TICKS_ALL}", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    ticks = response.json()
    assert len(ticks) > 0
    assert 'time' in ticks[0]
    assert 'bid' in ticks[0]
    assert 'ask' in ticks[0]
    assert 'last' in ticks[0]
    assert 'volume' in ticks[0]
    assert 'time_msc' in ticks[0]
    assert 'flags' in ticks[0]
    assert 'volume_real' in ticks[0]

def test_get_copy_ticks_range():
    date_from = pytz.utc.localize(datetime(2020, 1, 31, 12, 0, 0)).isoformat()
    date_to = pytz.utc.localize(datetime(2020, 1, 31, 12, 1, 0)).isoformat()
    response = client.get(f"/history/copy_ticks_range?symbol=EURUSD&date_from={date_from}&date_to={date_to}&flags={mt5.COPY_TICKS_ALL}", headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    ticks = response.json()
    assert len(ticks) > 0
    assert 'time' in ticks[0]
    assert 'bid' in ticks[0]
    assert 'ask' in ticks[0]
    assert 'last' in ticks[0]
    assert 'volume' in ticks[0]
    assert 'time_msc' in ticks[0]
    assert 'flags' in ticks[0]
    assert 'volume_real' in ticks[0]