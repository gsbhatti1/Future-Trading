> Name

Low-Lag-Triple-Moving-Average-Fast-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/d7ad3cd423121aaa02.png)

## Strategy Principle

This strategy uses three low-lag moving averages, including 12-period, 26-period, and 55-period low-lag TEMA. These three MAs represent the fast, medium, and slow MAs respectively. When the fast MA crosses above the medium MA, a buy signal is generated; when the fast MA crosses below the medium MA, a sell signal is generated. By using the crossover of these three MAs to determine market entry and exit points, high-frequency trading can be achieved.

The template function `tema()` in the code calculates the low-lag TEMA. The calculation formula is: `TEMA = 2*EMA - EMA(EMA)`, which uses double exponential moving average (EWMA) for computation. Essentially, it is a doubly smoothed EMA that significantly reduces lagging effects. Thus, it can respond to price changes faster and improve the timeliness of trading signals.

Specifically, the entry rules of this strategy are: when the fast MA crosses above the medium MA and the fast MA is above the slow MA, a buy signal is generated; when the fast MA crosses below the medium MA and the fast MA is below the slow MA, a sell signal is generated.

## Advantage Analysis

The biggest advantage of this strategy is that entries and exits are determined quickly and accurately. The low-lag design of the three MAs greatly reduces lagging effects so they can respond to price changes rapidly. Additionally, using the crossover of three MAs for signal determination avoids false signals.

Furthermore, this strategy is suitable for high-frequency trading to capture short-term price fluctuations. Through fast entries and exits, it can profit from highly volatile markets.

## Risk Analysis

The biggest risk is that ultra-short-term whipsaws may occur. Due to the high sensitivity to price changes from the low-lag design, some markets might experience high-frequency oscillations, leading to easy whipsaws.

Additionally, high-frequency trading requires paying relatively high commissions and slippage costs. If profit-making ability is insufficient, it can easily be offset by transaction fees.

Moreover, this strategy requires traders to have strong real-time monitoring abilities to update stop-loss and take-profit levels timely.

## Optimization Directions

This strategy can be optimized from the following aspects:

1. Optimize the period parameters of the three MAs to better suit different market characteristics.
2. Add volatility indicators or volume indicators to confirm signals and avoid whipsaws in ranging markets.
3. Incorporate more factors to set up dynamic trailing stop mechanisms.
4. Optimize position sizing through money management techniques to control single trade risks.
5. Integrate machine learning algorithms to dynamically optimize strategy parameters.

## Conclusion

This is a low-lag triple moving average fast trading strategy. Through its low-lag design, it can achieve fast entries and exits, making it suitable for high-frequency trading to capture short-term opportunities. The biggest advantage of this strategy is that signal determination is quick and accurate. However, the main disadvantage is that it is prone to be whipsawed in ranging markets. This article comprehensively summarizes this trading strategy through detailed analysis of its rationale, advantages, risks, and optimization directions.

---

> Strategy Arguments

|Argument|Default|Description|
|--------|-------|-----------|
|v_input_1|0|Moving Average Type: temadelay|ema|emadelay|fastema|tema|nkclose|
|v_input_2|8|N|
|v_input_3|1.2|K|
|v_input_4|true|fracCap|
|v_input_5|200|TP|
|v_input_6|130|SL|
|v_input_7|true|TS|

> Source (PineScript)

```pinescript
//@version=4
strategy("scalping low lag tema etal", shorttitle="Scalping tema", initial_capital=10000, overlay=true)
mav = input(title="Moving Average Type", defval="temadelay", options=["nkclose", "ema", "emadelay", "fastema", "tema", "temadelay"])
lenb = 3
N = input(8)
K = input(1.2)
fracCap = input(1.0)
in = close + K*mom(close, N)
source = close
length = 8
sigma = 12.0
offset = 0.9
p = 4
// length = 10
// sigma = 6.0
// offset = 0.85
tema(src,len) => fastemaOut = 2*ema(src, len) - ema(ema(src, len), len)

a = 0.0
b = 0.0
c = 0.0
if mav == "nkclose"
    a := ema(in, 12)
    b := a[1]
    c := a[2]
if mav == "ema"
    a := ema(close, 12)
    b := ema(close, 26)
    c := ema(close, 55)
```