<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

RSI Trend Following Bull Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/fa438e57f097a6738f.png)
[trans]

## Overview

This strategy is a trend-following bullish strategy that uses the RSI indicator to judge trends and the MACD indicator for entry timing. It also combines the EMA moving average as a trend filter and incorporates an emergency stop-loss mechanism to control risk.

## Strategy Logic

This strategy primarily relies on the RSI indicator to determine trend direction. When the RSI indicator crosses above the set long-term RSI threshold (default 21), it indicates that the market may reverse into an upward trend. If the MACD is already in a downtrend at this point, it can be determined that the current situation is a reversal point, providing a favorable opportunity to go long.

Additionally, the strategy introduces an EMA moving average (default 200-period) as a trend filter. Long positions are only considered when the price is above the EMA line. This effectively filters out false reversals during unclear or downward trends.

For stop-losses, the strategy sets both regular and emergency stop-loss levels. Positions are closed when RSI falls below the regular stop-loss level (default 86). If prices plummet significantly and RSI drops below the emergency stop-loss level (default 73), positions are unconditionally closed to control maximum losses.

## Advantages Analysis

- Uses RSI to identify reversal points and MACD to filter out false entries.
- Incorporates EMA moving average to judge the overall trend.
- Employs both regular and emergency stop-loss mechanisms to manage risk.

## Risk Analysis

- RSI reversal signals may produce false positives.
- During significant market trend changes, EMA may not respond promptly.
- A single stop-loss indicator might prematurely terminate profitable trades.

## Optimization Directions

- Additional indicators such as volume or candlestick patterns could be introduced to improve entry accuracy.
- The moving average system could be adjusted to dynamically track recent N-day trends.
- Implement trailing stops or statistical-based stop-loss mechanisms to enhance flexibility.

## Conclusion

Overall, this strategy represents a fairly conventional trend-following bullish approach. It leverages RSI to identify reversal points, MACD to filter false signals, EMA to assess the broader trend, and stop-loss mechanisms to control risk. While straightforward and intuitive, offering certain advantages in detecting market reversals, it serves well as an introductory quantitative trading strategy. However, considerable room remains for optimization, particularly regarding entry signals, trend identification methods, and stop-loss mechanisms.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Use Emergency Exit?|
|v_input_2|21|RSI Long Cross|
|v_input_3|86|RSI Close Long Position|
|v_input_4|73|RSI Emergency Close Long Position|
|v_input_5|true|Use EMA Trend Filter|
|v_input_6|200|EMA Length for Trend Filter|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-28 00:00:00
end: 2024-01-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © dravitch
//@version=4
strategy("RSI - BULL RUN (Improved)", overlay=true)

// Input
UseEmergency = input(true, "Use Emergency Exit?")
RSIlong = input(21, "RSI Long Cross")
RSIcloseLong = input(86, "RSI Close Long Position")

EmergencycloseLong = input(73, "RSI Emergency Close Long Position")
UseEMAFilter = input(true, "Use EMA Trend Filter")
EMAlength = input(200, "EMA Length for Trend Filter")  // Utiliser 200 pour SMMA

// RSI
rsiValue = rsi(close, 14)

// MACD
[macdLine, signalLine, _] = macd(close, 12, 26, 9)

// EMA Trend Filter
emaTrend = sma(close, EMAlength)  // Utiliser sma pour la SMMA (Simple Moving Average)

// Conditions pour les trades longs
trendUp = close > emaTrend
trendDown = close < emaTrend
longCondition = crossover(rsiValue, RSIlong) and trendDown or crossunder(macdLine, signalLine) and crossover(rsiValue, RSIlong)
longCloseCondition = crossunder(rsiValue, RSIcloseLong) and trendUp
emergencyLongCondition = crossunder(rsiValue, EmergencycloseLong) 

// Plots
plot(rsiValue, color=color.white, linewidth=2, title="RSI")

// Strategy
if (longCondition)
    strategy.entry("Long", strategy.long, alert_message='RSI Long Cross: LONG')
if (longCloseCondition)
    strategy.close("Long", alert_message='RSI Close Long Position')
if (emergencyLongCondition and UseEmergency)
    strategy.close("Long", alert_message='RSI Emergency Close Long')

// Plot EMA Trend Filter in a separate pane
plot(emaTrend, color=color.rgb(163, 0, 122), title="EMA Trend Filter", linewidth=2, style=plot.style_line, transp=0)
hline(0, "Zero Line", color=color.gray)
```

> Detail

https://www.fmz.com/strategy/437689

> Last Modified

2024-01-04 17:48:41