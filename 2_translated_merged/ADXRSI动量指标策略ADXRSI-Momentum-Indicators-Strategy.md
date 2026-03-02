``` pinescript
/*backtest
start: 2023-11-10 00:00:00
end: 2023-12-01 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("ADXRSI动量指标策略", overlay=true)

// 参数设置
adxlen = input(14, title="ADX Smoothing")
dilen = input(14, title="DI Length")
threshold = input(20, title="threshold")
rsiperiodo = input(7, title="Periodo RSI")
oversold_level = input(30, title="Livello Ipervenduto")
overbought_level = input(70, title="Livello Ipercomprato")
bbperiod = input(50, title="Periodo BB")
bbdev = input(2, title="Dev BB")

// 计算ADX
adx = ta.adx(dilen, adxlen)

// 计算RSI
rsi = ta.rsi(close, rsiperiodo)

// 计算Bollinger Bands
bbands = ta.bband(close, bbperiod, bbdev)

long_condition = adx > 32 and rsi < oversold_level and close < bbands[1].lower
short_condition = adx > 32 and rsi > overbought_level and close > bbands[1].upper

// 买入条件
if (long_condition)
    strategy.entry("Long", strategy.long)

// 卖出条件
if (short_condition)
    strategy.exit("Short Exit", from_entry="Long")

// 设置止损止盈
strategy.exit("Stop Loss", "Long", stop=bbands[1].lower, limit=close + 5 * bbdev)
```

This Pine Script translates the provided Chinese documentation into English while maintaining the original code structure and functionality.