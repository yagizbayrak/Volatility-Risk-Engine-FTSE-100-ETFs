
"""Risk (INCOMPLETE): VaR/ES (historical & parametric) and a simple coverage test."""
# from scipy.stats import norm

def var_es_historical(returns, alpha=0.95):
    """PSEUDOCODE:
    - sort returns ascending
    - q = quantile(1-alpha)
    - VaR = -q
    - ES = -mean(returns <= q)
    """
    raise NotImplementedError

def var_es_parametric(mu, sigma, alpha=0.95, dist='normal'):
    """PSEUDOCODE (Normal):
    - z = Phi^{-1}(1-alpha)
    - VaR = -(mu + sigma*z)
    - ES  = -(mu - sigma * phi(z)/(1-alpha))
    """
    raise NotImplementedError

def coverage_test(returns, var_series, alpha=0.95):
    """PSEUDOCODE:
    - align returns and VaR
    - exception when return < -VaR
    - report count, expected, and rate
    """
    raise NotImplementedError
