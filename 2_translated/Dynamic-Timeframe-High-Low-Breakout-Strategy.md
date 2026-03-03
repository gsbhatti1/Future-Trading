``` pinescript
/*backtest
start: 2023-05-28 00:00:00
end: 2024-06-02 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Dynamic-Timeframe-High-Low-Breakout-Strategy", overlay=true)

// Define input options for point settings and timeframe
points = input.int(60, title="Point Threshold", minval=1, step=1)
timeframe = input.timeframe("60", title="Timeframe", options=["1", "3", "5", "15", "30", "60", "240", "D", "W", "M"])

// Calculate high and low of the selected timeframe
high_timeframe = request.security(syminfo.ti
```