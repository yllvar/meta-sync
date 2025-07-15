# tests/unit/test_mt5.py
from unittest.mock import patch
import MetaTrader5 as mt5
from app.core.mt5 import MT5Connection
from app.core.logging import logger

@patch('MetaTrader5.initialize')
@patch('MetaTrader5.login')
@patch('MetaTrader5.shutdown')
def test_mt5_connection(mock_shutdown, mock_login, mock_initialize):
    mt5_conn = MT5Connection()

    # Test initialize
    mock_initialize.return_value = True
    mt5_conn.initialize()
    mock_initialize.assert_called_once_with(
        path='C:\\Program Files\\MetaTrader 5\\terminal64.exe',
        login=123456789,
        password='your_password',
        server='MetaQuotes-Demo'
    )
    assert mt5_conn.connected is True

    # Test login
    mock_login.return_value = True
    mt5_conn.login()
    mock_login.assert_called_once_with(
        login=123456789,
        password='your_password',
        server='MetaQuotes-Demo'
    )

    # Test shutdown
    mt5_conn.shutdown()
    mock_shutdown.assert_called_once()
    assert mt5_conn.connected is False

    # Test check_status
    mt5_conn.initialize()
    assert mt5_conn.check_status() is True
    mt5_conn.shutdown()
    assert mt5_conn.check_status() is False