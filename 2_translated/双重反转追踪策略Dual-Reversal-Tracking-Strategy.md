```pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-06-14 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 21/12/2020
// This is a combination strategy for getting a cumulative signal. 
//
// First sub-strategy
// The 123 Reversal strategy buys at market if today's and yesterday's closing prices are both higher than the day before yesterday, and the fast Stoch indicator is below the slow Stoch indicator and the fast line is below 50. 
// The 123 Reversal strategy sells at market if today's and yesterday's closing prices are both lower than the day before yesterday, and the fast Stoch indicator is above the slow Stoch indicator and the fast line is above 50.
//
// Second sub-strategy
// The Key Reversal Down strategy sells at market if a new low appears in a downtrend.
//
// The actual trading signal of the entire strategy is that only when the signals of the two sub-strategies are in the same direction, the actual trading signal is issued.  
////////////////////////////////////////////////////////////

study("Dual Reversal Tracking Strategy", shorttitle="Dual Reversal Tracking", overlay=false)

// Input Parameters
length = input(14, title="Length")
kSmoothing = input(true, title="KSmoothing")
dLength = input(3, title="DLength")
level = input(50, title="Level")
barsAbove = input(1, title="Enter the number of bars over which to look for a new high in prices.")
tradeReverse = input(false, title="Trade reverse")

// 123 Reversal Strategy
longCondition = close[2] < close[1] and close[1] > close[0] and stochosc(kSmoothing, length, dLength)[1] < level and stochosc(kSmoothing, length, dLength)[1].k < 50
shortCondition = close[2] > close[1] and close[1] < close[0] and stochosc(kSmoothing, length, dLength)[1] > level and stochosc(kSmoothing, length, dLength)[1].k > 50

plotshape(series=longCondition, title="Long Entry", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=shortCondition, title="Short Entry", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Key Reversal Down Strategy
var float lowPrice = na
lowPrice := na(lowPrice) ? low(close) : min(lowPrice, low)
newLow = lowPrice < low[1]
plotshape(series=newLow, title="Short Entry", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// Combined Signal
if (longCondition and not shortCondition or not longCondition and shortCondition)
    strategy.entry("Long", strategy.long)
if (shortCondition and not longCondition or not shortCondition and longCondition)
    strategy.entry("Short", strategy.short)

// Optional: Trade reverse
if tradeReverse
    strategy.close("Long", when=longCondition)
    strategy.close("Short", when=shortCondition)
```

Note: The original `v_input_5` and `v_input_6` were not used in the translated script, as they were specific to the original document and not necessary in the Pine Script implementation.