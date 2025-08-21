
"""Metrics (INCOMPLETE): RMSE, QLIKE, Sharpe, Max Drawdown."""
# import numpy as np
# import pandas as pd

def rmse(y_true, y_pred):
    """TODO: implement sqrt(mean((y_true - y_pred)^2))."""
    raise NotImplementedError

def qlike(realized_var, forecast_var):
    """TODO: implement mean(log(fv) + rv/fv) with small epsilon."""
    raise NotImplementedError

def sharpe_ratio(returns, rf=0.0, periods=252):
    """TODO: annualized Sharpe from daily returns."""
    raise NotImplementedError

def max_drawdown(returns):
    """TODO: compute cumulative product and worst peak-to-trough."""
    raise NotImplementedError
