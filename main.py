from data_ingestion.ingestion import fetch_data
from backtesting.engine import BacktestEngine
from strategies.moving_average import MovingAverageStrategy

def main():
    # 1) Fetch historical data
    symbol = "AAPL"
    start_date = "2023-01-01"
    end_date = "2023-06-01"
    df = fetch_data(symbol, start_date, end_date)
    
    if df.empty:
        print("No data fetched, exiting.")
        return
    
    # 2) Compute rolling MAs in your DataFrame
    df['ShortMA'] = df['Close'].rolling(20).mean()
    df['LongMA'] = df['Close'].rolling(50).mean()
    
    # 3) Initialize the backtest engine
    engine = BacktestEngine(initial_capital=10000.0)
    engine.set_data(df)
    
    # 4) Initialize your strategy
    ma_strategy = MovingAverageStrategy(short_window=20, long_window=50)
    
    # 5) Run the backtest
    final_value = engine.run(ma_strategy)
    print(f"Final portfolio value after backtest: ${final_value:,.2f}")

if __name__ == "__main__":
    main()
