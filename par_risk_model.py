import numpy as np
from scipy.stats import norm

#COVARIANCE MATRIX FOR EQUITY & STANDARD DEVIATION

def eq_cov_and_std(log_returns, weight):
    cov_matrix = log_returns.cov() * 252
    portf_std_dev = np.sqrt(weight.T @ cov_matrix @ weight)
    return cov_matrix, portf_std_dev

#CALCULATING VAR FOR DIFFERENT CONFIDENCE LEVEL

def eq_var(portf_value, portf_std_dev, confidence, days=10):
    VAR = []

    for cl in confidence:
        var = portf_value * portf_std_dev * norm.ppf(cl) * np.sqrt(days / 252)
        VAR.append(var)

    return VAR

#PRINTING THE CALCULATED VAR

def show_var(confidence, VAR):
    print(f"{'Confidence':<20} {'Value at Risk':<15}")
    print("-" * 40)

    for cl, var in zip(confidence, VAR):
        print(f"{cl*100:>5}% : {' ':<12} Rs {var:>10,.2f}")
        
