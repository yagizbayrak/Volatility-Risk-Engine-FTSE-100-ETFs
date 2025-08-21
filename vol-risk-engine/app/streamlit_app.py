
import streamlit as st

st.set_page_config(page_title="FTSE Volatility & Risk Engine (Skeleton)", layout="centered")
st.title("Volatility & Risk Engine — Skeleton")
st.caption("This is a learning scaffold with placeholders. Nothing runs yet.")

st.header("Plan")
st.markdown("""
- [ ] Load ISF.L / VUKE.L prices
- [ ] Compute returns + realized vol (20d)
- [ ] EWMA & GARCH forecasts
- [ ] VaR/ES + coverage checks
- [ ] Vol-target strategy
- [ ] Charts
""")

st.subheader("Pseudocode sketch")
st.code("""
# PSEUDOCODE ONLY — DO NOT EXECUTE

prices = get_price_data(["ISF.L","VUKE.L"], start="2010-01-01")   # TODO
returns = to_log_returns(prices)                                       # TODO
rv20 = realized_vol(returns, window=20)                                # TODO

ew = ewma_vol(returns['ISF.L'])                                        # TODO
garch_in, garch_f1 = garch11_forecast(returns['ISF.L'])                # TODO

var95, es95 = var_es_historical(returns['ISF.L'], alpha=0.95)          # TODO
report = coverage_test(returns['ISF.L'], var_series=..., alpha=0.95)   # TODO

bt = backtest_vol_target(returns['ISF.L'], forecast_vol=ew)            # TODO
""", language="python")
