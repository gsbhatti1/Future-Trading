``` pinescript
/*backtest
start: 2023-12-03 00:00:00
end: 2024-01-02 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy(title="Lesson 6", shorttitle="RSI Swing Signals", overlay=true)

// Get user input
rsiSource = input(title="RSI Source", type=input.source, defval=close)
rsiLength = input(title="RSI Length", type=input.integer, defval=9)
rsiOverbought = input(title="RSI Overbought Level", type=input.integer, defval=60)
rsiOversold = input(title="RSI Oversold Level", type=input.integer, defval=25)

// Calculate RSI
rsi = rsi(rsiSource, rsiLength)

// Define engulfing pattern function
longCondition = na
shortCondition = na

// Check for bullish and bearish engulfing patterns
if (close > open and close[1] < open[1])
    longCondition := true
else if (close < open and close[1] > open[1])
    shortCondition := true

// Generate buy/sell signals based on RSI and engulfing pattern
if rsi <= rsiOversold and longCondition
    strategy.entry("Buy", strategy.long)
    
if rsi >= rsiOverbought and shortCondition
    strategy.entry("Sell", strategy.short)

// Plot RSI
plot(rsi, color=color.blue, title="RSI")

// Plot buy/sell signals
plotshape(series=longCondition, location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")
plotshape(series=shortCondition, location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")
```

This script defines the strategy as specified in the Chinese document. It includes RSI calculations and engulfing pattern detection to generate buy and sell signals. The parameters for RSI source, length, overbought level, and oversold level are set by user input, and the strategy entry/exit conditions based on these inputs are outlined.