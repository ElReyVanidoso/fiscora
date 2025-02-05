class Order:
    """
    Represents a trade order.
    quantity > 0 => Buy 'quantity' shares
    quantity < 0 => Sell 'quantity' shares (absolute value)
    """
    def __init__(self, quantity: int):
        self.quantity = quantity

    def __repr__(self):
        return f"<Order quantity={self.quantity}>"
