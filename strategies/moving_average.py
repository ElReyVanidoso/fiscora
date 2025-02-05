import pandas as pd
from backtesting.order import Order

class MovingAverageStrategy:
    """
    A simple strategy: if Short MA crosses above Long MA => Buy, else Sell.
    """
    def __init__(self, short_window=20, long_window=50):
        self.short_window = short_window
        self.long_window = long_window
        self.in_position = False
        self.prev_short_ma = None
        self.prev_long_ma = None
    
    def on_bar(self, current_bar: pd.Series, portfolio):
        """
        Called for each bar. We can compute or retrieve MAs.
        
        For a full approach, you'd either:
          A) Precompute MAs and store them in the DataFrame
          B) Keep rolling windows in the strategy
        """
        orders = []
        
        # We'll assume the DataFrame has rolling MAs precomputed (for simplicity).
        # e.g., if we have a 'ShortMA' and 'LongMA' column in current_bar
        short_ma = current_bar.get('ShortMA', None)
        long_ma = current_bar.get('LongMA', None)
        
        # If we have no data for the MAs yet, skip
        if short_ma is None or long_ma is None:
            return orders
        
        # Simple crossover logic: if short MA > long MA => buy. If short < long => sell
        if short_ma > long_ma and not self.in_position:
            # Buy 10 shares
            orders.append(Order(quantity=10))
            self.in_position = True
        elif short_ma < long_ma and self.in_position:
            # Sell all shares (in this example we fix it at 10)
            orders.append(Order(quantity=-10))
            self.in_position = False
        
        return orders
