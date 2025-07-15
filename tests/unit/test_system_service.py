# tests/unit/test_system_service.py
from unittest.mock import patch
from app.services.system_service import SystemService
from app.core.logging import logger

@patch('MetaTrader5.version')
@patch('MetaTrader5.last_error')
@patch('MetaTrader5.terminal_info')
def test_system_service(mock_info, mock_error, mock_version):
    mock_version.return_value = (2, 'MetaQuotes-Demo', '16167573')
    mock_error.return_value = (500, 2325, '19 Feb 2020')
    mock_info.return_value = {
        'community_balance': 0.0,
        'community_total': 0.0,
        'company': 'MetaQuotes Software Corp.',
        'name': 'MetaTrader 5',
        'path': 'C:\\Program Files\\MetaTrader 5\\terminal64.exe',
        'data_path': 'C:\\Users\\User\\AppData\\Roaming\\MetaQuotes\\Terminal\\123456789\\Tester\\Files',
        'commondata_path': 'C:\\Program Files\\MetaTrader 5\\common',
        'language': 'English',
        'is_demo': True,
        'connected': True,
        'trade_allowed': True,
        'trade_expert': True,
        'trade_automation': True,
        'margin_mode': 0,
        'leverage': 100,
        'balance': 10000.0,
        'credit': 0.0,
        'profit': 0.0,
        'equity': 10000.0,
        'margin': 0.0,
        'free_margin': 10000.0,
        'margin_level': 0.0,
        'margin_so_mode': False,
        'margin_so_call': 30.0,
        'margin_so_covered': 10.0,
        'server': 'MetaQuotes-Demo',
        'trade_server': 'MetaQuotes-Demo',
        'connected_to': 'MetaQuotes-Demo',
        'time_zone': 'GMT+0',
        'time_synchronization': True,
        'dlls_allowed': True,
        'trade_api': True,
        'email_enabled': True,
        'ftp_enabled': True,
        'notifications_enabled': True,
        'trade_contexts_allowed': 1,
        'max_symbols': 1000,
        'currency': 'USD',
        'codepage': 1252,
        'digits': 4,
        'stop_level': 10,
        'free_margin_mode': True,
        'margin_mode_flags': 0
    }

    system_service = SystemService(None)

    version = system_service.version()
    assert version == (2, 'MetaQuotes-Demo', '16167573')

    error = system_service.last_error()
    assert error == (500, 2325, '19 Feb 2020')

    info = system_service.terminal_info()
    assert info.community_balance == 0.0
    assert info.community_total == 0.0
    assert info.company == 'MetaQuotes Software Corp.'
    assert info.name == 'MetaTrader 5'
    assert info.path == 'C:\\Program Files\\MetaTrader 5\\terminal64.exe'
    assert info.data_path == 'C:\\Users\\User\\AppData\\Roaming\\MetaQuotes\\Terminal\\123456789\\Tester\\Files'
    assert info.commondata_path == 'C:\\Program Files\\MetaTrader 5\\common'
    assert info.language == 'English'
    assert info.is_demo == True
    assert info.connected == True
    assert info.trade_allowed == True
    assert info.trade_expert == True
    assert info.trade_automation == True
    assert info.margin_mode == 0
    assert info.leverage == 100
    assert info.balance == 10000.0
    assert info.credit == 0.0
    assert info.profit == 0.0
    assert info.equity == 10000.0
    assert info.margin == 0.0
    assert info.free_margin == 10000.0
    assert info.margin_level == 0.0
    assert info.margin_so_mode == False
    assert info.margin_so_call == 30.0
    assert info.margin_so_covered == 10.0
    assert info.server == 'MetaQuotes-Demo'
    assert info.trade_server == 'MetaQuotes-Demo'
    assert info.connected_to == 'MetaQuotes-Demo'
    assert info.time_zone == 'GMT+0'
    assert info.time_synchronization == True
    assert info.dlls_allowed == True
    assert info.trade_api == True
    assert info.email_enabled == True
    assert info.ftp_enabled == True
    assert info.notifications_enabled == True
    assert info.trade_contexts_allowed == 1
    assert info.max_symbols == 1000
    assert info.currency == 'USD'
    assert info.codepage == 1252
    assert info.digits == 4
    assert info.stop_level == 10
    assert info.free_margin_mode == True
    assert info.margin_mode_flags == 0