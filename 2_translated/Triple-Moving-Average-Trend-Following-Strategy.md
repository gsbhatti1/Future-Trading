``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// LOVE JOY PEACE PATIENCE KINDNESS GOODNESS FAITHFULNESS GENTLENESS SELF-CONTROL 
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © JoshuaMcGowan

//@version=4

// 1. Define strategy settings
strategy(title="Triple Moving Average", overlay=true,
     pyramiding=0, initial_capital=1000,
     commission_type=strategy.commission.cash_per_order,
     commission_value=4, slippage=2)
     
fastMALen = input(title="Fast MA Length", type=input.integer, defval=8)
medMALen  = input(title="Medium MA Length", type=input.integer, defval=21)
slowMALen = input(title="Slow MA Length", type=input.integer, defval=55)

// === INPUT BACKTEST RANGE ===
FromMonth = input(defval = 12, title = "From Month", minval = 1, maxval = 12)
FromDay   = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
FromYear  = input(defval = 2016, title = "From Year", minval = 2017)
ToMonth   = input(defval = 1, title = "To Month", minval = 1, maxval = 12)
ToDay     = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
ToYear    = input(defval = 9999, title = "To Year", minval = 2017)

// === FUNCTION EXAMPLE ===
start     = timestamp(FromYear, FromMonth, FromDay, 00, 00)  // backtest start window
finish    = timestamp(ToYear, ToMonth, ToDay, 23, 59)        // backtest finish window
window()  => true

usePosSize = input(title="Use Position Sizing?", type=input.bool, defval=true)
riskPcnt   = input(title="% Risk", type=input.float, defval=0.5)

// === BACKTEST RANGE ===
if (time >= start and time <= finish) 
    window()

// === CALCULATE MOVING AVERAGES ===
fastMA = sma(close, fastMALen)
medMA  = sma(close, medMALen)
slowMA = sma(close, slowMALen)

// === ENTRY AND EXIT CONDITIONS ===
longCond = ta.crossover(fastMA, medMA) and (ta.trend(up, fastMA, 0) and ta.trend(up, medMA, 0) and ta.trend(up, slowMA, 0))
shortCond= ta.crossunder(fastMA, medMA) and (ta.trend(down, fastMA, 0) and ta.trend(down, medMA, 0) and ta.trend(down, slowMA, 0))

// === TRIGGER ENTRY AND EXIT BASED ON CONDITIONS ===
if (longCond)
    strategy.entry("Long", strategy.long)

if (shortCond)
    strategy.entry("Short", strategy.short)

// === EXIT CONDITION ===
exitCond = ta.crossover(fastMA, medMA) or ta.crossunder(fastMA, medMA)
if (exitCond)
    strategy.close("Long")
    strategy.close("Short")

// === POSITION SIZING ===
positionSize = riskPcnt * portfolio.value
strategy.entry("Long", strategy.long, size=math.round(positionSize))
strategy.entry("Short", strategy.short, size=math.round(positionSize))

```

This script sets up a triple moving average trend-following strategy with adjustable parameters for backtesting and live trading. It includes input fields for defining the backtest range and position sizing.