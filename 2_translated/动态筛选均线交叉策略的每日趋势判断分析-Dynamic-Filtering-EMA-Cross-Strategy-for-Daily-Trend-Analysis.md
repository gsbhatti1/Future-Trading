``` pinescript
/*backtest
start: 2024-12-06 00:00:00
end: 2025-01-04 08:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Daily EMA Comparison Strategy", shorttitle="Daily EMA cros Comparison", overlay=true)

//------------------------------------------------------------------------------
// Inputs
//------------------------------------------------------------------------------
fastEmaLength = input.int(10, title="Fast EMA Length", minval=1)  // Fast EMA period
slowEmaLength = input.int(50, title="Slow EMA Length", minval=1)  // Slow EMA period
checkHour = input.int(9, title="Check Hour (24h format)", minval=0, maxval=23)  // Hour to check
checkMinute = input.int(0, title="Check Minute", minval=0, maxval=59)  // Minute to check

//------------------------------------------------------------------------------
// EMA Calculation
//------------------------------------------------------------------------------
fastEMA = ta.ema(close, fastEmaLength)
slowEMA = ta.ema(close, slowEmaLength)

//------------------------------------------------------------------------------
// Time Check
//------------------------------------------------------------------------------
// Get the current bar's time in the exchange's timezone
currentTime = timestamp("GMT-0", year, month, dayofmonth, checkHour, checkMinute)
// Check if the bar's time equals or passes the daily check time
isCheckTime = (hour == checkHour) and (minute <= checkMinute)

// Trading Logic
if (isCheckTime)
    if fastEMA > slowEMA
        strategy.entry("Long", strategy.long)
    else if fastEMA < slowEMA
        strategy.entry("Short", strategy.short)

// Plot EMAs on the chart
plot(fastEMA, color=color.blue, title="Fast EMA")
plot(slowEMA, color=color.red, title="Slow EMA")

```