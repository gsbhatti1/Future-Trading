# 15-Minute Breakout Multi-Timeframe Synergy Strategy with Risk-Reward Optimization Model

**Author:** ianzeng123

## Overview

This strategy is a quantitative trading system based on timeframe breakout, utilizing the synergistic relationship between 15-minute and 2-minute timeframes to determine trading signals. It identifies entry opportunities by observing whether the 2-minute candle's closing price breaks through the high or low of the previous completed 15-minute candle, while implementing a precise risk control mechanism with a risk-to-reward ratio of 1:3. The strategy captures momentum continuation after short-term price breakouts, with an average win rate of approximately 30%, but achieves positive expected returns due to its well-designed risk-reward ratio.

## Strategy Principles

1. The strategy uses `request.security` to obtain the highest price, lowest price, and time for the 15-minute timeframe.
2. When a new 15-minute candle is detected, the strategy saves the previous completed 15-minute candle's high and low as breakout reference points.
3. **Long condition**: 2-minute candle close breaks above the last complete 15-min high. Entry at 2-min close; stop at 15-min low; target = entry + 3x risk.
4. **Short condition**: 2-minute candle close breaks below the last complete 15-min low. Entry at 2-min close; stop at 15-min high; target = entry - 3x risk.

This design uses the larger timeframe (15 min) for important price levels and the smaller timeframe (2 min) to optimize entries, reduce slippage, and improve execution precision.

## Strategy Advantages

1. **Clear Risk Management**: Precise 1:3 risk-reward ratio ensures potential returns are 3x potential losses, allowing positive expected returns even with ~30% win rate.
2. **Multi-Timeframe Synergy**: Captures important price levels from the 15-min chart while optimizing entries with 2-min precision.
3. **Automated Execution**: Clear entry and exit conditions reduce emotional interference.
4. **Integrated Capital Management**: Uses percentage of equity for position sizing, scaling risk proportionally with account size.
5. **High Adaptability**: Clean code structure, easy to extend for different markets.

## Strategy Risks

1. **Low Win Rate Risk**: ~30% win rate means most individual trades result in small losses.
2. **False Breakout Signals**: Price may not follow through after breaking key levels, especially in ranging markets.
3. **Slippage Risk**: In fast-moving markets, execution price may differ from planned price.
4. **Overtrading Risk**: Short 2-min timeframe may generate excessive trades and high transaction costs.
5. **Market Environment Dependency**: Performs better in trending markets; may underperform in choppy conditions.

**Solutions:**
- Add trend/volatility filters to reduce false signals
- Set daily maximum trade limits
- Adjust risk parameters during high/low volatility periods

## Optimization Directions

1. **Add Trend Filters**: Use MA or MACD to only trade breakouts aligned with the larger trend.
2. **Dynamic Risk-Reward Ratio**: Adjust the 1:3 ratio based on market volatility conditions.
3. **Time Filtering**: Avoid trading during market open/close or low-liquidity periods.
4. **Partial Profit-Taking**: Close partial positions at intermediate targets; let rest run.
5. **Adaptive Parameters**: Auto-adjust the 15-min period based on market regime.
6. **Volume Confirmation**: Require volume expansion on breakouts to improve signal quality.

## Summary

This strategy is a clearly structured quantitative system that captures post-breakout momentum using multi-timeframe price information. Despite a low ~30% win rate, the 1:3 risk-reward mechanism delivers positive expected returns. Core strengths: strict risk control, clear rules, multi-timeframe synergy. Key improvements: reduce false signals with trend filtering and dynamic parameters.

## Pine Script Source

```pinescript
//@version=5
strategy("15-min Breakout via 2-min Candle (R:R=1:3)", overlay=true, initial_capital=100000, default_qty_type=strategy.percent_of_equity, default_qty_value=10)

fifteenHigh = request.security(syminfo.tickerid, "15", high)
fifteenLow = request.security(syminfo.tickerid, "15", low)
time15 = request.security(syminfo.tickerid, "15", time)

var float last15High = na
var float last15Low = na
bool new15bar = time15 != time15[1]

if new15bar
    last15High := fifteenHigh[1]
    last15Low := fifteenLow[1]

bool longCondition = not na(last15High) and close > last15High
if longCondition
    float stopPrice = last15Low
    float risk = close - stopPrice
    float takeProfit = close + 3 * risk
    strategy.entry("Long Breakout", strategy.long)
    strategy.exit("Long Exit (SL/TP)", "Long Breakout", stop=stopPrice, limit=takeProfit)

bool shortCondition = not na(last15Low) and close < last15Low
if shortCondition
    float stopPrice = last15High
    float risk = stopPrice - close
    float takeProfit = close - 3 * risk
    strategy.entry("Short Breakout", strategy.short)
    strategy.exit("Short Exit (SL/TP)", "Short Breakout", stop=stopPrice, limit=takeProfit)
```

## Backtest Parameters
- Period: 2025-03-23 to 2025-03-24
- Timeframe: 15m / Base: 15m
- Exchange: Futures Binance ETH/USDT
- Initial Capital: $100,000
