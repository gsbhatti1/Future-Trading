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
strategy("EMA_cumulativeVolume_crossover[Strategy]", overlay=true, pyramiding=5, default_qty_type=strategy.percent_of_equity,  default_qty_value=20, initial_capital=10000)


emaLength = input(25, title="EMA Length", minval=1, maxval=200)
cumulativePeriod = input(100,  title="cumulative volume Period", minval=1, maxval=200)

riskCapital = input(title="Risk % of capital", defval=10, minval=1)
stopLoss=input(8,title="Stop Loss",minval=1)
takePartialProfits=input(true, title="Take partial profits (percentage same as stop loss)")

tradeDirection=input(title="Trade Direction", defval="LONG", options=["LONG", "SHORT"])

avgPrice = (high + low + close) / 3
avgPriceVolume = avgPrice * volume

cumulPriceVolume = sum(avgPriceVolume, cumulativePeriod)
cumulVolume = sum(volume, cumulativePeriod)

cumValue = cumulPriceVolume / cumulVolume

emaVal=ema(close, emaLength)

emaCumValue1=ema(cumValue, emaLength)
emaCumValue2=ema(cumValue, emaLength*2)

emaCumValueHistory=ema(cumValue[emaLength], emaLength)


//vwapVal1=vwap(hlc3)

rsiVal=rsi(close,5)

plotEma=plot(emaVal, title="EMA", color=color.green,  transp=25)
//plot(vwapValue, title="Cumulate Volumne", color=color.orange,  linewidth=2, transp=25)
//plot(vwapVal1, title="vwapVal1", color=color.purple,  linewidth=1, transp=25)
plotCum=plot(emaCumValue1, title="emaVwapValue", color=color.purple,  linewidth=2, transp=35)
plot(emaCumValue2, title="emaVwapValue", color=color.yellow,  linewidth=3, transp=25)
fill(plotEma,plotCum, color=emaVal>emaCumValue1 ? color.lime : color.red, transp=35, title="ema and cum area")

plot(rsiVal, title="RSI", color=color.blue, linewidth=2)

buyCondition = close > emaCumValue1
sellCondition = close < emaCumValue1

if (tradeDirection == "LONG")
    if (buyCondition)
        strategy.entry("Buy", strategy.long)
    
    // Check for profit taking
    if (rsiVal > 90 and takePartialProfits)
        strategy.exit("Take Profit", from_entry="Buy", limit=emaCumValue1 + rsiVal * riskCapital)

if (tradeDirection == "SHORT")
    if (sellCondition)
        strategy.entry("Sell", strategy.short)

    // Check for stop loss
    if (rsiVal < 10 and takePartialProfits)
        strategy.exit("Stop Loss", from_entry="Sell", stop=emaCumValue1 - rsiVal * riskCapital)

stopLossPrice = emaVal - stopLoss / 100 * emaVal

if (tradeDirection == "LONG")
    strategy.exit("Stop Loss", from_entry="Buy", stop=stopLossPrice)
    
if (tradeDirection == "SHORT")
    strategy.exit("Stop Loss", from_entry="Sell", stop=stopLossPrice)

```
```