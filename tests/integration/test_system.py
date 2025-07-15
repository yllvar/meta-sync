# tests/unit/test_symbol_service.py
import unittest
from unittest.mock import patch, MagicMock
from app.services.symbol_service import SymbolService
from app.core.logging import logger
from app.models.symbols import SymbolInfo, TickInfo

class TestSymbolService(unittest.TestCase):
    def setUp(self):
        self.mt5_conn = MagicMock()
        self.symbol_service = SymbolService(self.mt5_conn)

    @patch('MetaTrader5.symbols_total')
    def test_symbols_total(self, mock_symbols_total):
        mock_symbols_total.return_value = 100
        result = self.symbol_service.symbols_total()
        self.assertEqual(result, 100)
        mock_symbols_total.assert_called_once()

    @patch('MetaTrader5.symbols_get')
    def test_symbols_get(self, mock_symbols_get):
        mock_symbols_get.return_value = [
            {'name': 'EURUSD', 'path': 'path/to/EURUSD', 'description': 'Euro vs US Dollar'},
            {'name': 'GBPUSD', 'path': 'path/to/GBPUSD', 'description': 'British Pound vs US Dollar'}
        ]
        result = self.symbol_service.symbols_get()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]['name'], 'EURUSD')
        self.assertEqual(result[1]['name'], 'GBPUSD')
        mock_symbols_get.assert_called_once()

    @patch('MetaTrader5.symbol_info')
    def test_symbol_info(self, mock_symbol_info):
        mock_symbol_info.return_value = {
            'name': 'EURUSD',
            'path': 'path/to/EURUSD',
            'description': 'Euro vs US Dollar',
            'currency_base': 'EUR',
            'currency_profit': 'USD',
            'currency_margin': 'USD',
            'digits': 4,
            'spread': 10,
            'spread_float': 0.0010,
            'ticks_bookdepth': 10,
            'trade_calc_mode': 0,
            'trade_mode': 0,
            'start_time': 16167573,
            'expiration_time': 0,
            'trade_start': 16167573,
            'trade_end': 16167573,
            'min_lot': 0.01,
            'max_lot': 100.0,
            'lot_step': 0.01,
            'volume_min': 0.01,
            'volume_max': 100.0,
            'volume_step': 0.01,
            'volume_limit': 0.0,
            'swap_long': 0.0,
            'swap_short': 0.0,
            'swap_rollover3days': 0,
            'margin_initial': 100000.0,
            'margin_maintenance': 50000.0,
            'margin_hedged': 50000.0,
            'margin_long': 100000.0,
            'margin_short': 100000.0,
            'margin_limit': 0.0,
            'margin_stopout_initial': 50.0,
            'margin_stopout_maintenance': 30.0,
            'margin_stopout_hedged': 30.0,
            'session_hedged_margin': 50000.0,
            'price_limit_kind': 0,
            'price_limit_offset': 0.0,
            'price_freeze_level': 0,
            'trade_contract_size': 1.0,
            'trade_accrued_interest': 0.0,
            'trade_face_value': 0.0,
            'trade_liquidity_rate': 0.0,
            'trade_basis': 0.0,
            'trade_rebate': 0.0,
            'trade_commission_base': 0.0,
            'trade_commission_leg': 0.0,
            'trade_commission_point': 0.0,
            'trade_commission_mode': 0,
            'trade_options': 0,
            'trade_exec_mode': 0,
            'swap_mode': 0,
            'swap_rollover3days_mode': 0,
            'margin_flags': 0,
            'hedge_flags': 0,
            'trade_flags': 0,
            'flags': 0,
            'trade_mode3': 0,
            'filling_mode': 0,
            'order_mode': 0,
            'expiration_mode': 0,
            'swap_rollover_mode': 0,
            'swap_rollover_days': [],
            'margin_currency': 'USD',
            'margin_mode': 0,
            'margin_option': 0,
            'background_color': 0,
            'chart_mode': 0,
            'chart_mode_bars': 0,
            'chart_color_bg': 0,
            'chart_color_bg2': 0,
            'chart_color_bg3': 0,
            'chart_color_grid': 0,
            'chart_color_cross': 0,
            'chart_color_text': 0,
            'chart_color_candle_bull': 0,
            'chart_color_candle_bear': 0,
            'chart_color_candle_stable': 0,
            'chart_color_wick_stable': 0,
            'chart_scale_font': 0,
            'chart_scale_filter': 0,
            'chart_fixed_max': 0.0,
            'chart_fixed_min': 0.0,
            'chart_auto_scale': 0,
            'chart_price_max': 0.0,
            'chart_price_min': 0.0,
            'chart_price_fixed_max': 0.0,
            'chart_price_fixed_min': 0.0,
            'chart_price_min_deviation': 0.0,
            'chart_price_max_deviation': 0.0,
            'chart_fixed_max_deviation': 0.0,
            'chart_fixed_min_deviation': 0.0,
            'chart_auto_scale_deviation': 0,
            'chart_price_deviation': 0.0,
            'chart_price_deviation_in_pips': 0,
            'chart_price_deviation_in_percent': 0.0,
            'chart_price_deviation_in_points': 0,
            'chart_price_deviation_in_bars': 0,
            'chart_price_deviation_in_seconds': 0,
            'chart_price_deviation_in_minutes': 0,
            'chart_price_deviation_in_hours': 0,
            'chart_price_deviation_in_days': 0,
            'chart_price_deviation_in_weeks': 0,
            'chart_price_deviation_in_months': 0,
            'chart_price_deviation_in_years': 0,
            'chart_price_deviation_in_ticks': 0,
            'chart_price_deviation_in_volumes': 0,
            'chart_price_deviation_in_spreads': 0,
            'chart_price_deviation_in_averages': 0,
            'chart_price_deviation_in_ranges': 0,
            'chart_price_deviation_in_levels': 0,
            'chart_price_deviation_in_patterns': 0,
            'chart_price_deviation_in_indicators': 0,
            'chart_price_deviation_in_scripts': 0,
            'chart_price_deviation_in_functions': 0,
            'chart_price_deviation_in_events': 0,
            'chart_price_deviation_in_news': 0,
            'chart_price_deviation_in_alerts': 0,
            'chart_price_deviation_in_reports': 0,
            'chart_price_deviation_in_experts': 0,
            'chart_price_deviation_in_signals': 0,
            'chart_price_deviation_in_optimization': 0,
            'chart_price_deviation_in_backtesting': 0,
            'chart_price_deviation_in_strategy_testing': 0,
            'chart_price_deviation_in_visualization': 0,
            'chart_price_deviation_in_reporting': 0,
            'chart_price_deviation_in_analysis': 0,
            'chart_price_deviation_in_research': 0,
            'chart_price_deviation_in_development': 0,
            'chart_price_deviation_in_training': 0,
            'chart_price_deviation_in_simulation': 0,
            'chart_price_deviation_in_simulation_mode': 0,
            'chart_price_deviation_in_simulation_period': 0,
            'chart_price_deviation_in_simulation_data': 0,
            'chart_price_deviation_in_simulation_results': 0,
            'chart_price_deviation_in_simulation_statistics': 0,
            'chart_price_deviation_in_simulation_visualization': 0,
            'chart_price_deviation_in_simulation_reporting': 0,
            'chart_price_deviation_in_simulation_analysis': 0,
            'chart_price_deviation_in_simulation_research': 0,
            'chart_price_deviation_in_simulation_development': 0,
            'chart_price_deviation_in_simulation_training': 0,
            'chart_price_deviation_in_simulation_simulation': 0
        }
        result = self.symbol_service.symbol_info('EURUSD')
        self.assertEqual(result['name'], 'EURUSD')
        self.assertEqual(result['path'], 'path/to/EURUSD')
        self.assertEqual(result['description'], 'Euro vs US Dollar')
        mock_symbol_info.assert_called_once_with('EURUSD')

    @patch('MetaTrader5.symbol_info_tick')
    def test_symbol_info_tick(self, mock_symbol_info_tick):
        mock_symbol_info_tick.return_value = (
            1580209200, 1.10132, 1.10151, 0., 0, 1580209200067, 130, 0.
        )
        result = self.symbol_service.symbol_info_tick('EURUSD')
        self.assertEqual(result['time'], 1580209200)
        self.assertEqual(result['bid'], 1.10132)
        self.assertEqual(result['ask'], 1.10151)
        self.assertEqual(result['last'], 0.)
        self.assertEqual(result['volume'], 0)
        self.assertEqual(result['time_msc'], 1580209200067)
        self.assertEqual(result['flags'], 130)
        self.assertEqual(result['volume_real'], 0.)
        mock_symbol_info_tick.assert_called_once_with('EURUSD')

    @patch('MetaTrader5.symbol_info')
    def test_symbol_info_not_found(self, mock_symbol_info):
        mock_symbol_info.return_value = None
        with self.assertRaises(Exception) as context:
            self.symbol_service.symbol_info('UNKNOWN_SYMBOL')
        self.assertEqual(str(context.exception), "Symbol UNKNOWN_SYMBOL not found")
        mock_symbol_info.assert_called_once_with('UNKNOWN_SYMBOL')

    @patch('MetaTrader5.symbol_info_tick')
    def test_symbol_info_tick_not_found(self, mock_symbol_info_tick):
        mock_symbol_info_tick.return_value = None
        with self.assertRaises(Exception) as context:
            self.symbol_service.symbol_info_tick('UNKNOWN_SYMBOL')
        self.assertEqual(str(context.exception), "Tick for symbol UNKNOWN_SYMBOL not found")
        mock_symbol_info_tick.assert_called_once_with('UNKNOWN_SYMBOL')

if __name__ == '__main__':
    unittest.main()