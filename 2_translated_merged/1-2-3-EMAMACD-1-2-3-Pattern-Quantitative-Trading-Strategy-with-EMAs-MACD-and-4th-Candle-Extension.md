# 1-2-3 Pattern Quantitative Trading Strategy with EMAs, MACD, and 4th Candle Extension

**Author:** ChaoZhang

## Overview

This strategy, written in Pine Script, aims to identify potential buy and sell signals based on the 1-2-3 pattern, combined with additional conditions involving Exponential Moving Averages (EMAs) and the Moving Average Convergence Divergence (MACD) indicator. The strategy leverages price patterns, trend confirmation, and momentum indicators to provide comprehensive trading signals.

## Strategy Logic

The core of this strategy is to identify the 1-2-3 pattern, which is a common price pattern consisting of three consecutive candles, indicating a potential trend reversal. For buy signals, the first candle closes above its open, the second candle closes below its open, the third candle closes above the close of the first candle, and finally, the fourth candle closes above the close of the third candle. The conditions for sell signals are the exact opposite.

In addition to the 1-2-3 pattern, the strategy employs EMA and MACD indicators to confirm the trend direction and potential trend reversals. The 9-period EMA and 20-period EMA are used for trend confirmation, while the MACD line and signal line are used to identify momentum and potential trend reversals.

When all the buy conditions are met (1-2-3 pattern formed, close price above both EMAs, MACD line above the signal line), the strategy opens a long position. Similarly, when all the sell conditions are met, the strategy opens a short position. The strategy closes positions when the opposite signal is generated or when the current candle closes in the opposite direction.

## Advantages

1. Combines price patterns, trend confirmation, and momentum indicators for comprehensive trading signals.
2. The 1-2-3 pattern is a common and reliable price pattern that effectively captures potential trend reversals.
3. Uses EMA and MACD indicators to further confirm trend direction and momentum, enhancing signal reliability.
4. Clear entry and exit rules, making it easy to understand and implement.

## Risk Analysis

1. The strategy relies on a single timeframe, potentially missing important information from other timeframes.
2. May generate false signals during choppy markets or when the trend is unclear.
3. Does not consider risk management such as stop-loss and position sizing, which could lead to significant losses.
4. Strategy parameters are not optimized and may not be suitable for all market conditions.

## Optimization Directions

1. Incorporate multi-timeframe analysis to confirm trend consistency across different time scales.
2. Implement risk management measures such as dynamic stop-loss based on ATR and position sizing.
3. Optimize strategy parameters (EMA periods, MACD settings) to adapt to different market conditions.
4. Consider adding other technical or market sentiment indicators to enhance signal reliability.

## Summary

This strategy provides a comprehensive approach to identify potential buy and sell signals using the 1-2-3 pattern, EMAs, and MACD. It combines price patterns, trend confirmation, and momentum indicators to generate reliable trading signals. Limitations include lack of risk management and parameter optimization. With multi-timeframe analysis, dynamic stop-loss, and parameter optimization, performance can be significantly improved.

## Pine Script Source

```pinescript
//@version=5
strategy("1-2-3 Pattern Strategy with EMAs, MACD, and 4th Candle Extension", overlay=true)

// Define conditions for the 1-2-3 pattern for buy orders
buy_candle1_above_open = close[3] > open[3]
buy_candle2_below_open = close[2] < open[2]
buy_candle3_above_close = close[1] > close[3]
buy_candle4_above_close = close > close[3]

// Define conditions for the 1-2-3 pattern for sell orders
sell_candle1_below_open = close[3] < open[3]
sell_candle2_above_open = close[2] > open[2]
sell_candle3_below_close = close[1] < close[3]
sell_candle4_below_close = close < close[3]

// Fetch 9 EMA, 20 EMA, and MACD
ema_9 = ta.ema(close, 9)
ema_20 = ta.ema(close, 20)
[macd_line, signal_line, _] = ta.macd(close, 12, 26, 9)

// Buy logic
if (buy_candle1_above_open and buy_candle2_below_open and buy_candle3_above_close and buy_candle4_above_close and strategy.opentrades == 0 and close > ema_9 and close > ema_20 and macd_line > signal_line)
    strategy.entry("Buy", strategy.long, qty=5)
if (close < open and strategy.opentrades > 0)
    strategy.close("Buy", qty=5)

// Sell logic
if (sell_candle1_below_open and sell_candle2_above_open and sell_candle3_below_close and sell_candle4_below_close and strategy.opentrades == 0 and close < ema_9 and close < ema_20 and macd_line < signal_line)
    strategy.entry("Sell", strategy.short, qty=5)
if (close > open and strategy.opentrades > 0)
    strategy.close("Sell", qty=5)
```

## Backtest Parameters
- Period: 2024-02-01 to 2024-02-29
- Timeframe: 1h (base: 15m)
- Exchange: Futures Binance BTC/USDT

## Key Indicators
- **EMA 9**: Short-term trend
- **EMA 20**: Medium-term trend
- **MACD (12, 26, 9)**: Momentum confirmation
