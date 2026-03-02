``` pinescript
/*backtest
start: 2023-10-30 00:00:00
end: 2023-11-06 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © mohanee

//@version=4
strategy("EMA_cumulativeVolume_crossover[Strategy]", overlay=true, pyramiding=5, default_qty_type=strategy.percent_of_equity, default_qty_value=20, initial_capital=10000)


emaLength = input(25, title="EMA Length", minval=1, maxval=200)
cumulativePeriod = input(100, title="cumulative volume Period", minval=1, maxval=200)

riskCapital = input(title="Risk % of capital", defval=10, minval=1)
stopLoss = input(8, title="Stop Loss", minval=1)
takePartialProfits = input(true, title="take partial profits (percentage same as stop loss)")

tradeDirection = input(title="Trade Direction", defval="LONG", options=["LONG", "SHORT"])

avgPrice = (high + low + close) / 3
avgPriceVolume = avgPrice * volume

cumulPriceVolume = sum(avgPriceVolume, cumulativePeriod)
cumulVolume = sum(volume, cumulativePeriod)

cumValue = cumulPriceVolume / cumulVolume

emaVal = ema(close, emaLength)

emaCumValue1 = ema(cumValue, emaLength)
emaCumValue2 = ema(cumValue, emaLength * 2)

emaCumValueHistory = ema(cumValue[emaLength], emaLength)


//vwapVal1 = vwap(hlc3)

rsiVal = rsi(close, 5)

plotEma = plot(emaVal, title="EMA", color=color.green, transp=25)
// plot(vwapValue, title="Cumulate Volumne", color=color.orange, linewidth=2, transp=25)
// plot(vwapVal1, title="vwapVal1", color=color.purple, linewidth=1, transp=25)
plotCum = plot(emaCumValue1, title="emaVwapValue", color=color.purple, linewidth=2, transp=35)
plot(emaCumValue2, title="emaVwapValue", color=color.yellow, linewidth=3, transp=25)
fill(plotEma, plotCum, color=emaVal > emaCumValue1 ? color.lime : color.red, transp=35, title="ema and cum area")

plot(rsiVal, title="RSI", color=color.blue, linewidth=1)

// Buy logic
if (tradeDirection == "LONG")
    if close > emaVal
        strategy.entry("Long Entry", strategy.long)
        
    if rsiVal > 90
        takePartialProfits ? strategy.exit("Take Profit 1/3", from_entry="Long Entry", limit=(strategy.position_avg_price * (1 + riskCapital / 100))) : ""

    if close < emaVal
        strategy.close("Long Exit")

// Sell logic
if (tradeDirection == "SHORT")
    if close > emaVal
        strategy.entry("Short Entry", strategy.short)
        
    if rsiVal > 90
        takePartialProfits ? strategy.exit("Take Profit 1/3", from_entry="Short Entry", limit=(strategy.position_avg_price * (1 - riskCapital / 100))) : ""

    if close < emaVal
        strategy.close("Short Exit")

// Stop Loss logic
if tradeDirection == "LONG"
    strategy.exit("Stop Loss Long", from_entry="Long Entry", stop=(strategy.entry_price * (1 - stopLoss / 100)))
    
if tradeDirection == "SHORT"
    strategy.exit("Stop Loss Short", from_entry="Short Entry", stop=(strategy.entry_price * (1 + stopLoss / 100)))

// Plotting
plot(emaVal, title="EMA", color=color.green, transp=25)
plot(emaCumValue1, title="cumulative EMA Value", color=color.purple, linewidth=2, transp=35)
plot(emaCumValue2, title="double cumulative EMA Value", color=color.yellow, linewidth=3, transp=25)
```