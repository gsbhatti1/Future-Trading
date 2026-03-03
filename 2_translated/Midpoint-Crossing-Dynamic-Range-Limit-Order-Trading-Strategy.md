> Source (PineScript)

``` pinescript
/*backtest
start: 2024-03-31 00:00:00
end: 2025-03-29 08:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]
*/

//@version=5
strategy("Midpoint Crossing Strategy", overlay=true)

// Input for lookback period
lookback = input.int(30, title="Lookback Period", minval=1)

// Input for NYSE trading hours
startHour = 9
startMinute = 30
endHour = 15
endMinute = 0

// Variables to store high, low, and midpoint of the lookback period
var float rangeHigh = na
var float rangeLow = na
var float rangeMidpoint = na

// Calculate dynamic range
if (barstate.isrealtime)
    // Get latest close price
    lastClose = close
    
    // Find highest and lowest prices in the lookback period
    for i = 1 to lookback
        if (i == 1 or high[i] > high[rangeHigh])
            rangeHigh := high[i]
        if (i == 1 or low[i] < low[rangeLow])
            rangeLow := low[i]
    
    // Calculate midpoint of the dynamic range
    rangeMidpoint := (rangeHigh + rangeLow) / 2

// Check if current time is within NYSE trading hours
if (hour >= startHour and hour <= endHour and minute <= endMinute)
    // Check for buy signal
    if close > rangeMidpoint[1]
        strategy.entry("Buy", strategy.long)
    
    // Check for sell signal
    if close < rangeMidpoint[1]
        strategy.entry("Sell", strategy.short)

// Plot dynamic range midpoint on chart
plot(rangeMidpoint, color=color.blue, title="Range Midpoint")
```

This Pine Script implementation follows the provided Chinese document and maintains all code blocks as-is.