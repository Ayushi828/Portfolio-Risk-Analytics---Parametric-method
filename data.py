import pandas as pd
import yfinance as yf
from tickers import tickers

#DOWNLOADING DAILY ADJUSTED CLOSE PRICE


def get_adj_close_data(start="2021-01-01", end="2025-12-31"):
    adj_close_data = pd.DataFrame()

    for ticker in tickers:
        data_r = yf.download(ticker, start=start, end=end)
        if not data_r.empty:
            adj_close_data[ticker] = data_r['Close']
        else:
            print(f"No data found for {ticker}")

    print(adj_close_data)
    return adj_close_data