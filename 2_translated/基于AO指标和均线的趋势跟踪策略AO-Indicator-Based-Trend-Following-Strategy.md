> Name

AO-Indicator-Based-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description


![IMG](https://www.fmz.com/upload/asset/ba8cb806c91b6f7206.png)
 [trans]

#### Overview

This strategy uses the Awesome Oscillator (AO) indicator to determine trend direction and moving averages to confirm the trend, belonging to a trend-following strategy. It goes long when the AO indicator crosses above the 0 line and the fast MA crosses above the slow MA, and it goes short when the AO indicator crosses below the 0 line and the fast MA crosses below the slow MA, taking advantage of trend directionality for profits.

#### Strategy Logic

This strategy mainly relies on the AO indicator to determine the short-term trend direction. The AO indicator is calculated based on the difference between the mid-price’s 5-period and 34-period simple moving averages, categorizing it as a Momentum type indicator. When the AO is positive, it means the short-term MA is above the long-term MA, which should be interpreted as a bullish sign. Conversely, when the AO is negative, it indicates the short-term MA is below the long-term MA, interpreted as a bearish sign.

Therefore, the AO indicator can effectively determine the direction of the trend. When the AO crosses above the 0 line, it signals that the market trend has turned bullish and we should go long. When the AO crosses below the 0 line, it indicates a bearish shift in the market trend and a signal to go short.

Additionally, this strategy incorporates 20-period and 200-period moving averages. These MAs represent the direction of medium to long-term trends. Relying solely on the AO indicator for short-term trend direction is not sufficient; confirmation from mid-to-long term trends is also needed, thus incorporating MA crossovers.

When the fast MA crosses above the slow MA, indicating a bullish shift in the mid-to-long-term trend, we go long when the AO crosses above 0 to ride the uptrend. Conversely, when the fast MA crosses below the slow MA, indicating a bearish shift in the mid-to-long-term trend, we go short when the AO crosses below 0 to follow the downtrend.

#### Advantages

1. Accurately determining short-term trend direction using the AO indicator
2. Adding MAs for mid-to-long term trend confirmation helps avoid false breakouts
3. Quick profits suitable for short-term trading

#### Risk Analysis

1. Risk of failed entry when going short; price may continue rising even after an AO cross below 0 and MA signals a sell before turning down.
2. Risk of failed entry when going long; price may continue falling even after an AO cross above 0 and MA signals a buy before turning up.
3. Risk of distorted AO signals at major technical levels.

#### Improvement Directions

1. Test different combinations of MAs, such as 10- and 50-periods, to find better settings
2. Integrate other indicators like RSI for enhanced signal reliability
3. Optimize fixed stop loss percentages to improve risk-reward ratio

#### Conclusion

This is a simple trend-following strategy that uses the AO indicator for short-term trend direction with mid-to-long term MAs to confirm trends, making logical sense. The combination of AO and MAs has widespread use and maturity, ensuring this strategy’s reliability. Further optimization through parameter tuning and integrating other indicators can enhance its performance.

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
// oab := ta.crossover(ao, 0) ? true : ta.crossunder(0, ao) ? false : oab
```