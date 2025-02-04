from backtesting.order import Order

class MovingAverageStrategy:
    def __init__(self):
        self.in_position = False

    def on_bar(self, bar, portfolio):
        """
        bar could be a dict or row with 'Open', 'Close', etc.
        """
        orders = []
        # Example logic: if Close > Open and not in position, buy 10
        if bar['Close'] > bar['Open'] and not self.in_position:
            orders.append(Order(10))
            self.in_position = True
        elif bar['Close'] < bar['Open'] and self.in_position:
            orders.append(Order(-10))
            self.in_position = False

        # In real code, you'd pass these orders to the portfolio
        # For now, let's just return them
        return orders
