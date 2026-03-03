> Name

Dual-MA-Crossover-Trend-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1afddbdb85ac7f60eaa.png)
[trans]

## Overview

This strategy adopts the typical trend tracking method of dual moving average crossover, combined with risk management mechanisms such as stop loss, take profit, and trailing stop loss, aiming to capture large profits from trending markets.

## Strategy Logic

1. Calculate the n-day EMA as the fast line for short term;  
2. Calculate the m-day EMA as the slow line for long term;
3. Go long when the fast line breaks through the slow line upwards, and go short when breaks downwards;  
4. Exit signal: reverse crossover (e.g., exit long when a long crossover occurs).
5. Use stop loss, take profit, and trailing stop loss to manage risks.

## Advantage Analysis

1. Adopting dual EMA lines can better determine price trend reversal points and capture trending moves.
2. Combining stop loss, take profit, and trailing stop helps limit single trade loss, lock in profits, and reduce drawdown.
3. There are many customizable parameters to adjust and optimize for different products and market environments.  
4. The strategy logic is simple and clear, easy to understand and modify.
5. Support both long and short operations, adaptable to different market conditions.

## Risk Analysis

1. Dual MA strategies are very sensitive to false breakouts and prone to being trapped.
2. Improper parameter settings may lead to frequent trading, increasing trading costs and slippage losses. 
3. The strategy itself cannot determine trend reversal points, needs to be combined with other indicators.  
4. It’s easy to generate trading signals in ranging markets, but actual profitability tends to be low.
5. Parameters need to be optimized for different products and market environments.

Risks can be reduced by:
1. Filtering false signals with other indicators.  
2. Optimizing parameters to lower trading frequency. 
3. Adding trend-judging indicators to avoid range-bound market trades.
4. Adjusting position sizing to lower single trade risks.  

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Optimize fast and slow MA periods for different products and markets.  
2. Add other indicators to determine trends and filter false signals, e.g MACD, KDJ etc.
3. Consider replacing EMA with SMA or WMA.  
4. Dynamically adjust stop loss based on ATR.
5. Flexibly adjust single position sizes based on position sizing methodology. 
6. Parameter self-adaptive optimization based on correlation and volatility metrics.

## Summary

In summary, this is a typical dual EMA crossover trend tracking strategy. It has the advantage of capturing trending moves, integrated with risk management mechanisms like stop loss, take profit, and trailing stop loss. But it also has some typical weaknesses, such as high sensitivity toward noise and range-bound markets, prone to being trapped. Further improvements can be made by introducing additional indicators, parameters optimization, dynamic adjustments, and portfolio usage to enhance the strategy's performance. Overall speaking, with proper parameter tuning and good fitness with product and market conditions, this strategy can achieve decent results.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1_open|0|Fast MA Source: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|14|Fast MA Period|
|v_input_3_open|0|Slow MA Source: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|21|Slow MA Period|
|v_input_5|false|Invert Trade Direction?|
|v_input_6|1000|Take Profit|
|v_input_7|200|Stop Loss|
|v_input_8|200|Trailing Stop Loss|
|v_input_9|false|Trailing Stop Loss Offset|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-20 00:00:00
end: 2023-12-20 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2

strategy(title = "Dual-MA-Crossover-Trend-Tracking-Strategy", shorttitle = "DMCTS", overlay = true)

// === INPUTS ===
// Fast MA
maFastSource   = input(defval = open, title = "Fast MA Source")
maFastLength   = input(defval = 14, title = "Fast MA Period", minval = 1)
// Slow MA
maSlowSource   = input(defval = open, title = "Slow MA Source")
maSlowLength   = input(defval = 21, title = "Slow MA Period", minval = 1)

// === TRADING INPUTS ===
tradeInvert     = input(defval = false, title = "Invert Trade Direction?")
// Risk management inputs
takeProfit     = input(defval = 1000, title = "Take Profit", minval = 0)
stopLoss       = input(defval = 200, title = "Stop Loss", minval = 0)
trailStop      = input(defval = 200, title = "Trailing Stop", minval = 0)
trailOffset    = input(defval = false, title = "Trailing Stop Offset")

// === STRATEGY LOGIC ===
fastMA         = ema(close, maFastLength)
slowMA         = ema(close, maSlowLength)

if (not na(fastMA) and not na(slowMA))
    // Long entry condition
    if fastMA > slowMA and not tradeInvert or (tradeInvert and fastMA < slowMA)
        strategy.entry("Long", strategy.long)
    
    // Short entry condition
    if fastMA < slowMA and not tradeInvert or (tradeInvert and fastMA > slowMA)
        strategy.entry("Short", strategy.short)

    // Exit conditions based on crossovers
    if fastMA < slowMA and not tradeInvert or (tradeInvert and fastMA > slowMA)
        strategy.close("Long")
    
    if fastMA > slowMA and not tradeInvert or (tradeInvert and fastMA < slowMA)
        strategy.close("Short")

// === RISK MANAGEMENT ===
trailStopPrice = na(trailOffset) ? takeProfit : stopLoss + trailOffset * close

if (strategy.position_size > 0)
    strategy.exit("Take Profit", "Long", limit=takeProfit, stop=trailStopPrice)
else if (strategy.position_size < 0)
    strategy.exit("Take Profit", "Short", limit=takeProfit, stop=trailStopPrice)

if (strategy.position_size > 0)
    strategy.exit("Stop Loss", "Long", stop=stopLoss)
else if (strategy.position_size < 0)
    strategy.exit("Stop Loss", "Short", stop=stopLoss)

// === TRAILING STOP ===
if (strategy.position_size > 0)
    strategy.exit("Trailing Stop", "Long", limit=trailStop + close, stop=close - trailStopPrice)
else if (strategy.position_size < 0)
    strategy.exit("Trailing Stop", "Short", limit=-trailStop + close, stop=close + trailStopPrice)

```

This completes the translation and retains all code blocks, numbers, and formatting as in the original document.