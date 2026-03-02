```pinescript
/*backtest
start: 2023-11-06 00:00:00
end: 2023-11-13 00:00:00
period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2

strategy(title = "Dual-MA-Strategy-with-Time-Limit", shorttitle = "Dual-MA-Strategy", overlay = true)

// Revision:        1
// Author:          @ChaoZhang
//
// *** THIS IS JUST AN EXAMPLE OF STRATEGY TIME LIMITING ***
//
// This is a follow up to the original dual moving average strategy, extended to include a time limiting factor.

// === GENERAL INPUTS ===
// fast ma
maFastSource   = input(defval = open, title = "Fast MA Source", options=[open, high, low, close, hl2, hlc3, hlcc4, ohlc4])
maFastLength   = input(defval = 14, title = "Fast MA Period", minval = 1)
// slow ma
maSlowSource   = input(defval = open, title = "Slow MA Source", options=[open, high, low, close, hl2, hlc3, hlcc4, ohlc4])
maSlowLength   = input(defval = 21, title = "Slow MA Period", minval = 1)

// === STRATEGY RELATED INPUTS ===
tradeInvert     = input(defval = false, title = "Invert Trade Direction?")
// Risk management
takeProfit      = input(defval = 1000, title = "Take Profit", minval = 0)
stopLoss        = input(defval = 200, title = "Stop Loss", minval = 0)
trailStop       = input(defval = 200, title = "Trailing Stop Loss", minval = 0)
trailOffset     = input(defval = 0, title = "Trailing Stop Loss Offset", minval = 0)

// *** FOCUS OF EXAMPLE ***
// Time limiting
// a toggle for enabling/disabling
useTimeLimit    = input(defval = true, title = "Use Start Time Limiter?")
// set up where we want to run from
startYear       = input(defval = 2016, title = "Start From Year", minval = 0, step = 1)
startMonth      = input(defval = 5, title = "Start From Month", minval = 1, step = 1)
startDay        = input(defval = 1, title = "Start From Day", minval = 1, step = 1)
startHour       = input(defval = false, title = "Start From Hour?")
startMinute     = input(defval = false, title = "Start From Minute?")

// Check if the start time has been reached
isTimeLimitExceeded = (time >= timestamp(startYear, startMonth, startDay, startHour ? hour : 0, startMinute ? minute : 0))

if (useTimeLimit and isTimeLimitExceeded)
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit Long", "Long", profit_target=takeProfit, stop_loss=stopLoss, trail_stop=trailStop + trailOffset)

// Generate trading signals
fastMA = sma(close, maFastLength)
slowMA = sma(close, maSlowLength)

// Invert trade direction if enabled
if (tradeInvert)
    fastMA := -fastMA
    slowMA := -slowMA

// Buy signal when fast MA crosses above slow MA
if (crossed_above(fastMA, slowMA))
    strategy.entry("Long", strategy.long)

// Sell signal when fast MA crosses below slow MA
if (crossed_below(fastMA, slowMA))
    strategy.close("Long")

```