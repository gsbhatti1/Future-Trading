> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|10|short ema|
|v_input_int_2|50|long ema|
|v_input_int_3|200|hourly 10 ema|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_4|false|Offset|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-22 00:00:00
end: 2023-06-01 00:00:00
initialCapital: 10000
symbol: ES.M
resolution: D
*/

strategy("10EMA Double Cross Trend Tracking Strategy", shorttitle="10EMA-DC", overlay=true)

// Input Parameters
short_ema = input.int(10, title="Short EMA")
long_ema = input.int(50, title="Long EMA")
hourly_short_ema = input.int(200, title="Hourly Short EMA")
source = input(close, title="Source")
offset = input(false, title="Offset")

// Plot EMAs
plot(short_ema, color=color.blue, title="Short EMA")
plot(long_ema, color=color.red, title="Long EMA")
hplot = plot(hourly_short_ema, title="Hourly Short EMA", style=plot.style_circles)

// Golden Cross and Death Cross Conditions
golden_cross = crossover(short_ema, long_ema)
death_cross = crossunder(short_ema, long_ema)

// Filter by Hourly EMA Trend
long_filter = ta.upp(hplot) > 0
short_filter = ta.downp(hplot) < 0

// Enter Long or Short Positions Based on EMAs and Filters
if (golden_cross and long_filter)
    strategy.entry("Long", strategy.long, offset=offset)

if (death_cross and short_filter)
    strategy.entry("Short", strategy.short, offset=offset)

// Trailing Stop Loss and Limit Profit
trail_stop = na
limit_profit = na

long_exit = na
short_exit = na

if (strategy.position_size > 0)
    trail_stop := strategy.exit("Trailing Stop Long", "Long", limit=limit_profit, loss=strategy.position_avg_price * 1.5)

if (strategy.position_size < 0)
    short_exit := strategy.exit("Trailing Stop Short", "Short", limit=limit_profit, loss=strategy.position_avg_price * 1.5)
```

[/trans]

The provided Pine Script defines a backtest for the 10EMA Double Cross Trend Tracking Strategy from December 22, 2022, to June 1, 2023. The strategy uses short-term (10-day), long-term (50-day), and hourly EMAs to identify trend changes and entry points. It also includes a mechanism for trailing stop loss and limit profit taking based on the average price of the position.