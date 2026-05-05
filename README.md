# Value at Risk (VaR) — Parametric & Historical Methods

## Overview

Value at Risk (VaR) is a statistical measure used to quantify the potential loss in value of a portfolio over a defined time period, given a specified confidence level.

This project implements Value at Risk (VaR) using two common approaches:  
- Parametric (Variance-Covariance) Method  
- Historical Simulation  

---

## What’s inside

- Parametric VaR assuming normal distribution of returns.  
- Historical VaR calculation based on past returns.  
- Simple comparison between the two approaches.  

---

## How it works

### Parametric Method

This method uses statistical approach and follow a normal distribution:

- Calculate mean and standard deviation  
- Use Z-score for chosen confidence level  
- Calculate VaR using:

$$             VaR = μ - (Z * σ)

### Historical Method

In historical approach we look for historical data instead of following distribution to calculate risk:

-	Sort returns from worst to best.
-	Pick the percentile based on confidence level.
-	That value represents the VaR.

