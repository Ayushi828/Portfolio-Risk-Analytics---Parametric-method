import numpy as np

#CALCULATING LOG RETURNS

def calc_log_returns(adj_close_data):
    log_returns = np.log(adj_close_data / adj_close_data.shift(1))
    log_returns = log_returns.dropna()

    print(log_returns)
    return log_returns

#CALCULATING HISTORICAL RETURNS

def calc_portfolio_returns(log_returns, weight):
    historical_returns = (log_returns * weight).sum(axis=1)
    print(historical_returns)
    return historical_returns

#CALCULATING X-DAY HISTORICAL RETURNS

def calc_x_day_returns(historical_returns, days=10):
    historical_x_day_returns = historical_returns.rolling(window=days).sum()
    return historical_x_day_returns