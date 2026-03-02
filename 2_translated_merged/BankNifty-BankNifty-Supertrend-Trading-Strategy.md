``` pinescript
/*backtest
start: 2023-11-28 00:00:00
end: 2023-12-28 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("BankNifty 5min Supertrend Based Strategy, 09:15 Entry with Date Range and Risk Management")

// Session and date range input variables
session = input("0915-1510", "Session", group="Indian Session Time")
start_date = input(title="Start Date", defval=timestamp("01 Jan 2022 00:00:00"), group="Backtest Specific Range")
end_date = input(title="End Date", defval=timestamp("01 Dec 2023 23:59:59"))
atrPeriod = input(50, "ATR Length", group="SuperTrend Setting")
factor = input.float(3.0, "Factor", step=0.1)

useDelay = input(true, "Use Delay?", group="Delay at Session Start")
Delay = useDelay ? input(10, title="Delay N numbers of candle", group="Delay at Session Start") : na

useStopLossPoints = input(true, "Use Stoploss Points?", group="Risk Management")
stopLossPoints = useStopLossPoints ? 100 : na

useTrailStop = input(true, "Use Stoploss Trail?", group="Risk Management")
trailStopPercent = useTrailStop ? 0.1 : na

// Calculate Supertrend
[supertrend, _] = ta.supertrend(factor, atrPeriod)

// Function to check if we are within the session
inSession = ta.session(session)

// Wait for Delay candles at the start of the session
if (inSession and bar_index >= 3)
    // Long entry condition
    longCondition = supertrend > 0
    // Short entry condition
    shortCondition = supertrend < 0

    if (longCondition)
        strategy.entry("Long", strategy.long)

    if (shortCondition)
        strategy.entry("Short", strategy.short)

// Exit on session end
if not inSession
    strategy.close("Long")
    strategy.close("Short")

// Set stop loss
if (strategy.opentrades > 0 and useStopLossPoints)
    strategy.exit("Exit Long with Stop Loss", from_entry="Long", limit=stopLossPoints * -1)

if (strategy.opentrades > 0 and useTrailStop)
    trailStop = ta.stop.atr(trailStopPercent, stopLossPoints)
    strategy.exit("Exit Long with Trail Stop", from_entry="Long", trail=True, trail_offset=trailStop)
```