# 1-3-1 Red Green Candlestick Reversal Strategy

**Author:** ChaoZhang

## Overview

The 1-3-1 red green candlestick reversal strategy generates buy and sell signals based on candlestick patterns. It looks for buying opportunities when 1 red candlestick is reversed by 3 subsequent green candlesticks.

## Principles

The core logic of this strategy is:

1. Check if the current candlestick is a red candle (close price lower than open price)
2. Check if the previous 3 candlesticks are green candles (close price higher than open price)
3. Check if the last green candle's close price is higher than the previous 2 green candles
4. If the above conditions are met, go long at the close of the red candle
5. Set stop loss at the lowest price of the red candle
6. Set take profit at entry price plus the distance from entry to stop loss

With this strategy, we can buy when the red candle is reversed, because the subsequent trend is likely upwards. Stop loss and take profit are set to control risk and lock in profits.

## Advantage Analysis

1. Simple and clear logic, easy to understand and implement
2. Utilizes candlestick pattern features without reliance on indicators, avoiding overoptimization problems
3. Has clear entry and exit rules for objective execution
4. Sets stop loss and take profit to control risk/reward of each trade
5. Good backtest results, likely to translate well to live trading

## Risk Analysis

1. Candlestick patterns cannot perfectly predict future moves, some uncertainty exists
2. Only one entry, may have lower win rate due to stock specifics
3. No consideration of market trend, risk holding during sustained downtrend
4. Does not account for trading costs and slippage, actual performance may be worse

**Solutions:**
1. Consider combining with MA filters to improve entry success rate
2. Adjust position sizing, scale in across multiple entries
3. Dynamically adjust stop loss based on market conditions
4. Test different stop loss/take profit ratios

## Optimization Directions

1. **Market index filtering** - Filter signals based on short/medium term market trend
2. **Volume confirmation** - Only go long if green candle volumes increase
3. **Optimize stop loss/take profit ratios** - Test different ratios to find optimal parameters
4. **Position sizing optimization** - Scale in across multiple entries to reduce single trade risk
5. **Additional filters** - MA, volatility etc to ensure high probability entry
6. **Machine learning** - Train optimal parameter thresholds via ML on big data

## Summary

The 1-3-1 red green candlestick reversal strategy is a simple and practical short-term trading strategy. It has clear entry and exit rules and good backtest results. With optimization measures, it can become a reliable quantitative trading strategy. Risk management is essential.

## Pine Script Source

```pinescript
//@version=5
strategy("1-3-1 Red Green Candlestick Reversal", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

var float stopLossPrice = na
var float takeProfitPrice = na
var float stopLossPriceD = na
var float takeProfitPriceD = na

// Check conditions
redCandle = close[3] < open[3] and low[3] < low[2] and low[3] < low[1] and low[3] < low[0]
greenCandles = close > open and close[1] > open[1] and close[2] > open[2]
higherClose = close > close[1] and close[1] > close[2]

// Calculate stop loss
if (redCandle and greenCandles and higherClose) and strategy.position_size == 0
    stopLossPrice := low[3]

// Calculate take profit
if (not na(stopLossPrice)) and strategy.position_size == 0
    takeProfitPrice := close + (close - stopLossPrice)

// Entry
if (redCandle and greenCandles and higherClose) and strategy.position_size == 0
    strategy.entry("Long", strategy.long)

// Exit
if (not na(stopLossPrice)) and strategy.position_size > 0
    strategy.exit("TP/SL", stop=stopLossPrice, limit=takeProfitPrice)

if strategy.position_size == 0
    stopLossPriceD := na
    takeProfitPriceD := na
else
    stopLossPriceD := stopLossPrice
    takeProfitPriceD := takeProfitPrice

plotshape(series=redCandle and greenCandles and higherClose and strategy.position_size == 0, title="Entry Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plot(stopLossPriceD, color=color.red, title="Stop Loss", linewidth=2, style=plot.style_linebr)
plot(takeProfitPriceD, color=color.green, title="Take Profit", linewidth=2, style=plot.style_linebr)
```

## Key Parameters
- **Pattern**: 1 red candle followed by 3 green candles with higher closes
- **Stop Loss**: Low of the red candle
- **Take Profit**: Entry + (Entry - Stop Loss)
