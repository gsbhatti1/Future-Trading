> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Show Day High/Low Lines|
|v_input_2|true|Show Fibonacci Levels|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-09 00:00:00
end: 2024-01-16 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Day High/Low Fibonacci Levels Strategy", shorttitle="DHL Fibonacci", overlay=true)

// Calculate the day's high and low
var float dayHigh = na
var float dayLow = na
if change(time("D"))
    dayHigh := high
    dayLow := low

// Define input for plotting lines
showLines = input(true, title="Show Day High/Low Lines")
showFibLevels = input(true, title="Show Fibonacci Levels")

// Plot the day's high and low as lines
plot(showLines ? dayHigh : na, color=color.green, style=plot.style_line, linewidth=1, title="Day High")
plot(showLines ? dayLow : na, color=color.red, style=plot.style_line, linewidth=1, title="Day Low")

// Calculate buy and sell conditions
buyCondition = crossover(close, dayHigh)
sellCondition = crossunder(close, dayLow)

// Set the buy and sell signals
if buyCondition
    strategy.entry("Buy", strategy.long)

if sellCondition
    strategy.exit("Sell", from_entry="Buy")

// Calculate Fibonacci retracement levels
fib236High = dayLow + 0.236 * (dayHigh - dayLow)
fib786High = dayLow + 0.786 * (dayHigh - dayLow)

// Plot the Fibonacci levels
plot(fib236High, color=color.blue, style=plot.style_line, linewidth=1, title="Fib 23.6%")
plot(fib786High, color=color.blue, style=plot.style_line, linewidth=1, title="Fib 78.6%")
```

This updated Pine Script code includes the calculation and plotting of Fibonacci retracement levels and the buy/sell conditions based on the price crossing the day's high and low. The strategy entry and exit logic is also included.