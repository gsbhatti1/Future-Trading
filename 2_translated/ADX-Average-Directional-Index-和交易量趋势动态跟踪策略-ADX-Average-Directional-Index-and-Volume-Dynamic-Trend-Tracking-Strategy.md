<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

ADX-Average-Directional-Index-and-Volume-Dynamic-Trend-Tracking-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/15bef4738b0038b6c44.png)

[trans]

#### Overview
This strategy is a trend-following system based on the ADX indicator and trading volume. It determines trend strength using the ADX indicator and uses volume as a confirming signal to capture reliable trading opportunities in strongly trending markets. The core logic of the strategy is to trade only when the market exhibits a clear trend supported by sufficient trading volume.

#### Strategy Principle
The strategy uses a dual filtering mechanism combining the ADX indicator and volume. When the ADX value exceeds a set threshold (default 26), it indicates a significant market trend. At the same time, by comparing the current volume with the 20-period volume moving average (default multiple 1.8), the validity of the trend is confirmed. Based on these two conditions, and according to the relative strength relationship between DI+ and DI-, the trend direction is determined to decide the opening direction. When a reverse signal appears, the strategy will automatically close positions to control risk.

#### Strategy Advantages
1. The dual confirmation mechanism significantly improves the reliability of trading signals.
2. By setting ADX thresholds and volume multiples, false signals can be effectively filtered out.
3. The strategy logic is clear, with highly adjustable parameters and good adaptability.
4. The automatic position closing mechanism helps control risk promptly.
5. Combining trend strength and market participation increases the success rate of trades.

#### Strategy Risks
1. As a lagging indicator, ADX may cause delayed entry timing.
2. In ranging markets, frequent false signals may occur.
3. High volume requirements may cause missed trading opportunities in low liquidity markets.
4. Sudden market changes may lead to significant drawdowns.

#### Strategy Optimization Directions
1. Introduce price structure analysis to optimize entry timing.
2. Add stop-loss and trailing stop mechanisms to enhance risk control capabilities.
3. Consider introducing volatility indicators to optimize volume filtering conditions.
4. Develop adaptive parameter mechanisms to improve strategy adaptability.
5. Add time filtering functions to avoid trading during unfavorable periods.

#### Summary
This is a structurally complete and logically clear trend-following strategy. By combining the ADX indicator and trading volume, it effectively addresses the issue of signal reliability in trend trading. The strategy's parameter settings are flexible and can be optimized according to different market characteristics. Although there are certain risks of lag, with appropriate parameter adjustments and optimization improvements, this strategy has good practical value.

||

#### Overview
This strategy is a trend-following system based on the ADX indicator and trading volume. It determines trend strength using the ADX indicator and uses volume as a confirming signal to capture reliable trading opportunities in strongly trending markets. The core logic of the strategy is to trade only when the market exhibits a clear trend supported by sufficient trading volume.

#### Strategy Principle
The strategy uses a dual filtering mechanism combining the ADX indicator and volume. When the ADX value exceeds a set threshold (default 26), it indicates a significant market trend. At the same time, by comparing the current volume with the 20-period volume moving average (default multiple 1.8), the validity of the trend is confirmed. Based on these two conditions, and according to the relative strength relationship between DI+ and DI-, the trend direction is determined to decide the opening direction. When a reverse signal appears, the strategy will automatically close positions to control risk.

#### Strategy Advantages
1. The dual confirmation mechanism significantly improves the reliability of trading signals.
2. By setting ADX thresholds and volume multiples, false signals can be effectively filtered out.
3. The strategy logic is clear, with highly adjustable parameters and good adaptability.
4. The automatic position closing mechanism helps control risk promptly.
5. Combining trend strength and market participation increases the success rate of trades.

#### Strategy Risks
1. As a lagging indicator, ADX may cause delayed entry timing.
2. In ranging markets, frequent false signals may occur.
3. High volume requirements may cause missed trading opportunities in low liquidity markets.
4. Sudden market changes may lead to significant drawdowns.

#### Strategy Optimization Directions
1. Introduce price structure analysis to optimize entry timing.
2. Add stop-loss and trailing stop mechanisms to enhance risk control capabilities.
3. Consider introducing volatility indicators to optimize volume filtering conditions.
4. Develop adaptive parameter mechanisms to improve strategy adaptability.
5. Add time filtering functions to avoid trading during unfavorable periods.

#### Summary
This is a structurally complete and logically clear trend-following strategy. By combining the ADX indicator and trading volume, it effectively addresses the issue of signal reliability in trend trading. The strategy's parameter settings are flexible and can be optimized according to different market characteristics. Although there are certain risks of lag, with appropriate parameter adjustments and optimization improvements, this strategy has good practical value.

[/trans]



> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-11-11 00:00:00
period: 1h
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © traderhub

//@version=5
strategy("ADX + Volume Strategy", overlay=true)

// Strategy parameters
adxLength = input(21, title="ADX Period")  // ADX period
adxThreshold = input(26, title="ADX Threshold")  // ADX threshold to determine strong trend
volumeMultiplier = input.float(1.8, title="Volume Multiplier", minval=0.1, maxval=10 , step = 0.1)  // Volume multiplier, adjustable float

// Calculate ADX, DI+, DI-
[diPlus, diMinus, adx] = ta.dmi(adxLength, adxLength)

// Average volume for signal confirmation
avgVolume = ta.sma(volume, 20)  // Simple Moving Average of volume over 20 bars

// Conditions for entering a long position
longCondition = adx > adxThreshold and diPlus > diMinus and volume > avgVolume * volumeMultiplier

// Conditions for entering a short position
shortCondition = adx > adxThreshold and diMinus > diPlus and volume > avgVolume * volumeMultiplier

// Enter a long position
if (longCondition)
    strategy.entry("Long", strategy.long)

// Enter a short position
if (shortCondition)
    strategy.entry("Short", strategy.short)

// Close positions on opposite signals
if (strategy.position_size > 0 and shortCondition)
    strategy.close("Long")
if (strategy.position_size < 0 and longCondition)
    strategy.close("Short")

// Display ADX on the chart
plot(adx, color=color.red, title="ADX")
hline(adxThreshold, "ADX Threshold", color=color.green)


```

> Detail

https://www.fmz.com/strategy/471664

> Last Modified

2024-11-12 11:00:17