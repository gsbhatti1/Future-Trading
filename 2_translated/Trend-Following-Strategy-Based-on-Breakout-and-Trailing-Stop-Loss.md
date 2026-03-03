> Name

Trend-Following-Strategy-Based-on-Breakout-and-Trailing-Stop-Loss

> Author

ChaoZhang

> Strategy Description


This article explains in detail a trend trading strategy based on breakout entry and trailing stop loss exit. It builds long positions on upside breakouts and utilizes swing lows for stop loss trailing.

I. Strategy Logic

The main trading logic is:

1. Use pivot points to calculate swing highs and lows.

2. Take long positions when price breaks above swing highs.

3. The most recent swing low is used as the aggressive stop loss.

4. When a higher swing low appears, trail stop loss levels upwards.

This allows the strategy to capture strong trend moves after bullish resistance breaks. The trailing stop also locks in profits as the trend extends.

II. Advantages of the Strategy

The main advantages are:

1. Breakout entry accurately captures trend starting points.

2. Trailing stop maximizes profit capturing and reduces drawdowns.

3. Stop loss levels have a buffer to prevent invalidation.

4. Moving average filters can be added to avoid counter-trend trades.

III. Potential Risks

However, some potential risks also exist:

1. Breakout signals may lag, causing missed early opportunities.

2. Aggressive stops risk premature exit on normal retracements.

3. Drawdown pressure needs to be endured.

IV. Summary

In summary, this article has explained a trend following strategy based on price breakouts and trailing stop loss. It effectively maximizes profits by trailing trends but needs to manage risks like stop loss invalidation. Overall, it provides a simple and intuitive trend tracking methodology.

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|2019|From Year|
|v_input_2|true|From Month|
|v_input_3|true|From Day|
|v_input_4|9999|To Year|
|v_input_5|true|To Month|
|v_input_6|true|To Day|
|v_input_7|false|Color Background - Test Period?|
|v_input_8|true|Use MA for Filtering?|
|v_input_9|0|MA Type For Filtering: SMA|EMA|
|v_input_10|50|MA Period for Filtering|
|v_input_11|false|Stop Loss Buffer off Swing Low (%)|
|v_input_12|true|Color Background for Trades?|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-09-13 00:00:00
end: 2023-02-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

// Revision:        1
// Author:          @millerrh
// Strategy:  Enter long when recent swing high breaks out, using recent swing low as stop level.  Move stops up as higher lows print to act
// as trailing stops.  Ride trend as long as it is there and the higher lows aren't breached.  
// Conditions/Variables 
//    1. Can place a user-defined percentage below swing low and swing high to use as a buffer for your stop to help avoid stop hunts
//    2. Can add a filter to only take setups that are above a user-defined moving average (helps avoid trading counter trend) 
//    3. Manually configure which dates to back test
//    4. Color background of backtested dates - allows for easier measuring buy & hold return of time periods that don't go up to current date    


// === CALL STRATEGY/STUDY, PROGRAMATICALLY ENTER STRATEGY PARAMETERS HERE SO YOU DON'T HAVE TO CHANGE THEM EVERY TIME YOU RUN A TEST ===
// (STRATEGY ONLY) - Comment out srategy() when in a study() 
strategy("Breakout Trend Follower", overlay=true, initial_capital=10000, currency='USD', 
   default_qty_type=strategy.percent_of_equity, default_qty_value=100, commission_type=strategy.commission.percent, commission_value=0.1)
// (STUDY ONLY) - Comment out study() when in a strategy() 
//study("Breakout Trend Follower", overlay=true)

// === BACKTEST RANGE ===
From_Year  = input(defval = 2019, title = "From Year")
From_Month = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
From_Day   = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
To_Year    = input(defval = 9999, title = "To Year")
To_Month   = input(defval = 1, title = "To Month", minval = 1, maxval = 12)
To_Day     = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
Start  = timestamp(From_Year, From_Month, From_Day, 00, 00)  // backtest start window
Finish = timestamp(To_Year, To_Month, To_Day, 23, 59)        // backtest finish window

// A switch to control background coloring of the test period - Use for easy visualization of backtest range and manual calculation of 
// buy and hold (via measurement) if doing prior periods since value in Strategy Tester extends to current date by default
testPeriodBackground = input(title="Color Background - Test Period?", type=input.bool, defval=false)
testPeriodBackgroundColor = testPeriodBackground and (time >= Start) and (time <= Finish) ? #00FF00 : na
bgcolor(testPeriodBackgroundColor, transp=95)

// == FILTERING ==
// Inputs
useMaFilter = input(title = "Use MA for Filtering?", type = input.bool, defval = true)
maType = input(defval="SMA", options=["EMA", "SMA"], title = "MA Type For Filtering")
maLength   = input(defval = 50, title = "MA Period for Filtering", minval = 1)

// Declare function to be able to swap out EMA/SMA
ma(maType, src, length) =>
    maType == "EMA" ? ema(src, length) : sma(src, length) //Ternary Operator (if maType equals EMA, then do ema calc, else do sma calc)
maFilter = ma(maType, close,