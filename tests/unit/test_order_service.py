# tests/unit/test_order_service.py
import unittest
from unittest.mock import patch, MagicMock
from app.services.order_service import OrderService
from app.models.orders import OrderRequest
import MetaTrader5 as mt5

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.mt5_conn = MagicMock()
        self.account_service = MagicMock()
        self.symbol_service = MagicMock()
        self.order_service = OrderService(self.mt5_conn, self.account_service, self.symbol_service)

    @patch('MetaTrader5.orders_total')
    def test_orders_total(self, mock_orders_total):
        self.mt5_conn.check_status.return_value = True
        mock_orders_total.return_value = 5
        result = self.order_service.orders_total()
        self.assertEqual(result, 5)
        mock_orders_total.assert_called_once()

    @patch('MetaTrader5.orders_get')
    def test_orders_get(self, mock_orders_get):
        self.mt5_conn.check_status.return_value = True
        mock_order = MagicMock()
        mock_order._asdict.return_value = {'ticket': 123}
        mock_orders_get.return_value = [mock_order]
        result = self.order_service.orders_get()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['ticket'], 123)
        mock_orders_get.assert_called_once()

    @patch('MetaTrader5.order_check')
    def test_order_check(self, mock_order_check):
        self.mt5_conn.check_status.return_value = True
        mock_result = MagicMock()
        mock_result._asdict.return_value = {'retcode': 10009}
        mock_order_check.return_value = mock_result
        order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
        result = self.order_service.order_check(order_request.dict())
        self.assertEqual(result['retcode'], 10009)
        mock_order_check.assert_called_once()

    @patch('MetaTrader5.order_calc_margin')
    def test_order_calc_margin(self, mock_order_calc_margin):
        self.mt5_conn.check_status.return_value = True
        mock_order_calc_margin.return_value = 100.0
        order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
        result = self.order_service.order_calc_margin(order_request.dict())
        self.assertEqual(result, 100.0)
        mock_order_calc_margin.assert_called_once()

    @patch('MetaTrader5.order_calc_profit')
    def test_order_calc_profit(self, mock_order_calc_profit):
        self.mt5_conn.check_status.return_value = True
        mock_result = MagicMock()
        mock_result._asdict.return_value = {'profit': 10.0}
        mock_order_calc_profit.return_value = mock_result
        order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
        result = self.order_service.order_calc_profit(order_request.dict())
        self.assertEqual(result['profit'], 10.0)
        mock_order_calc_profit.assert_called_once()

    @patch('MetaTrader5.order_send')
    def test_order_send_success(self, mock_order_send):
        self.mt5_conn.check_status.return_value = True
        self.account_service.account_info.return_value = MagicMock(free_margin=200.0)
        self.symbol_service.symbol_info.return_value = MagicMock(trade_mode=mt5.SYMBOL_TRADE_MODE_FULL)
        self.order_service.order_calc_margin = MagicMock(return_value=100.0)

        mock_result = MagicMock()
        mock_result.retcode = mt5.TRADE_RETCODE_DONE
        mock_result._asdict.return_value = {'retcode': mt5.TRADE_RETCODE_DONE}
        mock_order_send.return_value = mock_result

        order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)
        
        result = self.order_service.order_send(order_request)

        self.assertEqual(result['retcode'], mt5.TRADE_RETCODE_DONE)
        self.account_service.account_info.assert_called_once()
        self.symbol_service.symbol_info.assert_called_once_with('EURUSD')
        self.order_service.order_calc_margin.assert_called_once()
        mock_order_send.assert_called_once()

    @patch('MetaTrader5.order_check')
    def test_order_send_dry_run(self, mock_order_check):
        self.mt5_conn.check_status.return_value = True
        self.account_service.account_info.return_value = MagicMock(free_margin=200.0)
        self.symbol_service.symbol_info.return_value = MagicMock(trade_mode=mt5.SYMBOL_TRADE_MODE_FULL)
        self.order_service.order_calc_margin = MagicMock(return_value=100.0)
        
        mock_result = MagicMock()
        mock_result._asdict.return_value = {'retcode': 10009}
        mock_order_check.return_value = mock_result

        order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0, dry_run=True)

        result = self.order_service.order_send(order_request)

        self.assertTrue(result['dry_run'])
        self.assertIn('check_result', result)
        mock_order_check.assert_called_once()

    def test_order_send_insufficient_margin(self):
        self.mt5_conn.check_status.return_value = True
        self.account_service.account_info.return_value = MagicMock(free_margin=50.0)
        self.order_service.order_calc_margin = MagicMock(return_value=100.0)

        order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)

        with self.assertRaisesRegex(Exception, "Insufficient margin for order"):
            self.order_service.order_send(order_request)

    def test_order_send_trading_disabled(self):
        self.mt5_conn.check_status.return_value = True
        self.account_service.account_info.return_value = MagicMock(free_margin=200.0)
        self.symbol_service.symbol_info.return_value = MagicMock(trade_mode=mt5.SYMBOL_TRADE_MODE_DISABLED)
        self.order_service.order_calc_margin = MagicMock(return_value=100.0)

        order_request = OrderRequest(action=0, symbol='EURUSD', volume=0.1, price=1.2, sl=1.1, tp=1.3, deviation=10, magic=123, comment='test', type_time=0, type_filling=0, expiration=0)

        with self.assertRaisesRegex(Exception, "Trading is disabled for symbol EURUSD"):
            self.order_service.order_send(order_request)

if __name__ == '__main__':
    unittest.main()
