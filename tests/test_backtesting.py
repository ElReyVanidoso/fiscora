import unittest
from backtesting.engine import BacktestEngine
from backtesting.portfolio import Portfolio
from strategies.moving_average import MovingAverageStrategy

class TestBacktesting(unittest.TestCase):
    def test_simple_strategy(self):
        engine = BacktestEngine(initial_capital=1000)
        # Provide some mock data
        mock_data = [
            {'Open': 100, 'Close': 101},
            {'Open': 102, 'Close': 100},
        ]
        engine.set_data(mock_data)
        engine.portfolio = Portfolio(1000)
        strategy = MovingAverageStrategy()

        final_value = engine.run(strategy)
        self.assertIsNotNone(final_value, "Engine run should return a final value")

if __name__ == '__main__':
    unittest.main()
