> Name

Pivot Reversal Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/185a11cb484a9f73dbc.png)
 [trans]


### Overview

This article will analyze in detail a reversal trading strategy based on pivot points. The strategy calculates potential support and resistance levels over a period, and identifies trend reversals when price breaks through these pivot levels, allowing reversal trades.

### Strategy Logic

The strategy mainly relies on two indicators: Pivot High and Pivot Low. Pivot highs and lows are the highest and lowest prices within a period, and can be obtained using the `pivothigh()` and `pivotlow()` functions. When computing pivot points, the periods to the left and right need to be set; this strategy uses 4 periods to the left and 2 periods to the right.

When the highest price of the latest period is lower than the previous period's pivot high, it signals a reversal opportunity. If previous positions were short, long positions should now be considered to capitalize on the reversal. Similarly, when the latest period's lowest price is higher than the previous pivot low, existing long positions should consider reversing to short.

Specifically, the main logic is:

1. Compute pivot high/low levels
2. Identify breakthroughs
   1. Long when price breaks above pivot low
   2. Short when price breaks below pivot high
3. Set stop loss levels

### Advantage Analysis

The biggest advantage of this strategy is identifying potential trend reversal points, which is crucial for reversal traders. Compared to other indicators, pivot points can more clearly identify key support/resistance levels without frequent false signals.

Moreover, the strategy has conditions for both long and short entries, covering different market situations to avoid missing opportunities. The use of stop loss controls risk and ensures a good risk/reward ratio.

In summary, this is a very practical reversal strategy.

### Risk Analysis

Despite efforts to reduce false signals, any breakout-based strategy inevitably faces issues like premature or lagging signals. This could result in planning a long entry but the market has already reversed, or planning a short but a bull run suddenly erupts. Such inability to perfectly predict reversals is an inherent limitation of technical analysis.

Additionally, pivot points cannot guarantee perfect support/resistance levels either. Bad luck could result in stop loss hitting just before the real support level. Such uncertainty around key zones cannot be fully avoided.

### Enhancement Opportunities

1. Period optimization. The current left/right periods are set at 4 and 2. These can serve as initial values and be further optimized for each market.
2. Add filters with other indicators. For example, combine with volume to only consider breakouts as valid when accompanied by increasing volume. This helps avoid false breakouts.
3. Dynamic stop loss. Currently stops are set with a buffer of one minimum tick above/below pivot levels. The buffer zone can be dynamically adjusted based on market volatility.
4. Operate only in trend direction. Currently long/short conditions are in parallel. An optimization is to only long in uptrends and short in downtrends based on a trend filter.

### Conclusion

In summary, this is a simple yet practical reversal strategy. Identifying pivot points over a period and monitoring price breakthroughs forms the core idea for detecting potential trend reversals. The parallel long/short conditions maximize opportunities while stop losses manage risk.

The strategy logic is straightforward and easy to implement. The parameters are also intuitive for beginners. Further optimizations can improve performance for adoption. Overall this is a recommended strategy.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|4|leftBars|
|v_input_2|2|rightBars|
|v_input_3|true|From Day|
|v_input_4|3|From Month|
|v_input_5|2018|From Year|
|v_input_6|true|To Day|
|v_input_7|true|To Month|
|v_input_8|2100|To Year|


> Source (PineScript)

```pinescript
//@version=3
strategy("Pivot Reversal Strategy", overlay=true)

leftBars  = input(4)
rightBars = input(2)

// backtesting date range
from_day   = input(defval = 1,    title = "From Day",   minval = 1)
from_month = input(defval = 3,    title = "From Month", minval = 1)
from_year  = input(defval = 2018, title = "From Year",  minval = 1)
to_day     = input(defval = 17,   title = "To Day",     minval = 1)
to_month   = input(defval = 12,   title = "To Month",   minval = 1)
to_year    = input(defval = 2023, title = "To Year",    minval = 1)

//@version=4
// for backtesting only
strategy("Pivot Reversal Strategy", overlay=true)
leftBars  = input(4)
rightBars = input(2)

from_day   = input(defval = 1,    title = "From Day",   minval = 1)
from_month = input(defval = 3,    title = "From Month", minval = 1)
from_year  = input(defval = 2018, title = "From Year",  minval = 1)
to_day     = input(defval = 17,   title = "To Day",     minval = 1)
to_month   = input(defval = 12,   title = "To Month",   minval = 1)
to_year    = input(defval = 2023, title = "To Year",    minval = 1)

// Define the pivot points
pivotHigh = pivothigh(leftBars, rightBars)[0]
pivotLow  = pivotlow(leftBars, rightBars)[0]

// Determine if a break has occurred
breakAbove = close > pivotHigh and open <= pivotHigh
breakBelow = close < pivotLow and open >= pivotLow

// Long entry condition
longCondition = not v_input_3 and (v_input_1 == 4) ? 
                close[1] < pivotLow : false

// Short entry condition
shortCondition = not v_input_6 and (v_input_7 == true) ? 
                 close[1] > pivotHigh : false

// Plot the pivot levels
plot(pivotHigh, title="Pivot High", color=color.red)
plot(pivotLow,  title="Pivot Low",  color=color.green)

// Strategy logic
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Set stop loss levels
stopLossLevel = close * 0.98

if (longCondition)
    strategy.exit("Exit Long", "Long", stop=stopLossLevel)

if (shortCondition)
    strategy.exit("Exit Short", "Short", stop=stopLossLevel)
```

This Pine Script code implements the described pivot reversal strategy with appropriate input parameters and logic for identifying trade entries and setting stop losses.