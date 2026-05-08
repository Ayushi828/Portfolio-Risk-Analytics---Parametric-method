import numpy as np

from data import (get_adj_close_data)
from returns import (calc_log_returns,calc_portfolio_returns,calc_x_day_returns)

from par_risk_model import (eq_cov_and_std, eq_var, show_var)
from visualisation import plot_histogram
from tickers import tickers

# DATA
adj_close_data = get_adj_close_data()

# RETURNS
log_returns = calc_log_returns(adj_close_data)

# PORTFOLIO WEIGHTS
portf_value = 10000000
weight = np.array([0.2, 0.125, 0.3, 0.275, 0.1])

historical_returns = calc_portfolio_returns(log_returns, weight)

# X-DAY RETURNS
days = 10
historical_x_day_returns = calc_x_day_returns(historical_returns, days)

# RISK MODEL
cov_matrix, portf_std_dev = eq_cov_and_std(log_returns, weight)
confidence = [0.9, 0.95, 0.99]

VAR = eq_var(portf_value, portf_std_dev, confidence, days)
show_var(confidence, VAR)

# PLOT
historical_x_day_returns_rs = historical_x_day_returns * portf_value

plot_histogram(historical_x_day_returns_rs, days, confidence, VAR)