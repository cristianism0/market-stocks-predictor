import pandas as pd

def data_request() -> pd.DataFrame:
    """Request data from Yahoo Finances using yfinance module"""
    import yfinance as yf
    try:
        stocks = yf.download('MSFT AAPL NVDA LCID QS WBD NU TSLA INTC RIOT', period="10y", group_by='ticker')  #download data
    except ConnectionError:
        print("Connection error. Please check your internet connection.")
        return pd.DataFrame()  # Return an empty DataFrame if download fails
    return stocks

def calc_returns(stocks):
    """Get all Close Columns for each stock"""
    close_columns = [col for col in stocks.columns if 'Close' in col]
    close_prices = stocks[close_columns].copy()
    
    close_prices.columns = [col[0] for col in close_prices.columns]
    
    returns = close_prices.pct_change().dropna()  
    covReturns = returns.cov()
    meanReturns = returns.mean()
    
    return covReturns, meanReturns
