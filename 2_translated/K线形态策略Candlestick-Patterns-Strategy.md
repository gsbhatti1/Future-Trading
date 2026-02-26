> Name

Candlestick-Patterns-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/11526096a58c40483c7.png)
 [trans]
## Overview  

This strategy determines buy and sell signals by identifying various price pattern formations on the candlestick chart. The strategy incorporates technical analysis methods such as Chanlun and Dow Theories, utilizing more than a dozen common graphical patterns to capture inflection points in the market.

## Strategy Principle  

The core of this strategy lies in recognizing different candlestick patterns, including engulfing lines, harami lines, piercing lines, morning stars etc. When a bullish pattern is identified, a buy signal is generated; when a bearish pattern is detected, a sell signal is triggered.

For example, when the Three White Soldiers pattern is recognized, it means that the last three candlesticks are all long green candles, and the closing price of each candle exceeds its opening price, indicating strong buying pressure pushing up the price, so a buy signal is generated.

Each pattern has a specific algorithm to identify. The strategy scans through the historical candlesticks, judging if each bar meets the formulation algorithm of a certain pattern, and once it does, plot a graphical marker on that bar marking out that signal.

## Advantages  

1. Combining judgments of various patterns improves winning rate  
2. Automatically pattern recognition without manual interference
3. Visualized markers gives intuitiveness  
4. Controlling risks by integrating stop loss and take profit

## Risks and Optimization  

1. Probability of failure still exists for patterns identification
2. Fine tune the stop loss ratio properly to lower per trade loss  
3. Adding trend judgment to avoid reverse patterns
4. Optimizing session setting to eliminate overnight risks

## Optimization Suggestions  

1. Including more auxiliary pattern judgments 
2. Combining trend indicators to filter signals
3. Optimizing ratios of stop loss and take profit  
4. Trying machine learning methods to recognize patterns
5. Adding position sizing control 

## Summary  

This strategy determines future market moves by analyzing graphical patterns formed on the candlesticks bars using technical tools. The strategy is practical to use, but traders still need to consider the general market environment, avoiding missing major trends because of local shapes. By further optimizations, it is promising to enhance the stability and profitability of the strategy.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Engulfing|
|v_input_2|true|Harami|
|v_input_3|true|Piercing Line / Dark Cloud Cover|
|v_input_4|true|Morning Star / Evening Star |
|v_input_5|true|Belt Hold|
|v_input_6|true|Three White Soldiers / Three Black Crows|
|v_input_7|true|Three Stars in the South|
|v_input_8|true|Stick Sandwich|
|v_input_9|true|Meeting Line|
|v_input_10|true|Kicking|
|v_input_11|true|Ladder Bottom|
|v_input_12|70|Stop Loss|
|v_input_13|1000|Take Profit|
|v_input_14|30|Trailing Stop|
|v_input_15|0000-0000|Trading session|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-10 00:00:00
end: 2024-01-17 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("Candle Patterns Strategy", shorttitle="CPS", overlay=true)

//--- Patterns Input ---

OnEngulfing = input(defval=true, title="Engulfing", type=bool)
OnHarami = input(defval=true, title="Harami", type=bool)
OnPiercingLine = input(defval=true, title="Piercing Line / Dark Cloud Cover", type=bool)
OnMorningStar = input(defval=true, title="Morning Star / Evening Star ", type=bool)
OnBeltHold = input(defval=true, title="Belt Hold", type=bool)
OnThreeWhiteSoldiers = input(defval=true, title="Three White Soldiers / Three Black Crows", type=bool)
OnThreeStarsInTheSouth = input(defval=true, title="Three Stars in the South", type=bool)
OnStickSandwich = input(defval=true, title="Stick Sandwich", type=bool)
OnMeetingLine = input(defval=true, title="Meeting Line", type=bool)
OnKicking = input(defval=true, title="Kicking", type=bool)
OnLadderBottom = input(defval=true, title="Ladder Bottom", type=bool)

//--- Risk Management Input ---

inpsl = input(defval = 70, title="Stop Loss", minval = 0)
inptp = input(defval = 1000, title="Take Profit", minval = 0)
inptrail = input(defval = 30, title="Trailing Stop", minval = 0)
// If the zero value is set for stop loss, take profit or trailing stop, then the function is disabled
sl = inpsl >= 1 ? inpsl : na
tp = inptp >= 1 ? inptp : na
trail = inptrail >= 1 ? inptrail : na

//--- Session Input ---

sess = input(defval = "0000-0000", title="Trading session")
t = time(timeframe.period, sess)
session_open = true

// --- Candlestick Patterns ---

//Engulfing 
bullish_engulfing = high[0]>high[1] and low[0]<low[1] and open[0]<open[1] and close[0]>close[1] and close[0]>open[0] and close[1]<close[2] and close[0]>open[1] ? OnEngulfing : na
bearish_engulfing = high[0]>high[1] and low[0]<low[1] and open[0]>open[1] and close[0]<close[1] and close[0]<open[0] and close[1]>close[2] and close[0]<open[1] ? OnEngulfing : na

//Harami
bullish_hara