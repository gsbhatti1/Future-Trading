> Name

Adaptive-Trading-Strategy-Based-on-ADX-Indicator

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/e71a2a708f61bbf9a5.png)
[trans]
## Overview

The core of this strategy is to use the ADX indicator to judge market trends, and combine the difference between DI+ and DI- to automatically identify breakout points for adaptive trading. When the difference between DI+ and ADX exceeds the set threshold, go long. When the difference between DI- and ADX exceeds the set threshold, go short. This strategy can automatically identify trend breakout points without manual intervention, suitable for medium and long term holdings.

## Strategy Principle

1. Calculate True Range, Directional Movement indicators to get DI+, DI-, DX, and ADX indicators.
2. Compare the difference amplitude1 between DI+ and ADX, and the difference amplitude2 between DI- and ADX.
3. When amplitude1 is greater than the set threshold (e.g., 10), a long signal is generated; when amplitude2 is greater than the set threshold (e.g., 10), a short signal is generated.
4. And require ADX to be between DI+ and DI- to filter out wrong signals.

Thus, when the market enters a trend, DI+ or DI- will notably lead ADX, generating trading signals. When the market trend ends, DI+, DI-, and ADX will get close again, avoiding chasing highs and selling lows.

## Advantages of the Strategy

1. Automatically identify trend breakout points without manual judgment.
2. Flexibly adjust the threshold of difference between DI and ADX to adapt to different market environments.
3. Effectively filter out wrong signals by combining the ADX indicator.
4. Longer holding periods, no need for high frequency trading, high capital utilization.
5. Controllable pullbacks and stable growth.

## Risks of the Strategy

1. The ADX indicator lags and may miss short-term trading opportunities. Other indicators can be combined or ADX parameters can be reduced to improve sensitivity.
2. Easy to be trapped in range-bound markets. Stop loss strategies can be introduced or ADX filtering conditions can be added to reduce the probability of being trapped.
3. Prone to huge losses during major trend reversals. Moving stop loss or trailing stop loss can be set up to control risks.

## Optimization Directions

1. Test on different markets and products to find the optimal parameter combination.
2. Consider incorporating other technical indicators to improve signal accuracy, such as MACD, KD, etc.
3. Add stop loss strategies to control drawdowns and maximum losses.
4. Introduce position sizing to adjust positions based on market conditions.
5. Optimize entry and exit criteria to reduce trading risks.

## Conclusion

This strategy integrates the strengths of ADX and DI indicators to effectively judge trends and implement adaptive trading. No frequent trading needed, suitable for medium-long term holdings. There are also certain risks. Auxiliary technical indicators and risk management techniques need to be incorporated to improve strategy stability. The strategy idea is reliable and logically clear, worth in-depth research and application.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|len|
|v_input_2|20|th|
|v_input_3|10|Long Difference|
|v_input_4|10|Short Difference|
|v_input_bool_1|true|(?Monthly Performance)Show Monthly Monthly Performance ?|
|v_input_5|0|Location: Bottom Right, Top Right, Top Left, Bottom Left, Middle Right, Bottom Center|
|v_input_6|0|Size: Small, Tiny, Normal, Large|
|v_input_color_1|#07e2f2|Background Color|
|v_input_color_2|#000000|Month/Year Heading Color|
|v_input_color_3|white|Month PnL Data Color|
|v_input_color_4|#000000|Year PnL Data Color|
|v_input_color_5|white|Table Border Color|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-01-10 00:00:00
end: 2024-01-16 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © MAURYA_ALGO_TRADER

//@version=5
strategy("Monthly Performance by Dr. Maurya", overlay=true, default_qty_value = 15, commission_type = strategy.commission.percent, commission_value = 0.1)


len = input(14)
th = input(20)

TrueRange = math.max(math.max(high - low, math.abs(high - nz(close[1]))), math.abs(low - nz(close[1])))
DirectionalMovementPlus = high - nz(high[1]) > nz(low[1]) - low ? math.max(high - nz(high[1]), 0) : 0
DirectionalMovementMinus = nz(low[1]) - low > high - nz(high[1]) ? math.max(nz(low[1]) - low, 0) : 0

SmoothedTrueRange = 0.0
SmoothedTrueRange := nz(SmoothedTrueRange[1]) - nz(SmoothedTrueRange[1]) / len + TrueRange

SmoothedDirectionalMovementPlus = 0.0
SmoothedDirectionalMovementPlus := nz(SmoothedDirectionalMovementPlus[1]) - nz(SmoothedDirectionalMovementPlus[1]) / len + DirectionalMovementPlus

Smoo