``` pinescript
/*backtest
start: 2023-12-20 00:00:00
end: 2024-12-18 08:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title="Swing Strategy (<30% DD)", shorttitle="SwingStratDD", overlay=true)

//-----------------------------------------------------
// Example Indicators and Logic
//-----------------------------------------------------
emaLen   = input.int(200, "EMA Length", minval=1)
emaValue = ta.ema(close, emaLen)

plot(emaValue, color=color.yellow, linewidth=2, title="EMA 200")

//-----------------------------------------------------
// User Inputs
//-----------------------------------------------------
adxLen           = input.int(14,  "ADX Length",      minval=1)
rsiLen           = input.int(14,  "RSI Length",      minval=1)
atrLen           = input.int(14,  "ATR Length",      minval=1)

rsiBuyThresh     = input.float(60, "RSI Buy Threshold",     minval=1, maxval=100)
adxThresh        = input.float(25, "ADX Threshold (Trend)", minval=1, maxval=100)
minVolume        = input.float(1e6,"Minimum Volume",         minval=1)
minATR           = input.float(2,  "Minimum ATR(14)",        minval=0.1, step=0.1)

stopLossPerc     = input.float(15, "Stop-Loss %",            minval=0.1, step=0.1)
// We’ll do two partial take-profit levels to aim for consistent cashflow:
takeProfit1Perc  = input.float(15, "Take-Profit1 %",         minval=0.1, maxval=30)
takeProfit2Perc  = input.float(30, "Take-Profit2 %",         minval=0.1, maxval=30)

//-----------------------------------------------------
// Strategy Logic
//-----------------------------------------------------
inTrend        = taADX > adxThresh and close > ta.sma(close, emaLen)
rsiMomentum    = rsi(rsiLen) > rsiBuyThresh
volumeOk       = volume > minVolume
atrVolatility  = ta.atr(atrLen) > minATR

isEntrySignal  = inTrend and rsiMomentum and volumeOk and atrVolatility

if (isEntrySignal)
    strategy.entry("Long", strategy.long)

//-----------------------------------------------------
// Take-Profit and Stop-Loss Logic
//-----------------------------------------------------
takeProfit1Level  = strategy.position_avg_price * (1 + takeProfit1Perc / 100)
takeProfit2Level  = strategy.position_avg_price * (1 + takeProfit2Perc / 100)

strategy.exit("Take Profit 1", from_entry="Long", profit_percent=takeProfit1Perc)
strategy.exit("Take Profit 2", from_entry="Long", profit_percent=takeProfit2Perc)

strategy.exit("Stop Loss", from_entry="Long", stop=stopLossPerc)

//-----------------------------------------------------
// Drawdown Monitoring
//-----------------------------------------------------
drawdownLevel = ta.lowest(low, barssince(isEntrySignal), 1)
if (ta.valuewhen(drawdownLevel > strategy.equity * (1 - stopLossPerc / 100), drawdownLevel, 0) < strategy.equity)
    strategy.close("Long")

plotshape(series=isEntrySignal, location=location.belowbar, color=color.green, style=shape.labelup, text="Entry")
plotshape(series=strategy.closed_trades.entry_price(strategy.long, bar_index) > 0, location=location.abovebar, color=color.red, style=shape.labeldown, text="Exit")

```

```