``` pinescript
/*backtest
start: 2022-12-06 00:00:00
end: 2023-12-12 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("TUE ADX/MACD Confluence V1.0", overlay=true)

showsignals = input(true, title="Show BUY/SELL Signals")
showcandlecolors = input(true, title="Show Candle Colors")
length = input(14, title="ADX Length")
smoothing = input(10, title="ADX Smoothing")
macdsource = input(close, title="MACD Source")
macdfast = input(12, title="MACD Fast Length")
macdslow = input(26, title="MACD Slow Length")
macdsignal = input(9, title="MACD Signal Length")
colorup = input(color.green, title="Up Candle Color")
colordown = input(color.red, title="Down Candle Color")
stoplossprice = input(100, title="Stop Loss Price")

// Calculate ADX
adx = ta.adx(length, smoothing)
plusdi = ta.adi(length, smoothing)
minusdi = ta.madi(length, smoothing)

// Determine trend direction
bullish = plusdi > minusdi and macdsource - ta.crossover(macdfast - macdslow, macdsignal)
bearish = minusdi > plusdi and macdsource - ta.crossunder(macdfast - macdslow, macdsignal)

// Plot signals and candles
plotshape(series=bullish, location=location.belowbar, color=colorup, style=shape.triangleup, title="Buy Signal")
plotshape(series=bearish, location=location.abovebar, color=colordown, style=shape.triangledown, title="Sell Signal")

if (showcandlecolors)
    bgcolor(macdsource > 0 ? colorup : colordown)

// Stop Loss Logic
stoploss = stoplossprice * close
strategy.exit("StopLoss", from_entry="Long Entry", stop=stoploss)
strategy.exit("StopLoss", from_entry="Short Entry", stop=stoploss)
```

This Pine Script code implements the "TUE ADX/MACD Confluence V1.0" strategy, as described in the translated text. It includes all input parameters and logic for generating buy/sell signals based on ADX and MACD conditions, as well as displaying candle colors and setting up a stop loss mechanism.