> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|20|Short MA Length|
|v_input_int_2|50|Long MA Length|
|v_input_int_3|200|Long MA 200 Length|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-03-23 00:00:00
end: 2024-03-28 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("EMA Crossover Strategy by Peter Gangmei", overlay=true)

// Define the length for moving averages
short_ma_length = input.int(20, "Short MA Length")
long_ma_length = input.int(50, "Long MA Length")
long_ma_200_length = input.int(200, "Long MA 200 Length")

// Define start time for testing
start_time = timestamp(2024, 01, 01, 00, 00)

// Calculate current date and time
current_time = timenow

// Calculate moving averages
ema20 = ta.ema(close, short_ma_length)
ema50 = ta.ema(close, long_ma_length)
ema200 = ta.ema(close, long_ma_200_length)

// Crossing conditions
crossed_above = ta.crossover(ema20, ema50)
crossed_below = ta.crossunder(ema20, ema50)

// Entry and exit conditions within the specified time period
if (current_time >= start_time)
    strategy.entry("Buy", strategy.long, when=crossed_above)
    strategy.exit("Sell", "Buy", loss=-10, profit=20)

// Plot moving averages on the chart
plot(ema20, color=color.green, title="20-day EMA")
plot(ema50, color=color.red, title="50-day EMA")
plot(ema200, color=color.blue, title="200-day EMA")

```
```