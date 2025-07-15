# tests/unit/test_position_service.py
import unittest
from unittest.mock import patch, MagicMock
from app.services.position_service import PositionService
from app.core.logging import logger
from app.models.orders import OrderCheckResult

class TestPositionService(unittest.TestCase):
    def setUp(self):
        self.mt5_conn = MagicMock()
        self.position_service = PositionService(self.mt5_conn)

    @patch('MetaTrader5.positions_total')
    def test_positions_total(self, mock_positions_total):
        mock_positions_total.return_value = 3
        result = self.position_service.positions_total()
        self.assertEqual(result, 3)
        mock_positions_total.assert_called_once()

    @patch('MetaTrader5.positions_get')
    def test_positions_get(self, mock_positions_get):
        mock_positions_get.return_value = [
            MagicMock(
                ticket=123456,
                magic=1000,
                time_setup=16167573,
                time_expiration=0,
                type=0,
                type_time=0,
                type_filling=0,
                symbol='EURUSD',
                volume=0.1,
                price_open=1.10132,
                sl=1.10000,
                tp=1.10200,
                price_current=1.10151,
                price_stoplimit=0.0,
                deviation=10,
                stoploss=1.10000,
                takeprofit=1.10200,
                state=0,
                comment='Test Position',
                external_id=''
            ),
            MagicMock(
                ticket=123457,
                magic=1000,
                time_setup=16167574,
                time_expiration=0,
                type=0,
                type_time=0,
                type_filling=0,
                symbol='GBPUSD',
                volume=0.2,
                price_open=1.30132,
                sl=1.30000,
                tp=1.30200,
                price_current=1.30151,
                price_stoplimit=0.0,
                deviation=10,
                stoploss=1.30000,
                takeprofit=1.30200,
                state=0,
                comment='Test Position 2',
                external_id=''
            ),
            MagicMock(
                ticket=123458,
                magic=1000,
                time_setup=16167575,
                time_expiration=0,
                type=0,
                type_time=0,
                type_filling=0,
                symbol='EURCAD',
                volume=0.3,
                price_open=1.45321,
                sl=1.45000,
                tp=1.45500,
                price_current=1.45301,
                price_stoplimit=0.0,
                deviation=10,
                stoploss=1.45000,
                takeprofit=1.45500,
                state=0,
                comment='Test Position 3',
                external_id=''
            )
        ]
        result = self.position_service.positions_get()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]['ticket'], 123456)
        self.assertEqual(result[1]['ticket'], 123457)
        self.assertEqual(result[2]['ticket'], 123458)
        mock_positions_get.assert_called_once()