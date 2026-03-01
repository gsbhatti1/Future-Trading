``` pinescript
/*backtest
start: 2023-12-26 00:00:00
end: 2024-01-25 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at
// https://mozilla.org/MPL/2.0/
//
// Created by ChaoZhang
// 
// This strategy benefits from extracts taken from the following
// studies/authors.  Thank you for developing and sharing your ideas in an open
// way!
//  * Wave Trend Strategy by thomas.gigure
//  * cRSI + Waves Strategy with VWMA overlay by Dr_Roboto
//
//@version=4

//==============================================================================
//==============================================================================
overlay = true  // plots VWMA (need to close and re-add)
//overlay = false // plots Wave Trend (need to close and re-add)

strategy("Wave Trend w/ VWMA overlay", overlay=overlay)
     
baseQty = input(defval=1, title="Base Quantity", type=input.float, minval=1)

useSessions = input(defval=true, title="Limit Signals to Trading Sessions?")
sess1_startHour = input(defval=8, title="Session 1: Start Hour",
     type=input.integer, minval=0, maxval=23)
sess1_startMinute = input(defval=25, title="Session 1: Start Minute",
     type=input.integer, minval=0, maxval=59)
sess1_stopHour = input(defval=10, title="Session 1: Stop Hour",
     type=input.integer, minval=0, maxval=23)
sess1_stopMinute = input(defval=25, title="Session 1: Stop Minute",
     type=input.integer, minval=0, maxval=59)
sess2_startHour = input(defval=12, title="Session 2: Start Hour",
     type=input.integer, minval=0, maxval=23)
sess2_startMinute = input(defval=55, title="Session 2: Start Minute",
     type=input.integer, minval=0, maxval=59)
sess2_stopHour = input(defval=14, title="Session 2: Stop Hour",
     type=input.integer, minval=0, maxval=23)
sess2_stopMinute = input(defval=55, title="Session 2: Stop Minute",
     type=input.integer, minval=0, maxval=59)
closeAllAtEndOfSession1 = input(defval=false, title="Close All at End of Session 1")
closeAllAtEndOfSession2 = input(defval=true, title="Close All at End of Session 2")
useVWMAVolume = input(defval=true, title="VWMA: Use Volume (uncheck if equity does not have volume)")
vwmalength = input(defval=21, title="VWMA: Length", type=input.integer, minval=1)
wavetrendChannelLength = input(defval=10, title="Wave Trend: Channel Length", type=input.integer, minval=1)
wavetrendAverageLength = input(defval=21, title="Wave Trend: Average Length", type=input.integer, minval=1)
wavetrendOverBoughtLevel1 = input(defval=60, title="Wave Trend: Over Bought Level 1", type=input.integer, minval=-100)
wavetrendOverBoughtLevel2 = input(defval=53, title="Wave Trend: Over Bought Level 2", type=input.integer, minval=-100)
wavetrendOverSoldLevel1 = input(defval=-60, title="Wave Trend: Over Sold Level 1", type=input.integer, minval=-100)
wavetrendOverSoldLevel2 = input(defval=-53, title="Wave Trend: Over Sold Level 2", type=input.integer, minval=-100)

// Wave Trend Calculation
[sma, wt1, wt2] = wtosc(closing价, wavetrendChannelLength, wavetrendAverageLength, wavetrendOverBoughtLevel1, wavetrendOverBoughtLevel2, wavetrendOverSoldLevel1, wavetrendOverSoldLevel2)

// VWMA Calculation
vwmam = vwap(close, volume, vwmalength)
if (useSessions and time[0] != time)
    // Switch to the next session if it's a new trading day
    timeSwitched = true
else
    timeSwitched = false

if useVWMAVolume and bar_index % 15 == 0
    // Update VWMA on each new minute in the session
    vwmam := vwap(close, volume, vwmalength)

// Trading Logic
longCondition = wt1 > wt2
shortCondition = wt1 < wt2

if useSessions and timeSwitched or not useSessions
    if longCondition
        strategy.entry("Long", strategy.long)
    if shortCondition
        strategy.close("Long")
        
if closeAllAtEndOfSession1 and not useSessions
    // Close all positions at the end of Session 1
    if time.hour >= sess1_stopHour and time.minute >= sess1_stopMinute
        strategy.close_all()

if closeAllAtEndOfSession2 and useSessions
    // Close all positions at the end of Session 2
    if time.hour >= sess2_stopHour and time.minute >= sess2_stopMinute
        strategy.close_all()

// Position Sizing Based on VWMA
if vwmam > 0
    qty = baseQty * (vwmam / 100)
else
    qty = baseQty

strategy.exit("Exit Long", from_entry="Long", size=qty)

```

Note: The `wtosc` function used in the script needs to be defined separately, as it is not a built-in Pine Script function. This function would need to be implemented based on the Wave Trend calculation described earlier.

Also, ensure that your strategy aligns with the rules and regulations of the exchange you are trading on.