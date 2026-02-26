``` pinescript
/*backtest
start: 2024-01-04 00:00:00
end: 2024-02-03 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
//© Densz
strategy("Triple Exponential Moving Average Profit Taking and Stop Loss Strategy (ATR)", overlay=true )

// INPUTS
startTime           =       input(title="Start Time", type=input.time, defval=timestamp("01 Jan 2017 00:00 +0000"))
endTime             =       input(title="End Time", type=input.time, defval=timestamp("01 Jan 2022 00:00 +0000"))

slowEMALength       =       input(title="Slow EMA Length", type=input.integer, defval=55)
middleEMALength     =       input(title="Middle EMA Length", type=input.integer, defval=21)
fastEMALength       =       input(title="Fast EMA Length", type=input.integer, defval=9)

trendMALength       =       input(title="Trend indicator MA Length", type=input.integer, defval=200)

atrLength           =       input(title="ATR Length", type=input.integer, defval=14)
tpATRMult           =       input(title="Take profit ATR multiplier", type=input.integer, defval=3)
slATRMult           =       input(title="Stop loss ATR multiplier", type=input.integer, defval=2)

rsiLength           =       input(title="RSI Length", type=input.integer, defval=14)

// Indicators
slowEMA             =       ema(close, slowEMALength)
middEMA             =       ema(close, middleEMALength)
fastEMA             =       ema(close, fastEMALength)
atr                 =       atr(atrLength)

rsiValue            =       rsi(close, rsiLength)
isRsiOB             =       rsiValue >= 80
isRsiOS             =       rsiValue <= 20

sma200              =       sma(close, trendMALength)

inDateRange         =       true

// Plotting
plot(slowEMA, title="Slow EMA", color=color.red, linewidth=2, transp=50)
plot(middEMA, title="Middle EMA", color=color.orange, linewidth=2, transp=50)
plot(fastEMA, title="Fast EMA", color=color.green, linewidth=2, transp=50)

plot(sma200, title="SMA Trend indicator", color=color.purple, linewidth=3, transp=10)
plotshape(isRsiOB, title="Overbought", location=location.abovebar, color=color.red, transp=0, style=shape.triangledown, text="OB")
plotshape(isRsiOS, title="Oversold", location=location.belowbar, color=color.green, transp=0, style=shape.triangleup, text="OS")

// Strategy Logic
if (middEMA > slowEMA and not inDateRange)
    order = strategy.entry("Long", strategy.long)

if (fastEMA < middEMA)
    strategy.close("Long")

// Stop Loss and Take Profit Levels
takeProfitLevel     =       close + atr * tpATRMult
stopLossLevel       =       close - atr * slATRMult

strategy.exit("Take profit or stop loss", "Long", limit=takeProfitLevel, stop=stopLossLevel)
```

This Pine Script translates the provided Chinese strategy into English and maintains the original formatting. The strategy logic is updated to reflect the proper use of `strategy.entry` and `strategy.close`.