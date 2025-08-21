
"""Strategy (INCOMPLETE): Vol-target weights and simple backtest."""

def vol_target_weights(forecast_vol, target_ann_vol=0.10, leverage_cap=2.0, periods=252):
    """PSEUDOCODE:
    - target_daily = target_ann_vol / sqrt(periods)
    - w = target_daily / forecast_vol
    - cap at leverage_cap; replace inf/NaN with 0
    - return w
    """
    raise NotImplementedError

def backtest_vol_target(returns, forecast_vol, target_ann_vol=0.10, leverage_cap=2.0, cost_bps=10.0, periods=252):
    """PSEUDOCODE:
    - use yesterday's weight for today's return (shift by 1)
    - transaction cost on |delta weight| * (bps/10000)
    - strat_ret = w_{t-1} * r_t - cost_t
    - equity = cumprod(1 + strat_ret)
    - return a small DataFrame (weight, ret, equity)
    """
    raise NotImplementedError
