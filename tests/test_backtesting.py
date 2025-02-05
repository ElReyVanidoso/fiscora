import unittest
import pandas as pd
from backtesting.engine import BacktestEngine
from backtesting.portfolio import Portfolio
from strategies.moving_average import MovingAverageStrategy

class TestBacktesting(unittest.TestCase):
    def test_simple_ma_strategy(self):
        data = pd.DataFrame({
            'Date': pd.date_range("2023-01-01", periods=5),
            'Open': [100, 102, 103, 104, 105],
            'Close': [101, 103, 104, 103, 102],
        })
        # Minimal rolling MAs for demonstration
        data['ShortMA'] = data['Close'].rolling(2).mean()
        data['LongMA'] = data['Close'].rolling(3).mean()

        engine = BacktestEngine(initial_capital=1000)
        engine.set_data(data)

        strat = MovingAverageStrategy(short_window=2, long_window=3)
        final_value = engine.run(strat)

        self.assertTrue(final_value >= 0, "Final value should be non-negative")

if __name__ == "__main__":
    unittest.main()
