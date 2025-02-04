class Order:
    """
    Simple class to represent a Buy/Sell order.
    """
    def __init__(self, quantity: int):
        self.quantity = quantity  # positive => buy, negative => sell
