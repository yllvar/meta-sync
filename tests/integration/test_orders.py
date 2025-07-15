# tests/integration/test_orders.py
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from app.models.orders import OrderRequest
from unittest.mock import patch, MagicMock
import MetaTrader5 as mt5

client = TestClient(app)

def test_get_orders_total_unauthorized():
    response = client.get("/orders/total")
    assert response.status_code == 401

def test_get_orders_total():
    with patch('MetaTrader5.orders_total', return_value=5):
        response = client.get("/orders/total", headers={"X-API-Key": settings.api_key})
        assert response.status_code == 200
        assert response.json() == 5

def test_get_orders_get():
    with patch('MetaTrader5.orders_get', return_value=[MagicMock(_asdict=lambda: {'ticket': 123})]):
        response = client.get("/orders/get", headers={"X-API-Key": settings.api_key})
        assert response.status_code == 200
        assert response.json() == [{'ticket': 123}]

@patch('app.services.order_service.OrderService.order_check')
def test_post_order_check(mock_order_check):
    mock_order_check.return_value = {'retcode': 10009}
    order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
    response = client.post("/orders/check", json=order_request.dict(), headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    assert response.json() == {'retcode': 10009}

@patch('app.services.order_service.OrderService.order_calc_margin')
def test_post_order_calc_margin(mock_order_calc_margin):
    mock_order_calc_margin.return_value = 100.0
    order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
    response = client.post("/orders/calc_margin", json=order_request.dict(), headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    assert response.json() == 100.0

@patch('app.services.order_service.OrderService.order_calc_profit')
def test_post_order_calc_profit(mock_order_calc_profit):
    mock_order_calc_profit.return_value = {'profit': 10.0}
    order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
    response = client.post("/orders/calc_profit", json=order_request.dict(), headers={"X-API-Key": settings.api_key})
    assert response.status_code == 200
    assert response.json() == {'profit': 10.0}

@patch('app.services.order_service.OrderService.order_send')
def test_post_order_send(mock_order_send):
    mock_result = MagicMock()
    mock_result.retcode = mt5.TRADE_RETCODE_DONE
    mock_result._asdict.return_value = {'retcode': mt5.TRADE_RETCODE_DONE}
    mock_order_send.return_value = mock_result._asdict()
    
    order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
    
    response = client.post("/orders/send", json=order_request.dict(), headers={"X-API-Key": settings.api_key})
    
    assert response.status_code == 200
    assert response.json()['retcode'] == mt5.TRADE_RETCODE_DONE
    mock_order_send.assert_called_once()

@patch('app.services.order_service.OrderService.order_send')
def test_post_order_send_dry_run(mock_order_send):
    mock_order_send.return_value = {"dry_run": True, "order_request": {}, "check_result": {}}
    order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0, dry_run=True)
    
    response = client.post("/orders/send", json=order_request.dict(), headers={"X-API-Key": settings.api_key})
    
    assert response.status_code == 200
    assert response.json()['dry_run'] is True
    mock_order_send.assert_called_once()

@patch('app.services.order_service.OrderService.order_send', side_effect=Exception("Insufficient margin for order"))
def test_post_order_send_insufficient_margin(mock_order_send):
    order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
    
    response = client.post("/orders/send", json=order_request.dict(), headers={"X-API-Key": settings.api_key})
    
    assert response.status_code == 500
    assert response.json()['detail'] == "Insufficient margin for order"

@patch('app.services.order_service.OrderService.order_send', side_effect=Exception("Trading is disabled for symbol EURUSD"))
def test_post_order_send_trading_disabled(mock_order_send):
    order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
    
    response = client.post("/orders/send", json=order_request.dict(), headers={"X-API-Key": settings.api_key})
    
    assert response.status_code == 500
    assert response.json()['detail'] == "Trading is disabled for symbol EURUSD"
