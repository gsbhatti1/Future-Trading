``` pinescript
``` pinescript
/*backtest
start: 2025-01-27 00:00:00
end: 2025-02-20 00:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Binance","currency":"SOL_USDT"}]
*/

//@version=5
strategy("Nifty/BankNifty Multi-Strategy v2", overlay=true, margin_long=100, margin_short=100)

// ———— Inputs ———— //
// Supertrend
atrPeriod = input.int(10, "ATR Period")
supertrendMultiplier = input.float(2.0, "Supertrend Multiplier", step=0.1)

// EMA
ema20Period = input.int(20, "20 EMA Period")
ema50Period = input.int(50, "50 EMA Period")

// ADX/DMI
adxThreshold = input.int(25, "ADX Trend Threshold")
adxLength = input.int(14, "ADX Length")

// RSI
rsiLength = input.int(14, "RSI Length")
rsiOverbought = input.int(70, "RSI Overbought")
rsiOversold = input.int(30, "RSI Oversold")

// Bollinger Bands
bbLength = input.int(20, "BB Length")
bbStdDev = input.float(2.0, "BB Std Dev", step=0.1)

// Stop-Loss
stopLossPerc = input.float(1.0, "Stop-Loss %", step=0.1)

// ———— Calculations ———— //
// Supertrend
[supertrend, direction] = ta.supertrend(supertrendMultiplier, atrPeriod)

// EMAs
ema20 = ta.ema(close, ema20Period)
ema50 = ta.ema(close, ema50Period)

// ADX via DMI (corrected)
[dip, din, adx] = ta.dmi(adxLength, adxLength) // ta.dmi(diLength, adxSmoothing)

// RSI
rsi = ta.rsi(close, rsiLength)

// Bollinger Bands
basis = ta.sma(close, bbLength)
upperBB = basis + ta.stdev(close, bbLength) * bbStdDev
lowerBB = basis - ta.stdev(close, bbLength) * bbStdDev

// VWAP
vwapValue = ta.vwap(hlc3)

// ———— Strategy Logic ———— //
trendingMarket = adx > adxThreshold
rangeMarket = adx < adxThreshold

// Entry Conditions
longCondition = trendingMarket and (direction == 1 or (ema20 > ema50 and close > vwapValue))
shortCondition = trendingMarket and (direction == -1 or (ema20 < ema50 and close < vwapValue))

// Exit Conditions
stopLoss = stopLossPerc * syminfo.mintick

// Long Position
if (longCondition)
    strategy.entry("Long", strategy.long, when=longCondition)
    strategy.exit("Stop Loss", "Long", stop=stopLoss * close)

// Short Position
if (shortCondition)
    strategy.entry("Short", strategy.short, when=shortCondition)
    strategy.exit("Stop Loss", "Short", stop=stopLoss * close)

// Range Trading
if (rangeMarket)
    // Buy when price touches lower BB and RSI is oversold
    if (close <= lowerBB and rsi <= rsiOversold)
        strategy.entry("Buy", strategy.long, when=rangeMarket)
    // Sell when price touches upper BB and RSI is overbought
    if (close >= upperBB and rsi >= rsiOverbought)
        strategy.entry("Sell", strategy.short, when=rangeMarket)
```
```