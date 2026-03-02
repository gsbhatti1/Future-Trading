import os, time
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import importlib.util

def load_config():
    spec = importlib.util.spec_from_file_location("config",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "0_config.py"))
    cfg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cfg)
    return cfg

cfg = load_config()
CACHE = os.path.join(cfg.RESULTS_DIR, "data_cache")
LOOKBACK = {"1m": 7, "5m": 59, "15m": 59, "30m": 59, "1h": 365}

YF_MAP = {
    "SPY": "^GSPC",
    "QQQ": "^NDX",
    "DIA": "^DJI",
    "NAS100": "^NDX",
    "US30": "^DJI"
}

def fetch_yfinance(yticker, tf, days):
    end = datetime.now()
    start = end - timedelta(days=days)
    df = yf.download(yticker, start=start, end=end, interval=tf, progress=False, auto_adjust=True)
    df.columns = [c[0].lower() if isinstance(c, tuple) else c.lower() for c in df.columns]
    return df[["open","high","low","close","volume"]].dropna()

print("\nFetching all stock/contract data...\n")
for tf in cfg.TIMEFRAMES:
    for ticker, yticker in YF_MAP.items():
        f = os.path.join(CACHE, f"{ticker}_{tf}.csv")
        if os.path.exists(f): os.remove(f)
        try:
            df = fetch_yfinance(yticker, tf, LOOKBACK[tf])
            df.to_csv(f)
            print(f"  {ticker} {tf} -> {len(df)} rows")
            time.sleep(0.3)
        except Exception as e:
            print(f"  FAIL {ticker} {tf}: {e}")
print("\nAll stock data done!\n")
