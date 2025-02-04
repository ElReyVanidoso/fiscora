class Portfolio:
    """
    Tracks positions, cash, and overall P/L.
    """
    def __init__(self, initial_capital: float):
        self.cash = initial_capital
        self.positions = 0
        self.avg_price = 0.0

    def execute_order(self, order, price: float):
        pass  # Update self.cash and self.positions accordingly

    def total_value(self, current_price: float):
        return self.cash + (self.positions * current_price)
