# PORTFOLIO RISK ANALSIS THROUGH PARAMETRIC METHOD

## Overview

Value at Risk (VaR) is a statistical measure used to quantify the potential loss in value of a portfolio over a defined time period, given a specified confidence level.

This project implements Value at Risk (VaR) using Parametric (Variance-Covariance) Method.

---

## How it works

### Parametric Method

This method uses statistical approach and follow a normal distribution:

- Calculate mean and standard deviation  
- Use Z-score for chosen confidence level  
- Calculate VaR using:

$$             VaR = μ - (Z * σ)

