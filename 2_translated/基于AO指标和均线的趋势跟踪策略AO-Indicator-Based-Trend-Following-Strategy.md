> Name

AO-Indicator-Based-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description


![IMG](https://www.fmz.com/upload/asset/ba8cb806c91b6f7206.png)
 [trans]

#### Overview

This strategy uses the Awesome Oscillator (AO) indicator to determine trend direction and moving averages to confirm the trend, falling under the category of a trend-following strategy. When the AO crosses above the 0 line and the fast MA crosses above the slow MA, go long; when the AO crosses below the 0 line and the fast MA crosses below the slow MA, go short. This leverages trends for profit.

#### Strategy Logic

The primary focus of this strategy is to use the AO indicator to determine trend direction. The AO is calculated as the difference between the mid-price and a simple moving average (SMA) over 5 periods and 34 periods. It falls under the Momentum category. When AO is positive, it means the short-term SMA is above the long-term SMA, interpreted as a bullish sign; when AO is negative, it means the short-term SMA is below the long-term SMA, interpreted as a bearish sign.

Thus, the AO indicator can effectively determine trend direction. Crossing above the 0 line signals a bullish market and suggests going long; crossing below the 0 line signals a bearish market and suggests going short. Additionally, this strategy includes 20-period and 200-period moving averages to gauge medium to long-term trends. While relying on AO for short-term direction is sufficient, confirming with moving averages provides more robust signals.

When the fast MA crosses above the slow MA, indicating a bullish medium-to-long term trend, we go long when the AO crosses above 0 and ride the uptrend. Conversely, when the fast MA crosses below the slow MA, signaling a bearish medium-to-long term trend, we go short when the AO crosses below 0 to benefit from the downtrend.

#### Advantages

1. Accurate determination of short-term trend direction using the AO indicator.
2. Incorporation of moving averages for mid-to-long-term trend confirmation, effectively filtering false breakouts.
3. Fast profits suitable for short-term trading.

#### Risk Analysis

1. When going short and the AO crosses below 0 with MA signals, prices may continue to rise before reversing downward, posing an entry risk.
2. When going long and the AO crosses above 0 with MA signals, prices may continue to fall before reversing upward, posing an entry risk.
3. Risk of false signals at major technical levels.

#### Optimization Directions

1. Test different moving average combinations, such as 10-period and 50-period MAs, to find better settings.
2. Integrate other indicators like RSI for signal confirmation.
3. Optimize fixed stop loss percentage for a better risk/reward ratio.

#### Summary

This is a simple trend-following strategy that relies on the AO indicator to determine short-term trends while confirming with mid-to-long-term moving averages, which is logically sound and widely used. The combination of AO and moving averages shows maturity and reliability. Further parameter optimization and integration of other indicators can enhance its performance.

||

#### Overview

This strategy uses the Awesome Oscillator (AO) to determine trend direction and moving averages to confirm trends, falling under the category of a trend-following strategy. When the AO crosses above the 0 line and the fast MA crosses above the slow MA, go long; when the AO crosses below the 0 line and the fast MA crosses below the slow MA, go short, taking advantage of trend directionality to profit.

#### Strategy Logic

The primary focus of this strategy is to use the AO indicator to determine the short-term trend direction. The AO is calculated based on the difference between the mid-price and simple moving averages (SMA) over 5 periods and 34 periods, which falls under the Momentum category of indicators. When AO is positive, it means the short-term SMA is above the long-term SMA, interpreted as a bullish sign; when AO is negative, it means the short-term SMA is below the long-term SMA, interpreted as a bearish sign.

Therefore, the AO indicator can effectively determine trend direction. Crossing above the 0 line signals that the market trend has turned bullish and suggests going long. Conversely, crossing below the 0 line signals that the market trend has turned bearish and suggests going short. 

In addition, this strategy also incorporates 20-period and 200-period moving averages to indicate medium to long-term trends. Judging only by the AO for short-term trend direction is not enough; confirmation from mid-to-long term trends using MAs is also necessary.

When the fast MA crosses above the slow MA, indicating a bullish medium-to-long term trend, we go long when the AO crosses above 0 and ride the uptrend. Conversely, when the fast MA crosses below the slow MA, indicating a bearish medium-to-long term trend, we go short when the AO crosses below 0 to benefit from the downtrend.

#### Advantages

1. Accurately determining short-term trend direction using the AO indicator.
2. Adding moving averages for mid-to-long-term trend confirmation, effectively avoiding false breakouts.
3. Fast profits suitable for short-term trading.

#### Risk Analysis

1. When going short and the AO crosses below 0 with MA signals, prices may continue to rise before reversing downward, posing an entry risk.
2. When going long and the AO crosses above 0 with MA signals, prices may continue to fall before reversing upward, posing an entry risk.
3. Risk of distorted AO signals at major technical levels.

#### Optimization Directions

1. Test different moving average combinations, such as 10-period and 50-period MAs, to find better settings.
2. Integrate other indicators like RSI for signal confirmation.
3. Optimize fixed stop loss percentage for a better risk/reward ratio.

#### Conclusion

This is a simple trend-following strategy that relies on the AO indicator to determine short-term trends while confirming with mid-to-long-term moving averages, which is logically sound and widely used. The combination of AO and MAs shows maturity and reliability. Further optimization of parameters and integration of other indicators can improve its performance.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_bool_1|true|long|
|v_input_bool_2|true|short|
|v_input_float_1|10|profit|
|v_input_float_2|5|stop|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-12 00:00:00
end: 2023-12-14 20:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// https://www.youtube.com/watch?v=zr3AVwjCtDA

//@version=5
strategy(title="Bingx ESTRATEGIA de Trading en 1 minuto", shorttitle="AO")
long = input.bool(true, "long")
short = input.bool(true, "short")
profit = (input.float(10, "profit") / 100) + 1
stop = (input.float(5, "stop") / 100) + 1
ao = ta.sma(hl2, 5) - ta.sma(hl2, 34)
diff = ao - ao[1]
plot(ao, color = diff <= 0 ? #F44336 : #009688, style=plot.style_columns)
changeToGreen = ta.crossover(diff, 0)
changeToRed = ta.crossunder(diff, 0)
alertcondition(changeToGreen, title="AO color changed to green", message="Awesome Oscillator's color has changed to green")
alertcondition(changeToRed, title="AO color changed to red", message="Awesome Oscillator's color has changed to red")

ema20 = ta.ema(close, 20)
ema200 = ta.ema(close, 200)
rsi = ta.rsi(close, 7)
plot(rsi)
plot(0, color=color.white)
var float pentry = 0.0
var float lentry = 0.0
var bool oab = false
// oab := ta.crossover(ao, 0) ? true : ta.crossunder(0, ao)
```