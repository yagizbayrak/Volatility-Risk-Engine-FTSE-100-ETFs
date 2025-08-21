
"""Data utilities (INCOMPLETE).
- get_price_data: TODO — download Yahoo prices for tickers
- to_log_returns: TODO — compute log returns
- realized_vol: TODO — rolling sqrt of sum of squared returns (window=20)
"""

from typing import List
# import yfinance as yf  # to be used later
# import pandas as pd
# import numpy as np

def get_price_data(tickers, start="2010-01-01", end=None, auto_adjust=True):
    """PSEUDOCODE:
    - call yfinance.download(tickers, start, end, auto_adjust=True, progress=False)
    - select 'Close' column(s)
    - sort by date, drop NA rows
    - return wide DataFrame (columns=tickers)
    """
    raise NotImplementedError("get_price_data is a stub — implement later.")

def to_log_returns(prices):
    """PSEUDOCODE:
    - returns = log(prices).diff()
    - drop first NA
    - return returns
    """
    raise NotImplementedError("to_log_returns is a stub — implement later.")

def realized_vol(returns, window=20, annualize=True, periods=252):
    """PSEUDOCODE:
    - rv_daily = sqrt( rolling_sum( returns**2, window ) )
    - if annualize: rv_annual = rv_daily * sqrt(periods)
    - return rv_daily, rv_annual
    """
    raise NotImplementedError("realized_vol is a stub — implement later.")
