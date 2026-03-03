> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Enable Long Strategy|
|v_input_2|50|Stoploss %|
|v_input_3|50|Take Profit %|
|v_input_4|true|Enable Short Strategy|
|v_input_5|50|Stoploss %|
|v_input_6|50|Take Profit %|
|v_input_7|true|Start Date|
|v_input_8|true|Start Month|
|v_input_9|1804|Start Year|
|v_input_10|true|End Date|
|v_input_11|true|End Month|
|v_input_12|2077|End Year|


> Source (PineScript)

``` pinescript
// Define strategy arguments
strategy("RSI Breakout Strategy", shorttitle="RSI Breakout", overlay=false)

// Input arguments
longEnabled = input(true, title="Enable Long Strategy")
shortEnabled = input(true, title="Enable Short Strategy")
stopLossPercent = input(50, title="Stoploss %")
takeProfitPercent = input(50, title="Take Profit %")

// Date range inputs
startDate = input(title="Start Date", type=input.date, defval=datetime(2023, 1, 1))
startMonth = input(title="Start Month", type=input.int, defval=1)
startYear = input(title="Start Year", type=input.int, defval=2023)
endDate = input(title="End Date", type=input.date, defval=datetime(2023, 12, 1))
endMonth = input(title="End Month", type=input.int, defval=12)
endYear = input(title="End Year", type=input.int, defval=2023)

// RSI parameters
rsiThreshold = input(30, title="RSI Overbought/Oversold Threshold")
longRSI = rsi(close, 14) < rsiThreshold
shortRSI = rsi(close, 14) > 70

// Generate buy signal
if (longEnabled and longRSI)
    strategy.entry("Long", strategy.long)

// Generate sell signal
if (shortEnabled and shortRSI)
    strategy.entry("Short", strategy.short)

// Set stop loss and take profit
strategy.exit("Long Exit", "Long", stop=trail_stop(close, stopLossPercent), limit=trail_limit(close, takeProfitPercent))
strategy.exit("Short Exit", "Short", stop=trail_stop(close, stopLossPercent), limit=trail_limit(close, takeProfitPercent))

// Display RSI on chart
plot(rsi(close, 14), color=color.blue, title="RSI(14)")
```
```