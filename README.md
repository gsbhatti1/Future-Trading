# Future-Trading

## GB-ALPHA AI Trading Engine

Automated pipeline that:
1. Pulls 5,800+ Chinese trading strategies from source repo
2. Translates all strategies to English using local Qwen AI
3. Extracts entry/exit logic and indicators from each strategy
4. Backtests all strategies on NAS100, SPX, US30 (1m/5m/15m)
5. Ranks by win rate, profit factor, max drawdown
6. Synthesizes top performers into one master Pine Script v5

### Pipeline
| Script | Purpose |
|--------|---------|
| engine/1_clone_translate.py | Clone source + translate Chinese to English |
| engine/2_extract_logic.py | Extract trading logic from each file |
| engine/3_backtest.py | Backtest on Yahoo Finance data |
| engine/4_rank_strategies.py | Score and rank all strategies |
| engine/5_build_pine.py | Build final Pine Script from top strategies |

### Assets
- NAS100 (^NDX)
- SPX (^GSPC)  
- US30 (^DJI)

### Timeframes
- 1m, 5m, 15m
