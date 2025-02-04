class BacktestEngine:
    def __init__(self, initial_capital: float = 100000.0):
        self.initial_capital = initial_capital
        self.portfolio = None
        self.data = []

    def set_data(self, data):
        self.data = data

    def run(self, strategy):
        """
        Main loop to apply the strategy logic over the data.
        """
        for bar in self.data:
            strategy.on_bar(bar, self.portfolio)
        # Return final portfolio stats or value
        return None
