``` pinescript
/*backtest
start: 2024-03-11 00:00:00
end: 2024-03-15 09:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("RMM_byMR", overlay=true)

// RSI length input
rsiLength = input(14, title="RSI Uzunluğu")

// Overbought and oversold levels inputs
overboughtLevel = input(70, title="Aşırı Alım Seviyesi")
oversoldLevel = input(30, title="Aşırı Satım Seviyesi")

// RSI calculation
rsiValue = rsi(close, rsiLength)

// Detect last peak points // Detect last valley points
```