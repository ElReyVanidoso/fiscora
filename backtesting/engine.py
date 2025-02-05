import pandas as pd
from backtesting.portfolio import Portfolio
from backtesting.order import Order

class BacktestEngine:
    def __init__(self, initial_capital: float = 100000.0):
        """
        :param initial_capital: Starting capital for the backtest.
        """
        self.initial_capital = initial_capital
        self.portfolio = Portfolio(initial_capital)
        self.data = pd.DataFrame()
    
    def set_data(self, data: pd.DataFrame):
        """
        Load the market data into the engine.
        Expects columns like ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'].
        """
        # Sort by date just to be safe
        data.sort_values(by='Date', inplace=True)
        data.reset_index(drop=True, inplace=True)
        self.data = data
    
    def run(self, strategy):
        """
        Main loop: for each row (bar) in self.data:
          1) Strategy decides to buy/sell/hold
          2) Engine executes orders on the portfolio
        :param strategy: An object that implements `on_bar(current_bar, portfolio)`
        :return: final portfolio value
        """
        for i in range(len(self.data)):
            current_bar = self.data.iloc[i]
            
            # Strategy logic: returns a list of Order objects
            orders = strategy.on_bar(current_bar, self.portfolio)
            
            # Execute each order in the portfolio
            for order in orders:
                # We'll assume we use the Close price for fills
                fill_price = current_bar['Close']
                self.portfolio.execute_order(order, fill_price)
        
        # Return the final portfolio value using the last bar's Close price
        if len(self.data) > 0:
            last_close = self.data.iloc[-1]['Close']
            return self.portfolio.calculate_value(last_close)
        else:
            return self.portfolio.cash
