import os, json, warnings
import pandas as pd
import importlib.util
import ta
warnings.filterwarnings("ignore")

def load_config():
    spec = importlib.util.spec_from_file_location("config",
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "0_config.py"))
    cfg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cfg)
    return cfg

cfg = load_config()
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

CACHE = os.path.join(cfg.RESULTS_DIR, "data_cache")

class RSIStrat(Strategy):
    rsi_p = 14
    def init(self):
        self.rsi = self.I(lambda x: ta.momentum.RSIIndicator(pd.Series(x), self.rsi_p).rsi().values, self.data.Close)
    def next(self):
        if self.rsi[-1] < 30: self.buy()
        elif self.rsi[-1] > 70 and self.position: self.position.close()

class MACross(Strategy):
    fast = 10; slow = 20
    def init(self):
        self.fma = self.I(lambda x: pd.Series(x).rolling(self.fast).mean().values, self.data.Close)
        self.sma = self.I(lambda x: pd.Series(x).rolling(self.slow).mean().values, self.data.Close)
    def next(self):
        if crossover(self.fma, self.sma): self.buy()
        elif crossover(self.sma, self.fma) and self.position: self.position.close()

class MACDStrat(Strategy):
    def init(self):
        c = pd.Series(self.data.Close); m = ta.trend.MACD(c)
        self.macd = self.I(lambda: m.macd().values)
        self.signal = self.I(lambda: m.macd_signal().values)
    def next(self):
        if crossover(self.macd, self.signal): self.buy()
        elif crossover(self.signal, self.macd) and self.position: self.position.close()

class BBStrat(Strategy):
    def init(self):
        c = pd.Series(self.data.Close); b = ta.volatility.BollingerBands(c)
        self.upper = self.I(lambda: b.bollinger_hband().values)
        self.lower = self.I(lambda: b.bollinger_lband().values)
    def next(self):
        if self.data.Close[-1] < self.lower[-1]: self.buy()
        elif self.data.Close[-1] > self.upper[-1] and self.position: self.position.close()

STRAT_MAP = {"RSI": RSIStrat, "MACD": MACDStrat, "BB": BBStrat,
             "EMA": MACross, "MA": MACross, "GENERIC": MACross, "STOCH": RSIStrat}

def stars(w): return 5 if w>=80 else 4 if w>=60 else 3 if w>=40 else 2 if w>=20 else 1

ALL_TICKERS = cfg.CRYPTO_TICKERS + list(cfg.STOCK_TICKERS)

def run_bt(s, ticker, tf):
    path = os.path.join(CACHE, f"{ticker}_{tf}.csv")
    if not os.path.exists(path): return None
    df = pd.read_csv(path, index_col=0, parse_dates=True)
    df.columns = [c.capitalize() for c in df.columns]
    df = df.dropna()
    if len(df) < 100: return None
    try:
        bt = Backtest(df, STRAT_MAP.get(s["type"], MACross), cash=10000, commission=0.001)
        st = bt.run()
        if st["# Trades"] < cfg.MIN_TRADES: return None
        return {"strategy": s["name"], "ticker": ticker, "timeframe": tf,
                "win_rate": round(st["Win Rate [%]"], 2), "return_pct": round(st["Return [%]"], 2),
                "trades": st["# Trades"], "stars": stars(st["Win Rate [%]"]), "type": s["type"]}
    except: return None

with open(os.path.join(cfg.RESULTS_DIR, "strategy_registry.json")) as f:
    strats = json.load(f)

results = []; done = 0
total = len(strats) * len(ALL_TICKERS) * len(cfg.TIMEFRAMES)
print(f"\nRunning {total:,} backtests...\n")
for s in strats:
    for ticker in ALL_TICKERS:
        for tf in cfg.TIMEFRAMES:
            r = run_bt(s, ticker, tf)
            if r: results.append(r)
            done += 1
            if done % 5000 == 0:
                print(f"  {done:,}/{total:,} ({round(done/total*100,1)}%) | hits: {len(results):,}")
pd.DataFrame(results).to_csv(os.path.join(cfg.RESULTS_DIR, "raw_results.csv"), index=False)
print(f"\nDone! {len(results):,} valid results saved\n")
