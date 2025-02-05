import pandas as pd
from backtesting.order import Order
from backtesting.portfolio import Portfolio

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
    
    def on_bar(self, current_bar, portfolio):
        short_ma = current_bar['ShortMA']  # single float
        long_ma = current_bar['LongMA'] 

        # single float
        print("********************")
        print("ShortMA: ", short_ma, " ... ")
        print("********************")
        print("LongMA: ", long_ma, " ... ")
        print("********************")

         # If either is NaN (window not reached), skip:
        if pd.isna(short_ma) or pd.isna(long_ma):
            return []

        orders = []
        # Now short_ma and long_ma are floats, so this comparison works:
        if short_ma > long_ma and not self.in_position:
            orders.append(Order(10))
            self.in_position = True
        elif short_ma < long_ma and self.in_position:
            orders.append(Order(-10))
            self.in_position = False
        return orders

