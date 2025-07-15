# tests/unit/test_history_service.py
import unittest
from unittest.mock import patch, MagicMock
from app.services.history_service import HistoryService
from app.core.logging import logger
from app.models.history import HistoricalBar, HistoricalTick
from datetime import datetime
import pytz

class TestHistoryService(unittest.TestCase):
    def setUp(self):
        self.mt5_conn = MagicMock()
        self.history_service = HistoryService(self.mt5_conn)

    @patch('MetaTrader5.copy_rates_from')
    def test_copy_rates_from(self, mock_copy_rates_from):
        mock_copy_rates_from.return_value = [
            MagicMock(
                time=1580149260,
                open=1.10132,
                high=1.10151,
                low=1.10131,
                close=1.10149,
                tick_volume=44,
                spread=1,
                real_volume=0
            ),
            MagicMock(
                time=1580149320,
                open=1.10149,
                high=1.10161,
                low=1.10143,
                close=1.10154,
                tick_volume=42,
                spread=1,
                real_volume=0
            )
        ]
        date_from = pytz.utc.localize(datetime(2020, 1, 29, 12, 1, 0))
        result = self.history_service.copy_rates_from('EURUSD', mt5.TIMEFRAME_M1, date_from, 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['time'], 1580149260)
        self.assertEqual(result[1]['time'], 1580149320)
        mock_copy_rates_from.assert_called_once_with('EURUSD', mt5.TIMEFRAME_M1, date_from, 2)

    @patch('MetaTrader5.copy_rates_from_pos')
    def test_copy_rates_from_pos(self, mock_copy_rates_from_pos):
        mock_copy_rates_from_pos.return_value = [
            MagicMock(
                time=1580149260,
                open=1.10132,
                high=1.10151,
                low=1.10131,
                close=1.10149,
                tick_volume=44,
                spread=1,
                real_volume=0
            ),
            MagicMock(
                time=1580149320,
                open=1.10149,
                high=1.10161,
                low=1.10143,
                close=1.10154,
                tick_volume=42,
                spread=1,
                real_volume=0
            )
        ]
        result = self.history_service.copy_rates_from_pos('EURUSD', mt5.TIMEFRAME_M1, 0, 2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['time'], 1580149260)
        self.assertEqual(result[1]['time'], 1580149320)
        mock_copy_rates_from_pos.assert_called_once_with('EURUSD', mt5.TIMEFRAME_M1, 0, 2)

    @patch('MetaTrader5.copy_rates_range')
    def test_copy_rates_range(self, mock_copy_rates_range):
        mock_copy_rates_range.return_value = [
            MagicMock(
                time=1580149260,
                open=1.10132,
                high=1.10151,
                low=1.10131,
                close=1.10149,
                tick_volume=44,
                spread=1,
                real_volume=0
            ),
            MagicMock(
                time=1580149320,
                open=1.10149,
                high=1.10161,
                low=1.10143,
                close=1.10154,
                tick_volume=42,
                spread=1,
                real_volume=0
            )
        ]
        date_from = pytz.utc.localize(datetime(2020, 1, 29, 12, 1, 0))
        date_to = pytz.utc.localize(datetime(2020, 1, 29, 12, 2, 0))
        result = self.history_service.copy_rates_range('EURUSD', mt5.TIMEFRAME_M1, date_from, date_to)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['time'], 1580149260)
        self.assertEqual(result[1]['time'], 1580149320)
        mock_copy_rates_range.assert_called_once_with('EURUSD', mt5.TIMEFRAME_M1, date_from, date_to)

    @patch('MetaTrader5.copy_ticks_from')
    def test_copy_ticks_from(self, mock_copy_ticks_from):
        mock_copy_ticks_from.return_value = [
            MagicMock(
                time=1580209200,
                bid=1.10132,
                ask=1.10151,
                last=0.,
                volume=0,
                time_msc=1580209200067,
                flags=130,
                volume_real=0.
            ),
            MagicMock(
                time=1580209260,
                bid=1.10149,
                ask=1.10161,
                last=0.,
                volume=0,
                time_msc=1580209260785,
                flags=130,
                volume_real=0.
            )
        ]
        date_from = pytz.utc.localize(datetime(2020, 1, 31, 12, 0, 0))
        result = self.history_service.copy_ticks_from('EURUSD', date_from, mt5.COPY_TICKS_ALL)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['time'], 1580209200)
        self.assertEqual(result[1]['time'], 1580209260)
        mock_copy_ticks_from.assert_called_once_with('EURUSD', date_from, mt5.COPY_TICKS_ALL)

    @patch('MetaTrader5.copy_ticks_range')
    def test_copy_ticks_range(self, mock_copy_ticks_range):
        mock_copy_ticks_range.return_value = [
            MagicMock(
                time=1580209200,
                bid=1.10132,
                ask=1.10151,
                last=0.,
                volume=0,
                time_msc=1580209200067,
                flags=130,
                volume_real=0.
            ),
            MagicMock(
                time=1580209260,
                bid=1.10149,
                ask=1.10161,
                last=0.,
                volume=0,
                time_msc=1580209260785,
                flags=130,
                volume_real=0.
            )
        ]
        date_from = pytz.utc.localize(datetime(2020, 1, 31, 12, 0, 0))
        date_to = pytz.utc.localize(datetime(2020, 1, 31, 12, 1, 0))
        result = self.history_service.copy_ticks_range('EURUSD', date_from, date_to, mt5.COPY_TICKS_ALL)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['time'], 1580209200)
        self.assertEqual(result[1]['time'], 1580209260)
        mock_copy_ticks_range.assert_called_once_with('EURUSD', date_from, date_to, mt5.COPY_TICKS_ALL)