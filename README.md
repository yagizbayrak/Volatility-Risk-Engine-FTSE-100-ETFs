[README.md](https://github.com/user-attachments/files/21919806/README.md)
# Volatility & Risk Engine — FTSE 100 ETFs (ISF.L, VUKE.L)

**Status:** learning project (in progress) • **Created:** 2025-08-12

This repository contains a beginner-friendly Python toolkit for **volatility forecasting** and **risk measurement** on FTSE 100 ETFs (**ISF.L**, **VUKE.L**). It implements simple models and clear evaluation:

- **Forecasts:** EWMA and GARCH(1,1), compared against 20‑day realized volatility (metrics: **RMSE**, **QLIKE**).
- **Risk:** 95%/99% **Value-at-Risk (VaR)** and **Expected Shortfall (ES)** with basic out‑of‑sample coverage tests.
- **Allocation:** a **volatility-targeted** strategy (with leverage cap and transaction-cost assumptions) benchmarked vs buy-and-hold (Sharpe, max drawdown).
- **App:** minimal **Streamlit** dashboard for quick exploration.
- **Reproducibility:** tidy repo layout and a few unit tests.

> ⚠Educational only — **not** financial advice.

---

## Quickstart

```bash
# 1) Clone & create a virtual environment (recommended)
python -m venv .venv
# Windows: .\.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install
pip install -r requirements.txt

# 3) Run tests (optional)
pytest -q

# 4) Launch Streamlit app
streamlit run app/streamlit_app.py
```

The app and data loader fetch prices from Yahoo Finance for `ISF.L` and `VUKE.L`.
You can change tickers in the sidebar.

---

## Repository layout

```
.
├─ app/
│  └─ streamlit_app.py         # Minimal dashboard
├─ notebooks/
│  └─ 01_quickstart.ipynb      # Starter notebook
├─ src/
│  ├─ __init__.py
│  ├─ data.py                  # Data loading & returns
│  ├─ models.py                # EWMA / GARCH forecasts
│  ├─ risk.py                  # VaR / ES & coverage tests
│  ├─ strategy.py              # Vol-target backtest
│  ├─ metrics.py               # RMSE, QLIKE, Sharpe, DD
│  └─ plots.py                 # Matplotlib helpers
├─ tests/
│  ├─ test_metrics.py
│  └─ test_strategy.py
├─ data/
│  └─ .gitkeep
├─ requirements.txt
├─ LICENSE
├─ .gitignore
└─ README.md
```

---

## How it works (short)

1. **Load prices** from Yahoo Finance (`yfinance`), compute daily **log returns**.
2. Compute **realized volatility** over a rolling 20‑day window.
3. Fit **EWMA** (decay λ) and **GARCH(1,1)** on returns; produce **1‑day‑ahead** volatility forecasts.
4. Evaluate accuracy vs realized vol using **RMSE** and **QLIKE**.
5. Compute **VaR/ES** at 95%/99% both via historical and parametric (Normal) methods; run a simple coverage check.
6. Build a **vol-targeted** strategy: scale daily exposure ≈ target_vol / forecast_vol, with a leverage cap and transaction costs.
7. Compare with **buy‑and‑hold** using Sharpe ratio and max drawdown; visualize in the app.

---

## Notes & caveats

- Yahoo data may have **splits/dividends**; we use `auto_adjust=True`. Validate as needed.
- For **GARCH**, returns are often scaled (e.g., ×100). See docstrings in `src/models.py`.
- **Coverage tests** here are simple (Kupiec POF-style count). For production, expand diagnostics.

---

## Push to GitHub

```bash
git init
git add .
git commit -m "Init: FTSE volatility & risk engine scaffold"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
```

---

## License

MIT — see `LICENSE`.
