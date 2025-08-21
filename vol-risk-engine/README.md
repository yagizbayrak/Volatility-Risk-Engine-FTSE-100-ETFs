# Volatility & Risk Engine — FTSE 100 ETFs (ISF.L, VUKE.L) — **Skeleton**
**Status:** intentionally **incomplete** (learning scaffold) — 2025-08-21

This repo is a *starter shell* for a learning project. It contains **pseudocode** and **stubs** only.
Nothing is expected to run yet.

## What to build (later)
- Data loader (`yfinance`) → daily prices for **ISF.L** / **VUKE.L**
- Returns + realized 20-day volatility
- Forecasts: **EWMA**, **GARCH(1,1)**
- Risk: **VaR/ES** (95%/99%) + simple coverage checks
- Simple **vol-target** strategy (leverage cap, txn costs)
- Tiny **Streamlit** app to show charts
- Basic unit tests

## Notes
- All Python modules raise `NotImplementedError` or contain pseudocode.
- Replace `TODO:` blocks with actual implementations as you learn.
- You can push this to GitHub now; treat it as a public learning log.

## Setup (later)
```bash
python -m venv .venv
# activate venv ...
pip install -r requirements.txt  # contains more than you need right now
```

## Roadmap (scratch)
- [ ] Implement `get_price_data` & `to_log_returns`
- [ ] Implement EWMA, then compare vs realized vol (RMSE/QLIKE)
- [ ] Add GARCH(1,1) forecast
- [ ] VaR/ES (historical & normal)
- [ ] Vol-target weights + backtest loop
- [ ] Streamlit UI tab for each step
- [ ] Tests for metrics & windowing
