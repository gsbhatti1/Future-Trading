``` pinescript
/*backtest
start: 2023-01-16 00:00:00
end: 2024-01-22 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
// © ChaoZhang
strategy(title='MACD and RSI', overlay=true, shorttitle='MACD&RSI')
//MACD Settings
fastMA = input.int(title='Fast moving average', defval=12, minval=1)
slowMA = input.int(title='Slow moving average', defval=26, minval=1)
signalLength = input.int(9, minval=1)

//RSI settings
RSIOverSold = input.int(35, minval=1)
RSIOverBought = input.int(80, minval=1)
src = close
len = input.int(14, minval=1, title='Length')
up = ta.rma(math.max(ta.change(src), 0), len)
down = ta.rma(-math.min(ta.change(src), 0),
```