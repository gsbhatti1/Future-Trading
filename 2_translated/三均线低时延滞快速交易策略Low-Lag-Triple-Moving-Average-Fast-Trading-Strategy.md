> Name

Low-Lag-Triple-Moving-Average-Fast-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/d7ad3cd423121aaa02.png)

## Strategy Principle 

The strategy uses three low-lag moving averages, including 12-period, 26-period, and 55-period low-lag TEMA. These three MAs represent: the fast MA, medium MA, and slow MA, respectively. When the fast MA crosses above the medium MA, a buy signal is generated; when the fast MA crosses below the medium MA, a sell signal is generated. By using the crossover of these three MAs to determine market entry and exit points, high-frequency trading can be achieved.

The template function `tema()` is defined in the code to calculate the low-lag TEMA. Its calculation formula is: `TEMA = 2*EMA - EMA(EMA)`. This uses a double exponential moving average (EWMA) for computation, essentially a doubly smoothed EMA with the main advantage of significantly reducing lagging effects. Thus, it can respond to price changes faster and improve the timeliness of trading signals.

Specifically, the entry rules of this strategy are: when the fast MA crosses above the medium MA and the fast MA is higher than the slow MA, a buy signal is generated; when the fast MA crosses below the medium MA and the fast MA is lower than the slow MA, a sell signal is generated.

## Advantage Analysis

The biggest advantage of this strategy lies in its quick and accurate entry and exit determinations. The low-lag design of the three MAs greatly reduces lagging effects, enabling rapid responses to price changes. Using the crossover of three MAs for signal determination also helps avoid false signals.

Additionally, this strategy is suitable for high-frequency trading, as it can capture short-term price fluctuations. By executing trades quickly and frequently, it can profit from volatile markets.

## Risk Analysis

The biggest risk is that ultra-short-term whipsaws may occur due to the high sensitivity of the low-lag design to price changes. In certain markets, frequent oscillations are likely, leading to potential losses. 

Also, high-frequency trading requires paying relatively high commissions and slippage costs. If profitability is insufficient, these fees can reverse any gains.

Moreover, this strategy demands strong real-time monitoring capabilities from traders to update stop-loss and take-profit levels promptly.

## Optimization Directions

The strategy can be optimized in the following ways:

1. Optimize the period parameters of the three MAs to better suit different market characteristics.
2. Add volatility indicators or volume indicators to confirm signals, especially during ranging markets.
3. Incorporate more factors into stop-loss and take-profit mechanisms for dynamic tracking.
4. Optimize position sizing using money management techniques to control single trade risks.
5. Integrate machine learning algorithms to dynamically optimize strategy parameters.

## Conclusion

This is the Low-Lag-Triple-Moving-Average-Fast-Trading-Strategy. Through its low-lag design, it achieves fast entries and exits suitable for high-frequency trading to capture short-term opportunities. The biggest advantage of this strategy is that its signal determination is quick and accurate. However, it can be prone to whipsaws in ranging markets. This article comprehensively analyzes the rationale, advantages, risks, and optimization directions of this trading strategy.

| Argument | Default | Description |
| ---- | ---- | ---- |
| v_input_1 | 0 | Moving Average Type: temadelay | ema | emadelay | fastema | tema | nkclose |
| v_input_2 | 8 | N |
| v_input_3 | 1.2 | K |
| v_input_4 | true | fracCap |
| v_input_5 | 200 | TP |
| v_input_6 | 130 | SL |
| v_input_7 | true | TS |

```pinescript
//@version=4
strategy("scalping low lag tema et al", shorttitle="Scalping tema", initial_capital=10000, overlay=true)
mav = input(title="Moving Average Type", defval="temadelay", options=["nkclose", "ema", "emadelay", "fastema", "tema", "temadelay"])
lenb = 3
N = input(8)
K = input(1.2)
fracCap = input(1.0)
in = close + K*mom(close, N)
source = close
length = 8
sigma  = 12.0
offset = 0.9
p = 4

// length = 10
// sigma  = 6.0
// offset = 0.85

tema(src, len) => fastemaOut = 2*ema(src, len) - ema(ema(src, len), len)

a = 0.0
b = 0.0
c = 0.0
if mav == "nkclose"
    a := ema(in, 12)
    b := a[1]
    c := a[2]
else if mav == "ema"
    a := ema(close, 12)
    b := ema(close, 26)
    c := ema(close, 55)
```

Note: The code provided is part of the Pine Script and may require further completion or adjustments based on specific trading requirements.