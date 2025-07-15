# tests/unit/test_account_service.py
import unittest
from unittest.mock import patch, MagicMock
from app.services.account_service import AccountService
from app.core.logging import logger
from app.models.account import AccountInfo

class TestAccountService(unittest.TestCase):
    def setUp(self):
        self.mt5_conn = MagicMock()
        self.account_service = AccountService(self.mt5_conn)

    @patch('MetaTrader5.account_info')
    def test_account_info(self, mock_account_info):
        mock_account_info.return_value = MagicMock(
            login=123456789,
            trade_mode=0,
            leverage=100,
            balance=10000.0,
            credit=0.0,
            profit=0.0,
            equity=10000.0,
            margin=0.0,
            free_margin=10000.0,
            margin_level=0.0,
            margin_so_call=30.0,
            margin_so_mode=False,
            margin_so_covered=10.0,
            margin_mode=0,
            margin_currency='USD',
            server='MetaQuotes-Demo',
            company='MetaQuotes Software Corp.',
            name='MetaTrader 5',
            currency='USD',
            currency_digits=4,
            assets=0.0,
            liabilities=0.0,
            commission_blocked=0.0,
            margin_blocked=0.0,
            swap_blocked=0.0,
            profit_blocked=0.0,
            taxes_blocked=0.0,
            withdraw_blocked=0.0,
            acc_type=0,
            limit_orders=0,
            margin_hedged=0.0,
            trade_expert=True,
            trade_automation=True,
            margin_free_mode=True,
            margin_mode_flags=0
        )
        result = self.account_service.account_info()
        self.assertEqual(result['login'], 123456789)
        self.assertEqual(result['trade_mode'], 0)
        self.assertEqual(result['leverage'], 100)
        self.assertEqual(result['balance'], 10000.0)
        mock_account_info.assert_called_once()