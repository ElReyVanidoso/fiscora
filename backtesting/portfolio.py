class Portfolio:
    """
    Tracks how many shares we hold, our cash, and our average cost basis.
    """
    def __init__(self, initial_capital: float):
        self.cash = initial_capital
        self.positions = 0     # number of shares held
        self.avg_price = 0.0   # average cost basis
    
    def execute_order(self, order, fill_price: float):
        """
        Updates 'positions' and 'cash' based on the fill_price for the trade.
        """
        if order.quantity == 0:
            return
        
        # The cost of this transaction
        cost = order.quantity * fill_price
        
        # If it's a buy (quantity > 0)
        if order.quantity > 0:
            # Check if we have enough cash
            if cost > self.cash:
                # Not enough cash, skip or raise an error
                print("Insufficient cash to buy.")
                return
            # Recalculate avg_price if we already hold some shares
            total_shares = self.positions + order.quantity
            if total_shares > 0:
                self.avg_price = (
                    (self.avg_price * self.positions) + cost
                ) / total_shares
            self.positions += order.quantity
            self.cash -= cost
        
        # If it's a sell (quantity < 0)
        else:
            shares_to_sell = abs(order.quantity)
            if shares_to_sell > self.positions:
                # Sell only what's possible
                shares_to_sell = self.positions
            
            self.positions -= shares_to_sell
            self.cash += shares_to_sell * fill_price
    
    def calculate_value(self, current_price: float) -> float:
        """
        Current total value = cash + (positions * current_price).
        """
        return self.cash + (self.positions * current_price)
