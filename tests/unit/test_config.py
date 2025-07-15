# tests/unit/test_config.py
from app.core.config import settings

def test_config_values():
    assert settings.mt5_login == 123456789
    assert settings.mt5_password == "your_password"
    assert settings.mt5_server == "MetaQuotes-Demo"
    assert settings.mt5_path == "C:\\Program Files\\MetaTrader 5\\terminal64.exe"
    assert settings.api_key == "your_api_key_here"
    assert settings.log_level == "INFO"