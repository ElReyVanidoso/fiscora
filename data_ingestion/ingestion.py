import pandas as pd
import yfinance as yf  # Example library for free data (daily resolution)

def fetch_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """
    Fetch historical data for a given symbol using yfinance.
    - symbol: e.g. 'AAPL'
    - start: 'YYYY-MM-DD'
    - end: 'YYYY-MM-DD'
    
    Returns a pandas DataFrame with the columns:
    Date, Open, High, Low, Close, Adj Close, Volume
    """
    df = yf.download(symbol, start=start, end=end)
    # If empty or invalid symbol, handle that gracefully
    if df.empty:
        print(f"No data returned for {symbol}")
        return df
    
    # Reset index so 'Date' becomes a column
    df.reset_index(inplace=True)
    
    # Convert Date column to string or keep it as a datetime
    # Here we assume we keep it as datetime objects
    df['Date'] = pd.to_datetime(df['Date'])
    
    return df
