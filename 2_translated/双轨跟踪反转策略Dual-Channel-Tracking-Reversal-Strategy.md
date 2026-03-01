``` pinescript
/*backtest
start: 2023-10-02 00:00:00
end: 2023-11-01 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// Credit for the initial Squeeze Momentum code to LazyBear, rate of change code is from Kiasaki
strategy("Squeeze X BF ?", overlay=false, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.0)

/////////////// Time Frame ///////////////
testStartYear = input(2012, "Backtest Start Year") 
testStartMonth = input(1, "Backtest Start Month")
testStartDay = input(1, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay, 0, 0)

testStopYear = input(2019, "Backtest Stop Year")
testStopMonth = input(12, "Backtest Stop Month")
testStopDay = input(31, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear,testStopMonth,testStopDay, 0, 0)

testPeriod() => true

/////////////// Squeeeeze ///////////////
length = input(20, title="BB Length")
mult = input(2.0,title="BB MultFactor")
lengthKC=input(22, title="KC Length")
multKC = input(1.5, title="KC MultFactor")

source = close
basis = sma(source, length)
dev = mult * stdev(source, length)

upperBB = basis + dev
lowerBB = basis - dev

srcKC = close
kcMa = sma(srcKC, lengthKC)
trueRange = ta.highest(high - low, 14) + (high - low)[1] + (low - high)[1]
kcHlAvg = (high + low) / 2
upperKC = kcMa + multKC * trueRange
lowerKC = kcMa - multKC * trueRange

isSqueeze = lowerBB > lowerKC and upperBB < upperKC
val = ta.slope(ta.linearreg(srcKC, [basis, basis]), 10)
roc = (srcKC - srcKC[12]) / srcKC[12]
stopLossPct = input(100.0, "Stop Loss %")
takeProfitPct = input(5000.0, "Take Profit %")

if isSqueeze and val > 0 and roc > stopLossPct
    strategy.entry("Long", strategy.long)
else if isSqueeze and val < 0 and roc < -stopLossPct
    strategy.entry("Short", strategy.short)

strategy.exit("Stop Loss", "Long", loss=stopLossPct * close / 100.0, profit=takeProfitPct * close / 100.0)
strategy.exit("Stop Loss", "Short", loss=stopLossPct * close / 100.0, profit=takeProfitPct * close / 100.0)

plot(isSqueeze ? color.green : color.red, title="Squeeze")
```

This Pine Script code implements the Dual-Channel-Tracking-Reversal-Strategy as described in the translated document. The script includes time frame settings for backtesting, Bollinger Bands and Keltner Channels calculations, and entry/exit logic based on the conditions defined in the strategy description.