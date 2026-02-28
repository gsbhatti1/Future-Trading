> Name

VRSI-EMA Crossover Combined with VMACD Wavefinder Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/11eb833a57010f4073e.png)
[trans]

## Overview

This is a strategy that integrates Stochastic RSI, EMA crossovers, and VMACD to identify market reversal points. It performs best when a downtrend is about to reverse. It will generate buy signals under certain conditions.

## Strategy Logic

The strategy primarily relies on the combination of the following indicators:

1. **Stochastic RSI**: To detect overbought and oversold conditions.
2. **EMA Crossover (Fast EMA crosses above Slow EMA)**: To determine trend direction and potential reversals.
3. **VMACD**: To confirm reversal signals.

When Stochastic RSI bounces from the oversold region, the fast EMA crosses above the slow EMA, and VMACD starts to rise, a buy signal is generated. Additionally, if the short-term price breaks above the 10-period SMA, it serves as an auxiliary buy signal.

The strategy tracks changes in these indicators in real-time, calculates SMAs and EMAs over a fixed lookback period. When buy conditions are triggered, it buys and opens positions with a fixed number of contracts. If stop-loss conditions such as a 5% drawdown or price below the SMA line occur, positions will be closed for a stop-loss.

## Advantage Analysis

The strategy combines multiple indicators to effectively identify market reversal opportunities. Main advantages include:

1. Stochastic RSI is strong at identifying overbought and oversold conditions.
2. EMA crossovers have high accuracy in determining reversal signals.
3. VMACD helps filter out false signals.
4. Combining multiple indicators improves signal quality.
5. Using a short-term SMA as a stop-loss method is reasonable.

In summary, this strategy can effectively capture reversal signals and establish long positions after declines to a certain degree, thereby generating profits.

## Risk Analysis

Despite its strengths, the strategy also has some risks that need attention:

1. The market may continue to decline without reversing—systematic risk.
2. The probability of multiple indicators triggering buy signals simultaneously is low—fewer signals.
3. A simple SMA stop-loss method can be too subjective and may not provide effective drawdown control.
4. It does not account for high-volatility market environments.

To mitigate these risks, the following optimizations can be considered:

1. Add more reversal indicators to enhance effectiveness.
2. Use a combination of timed and amount-based stop losses.
3. Judge market conditions and avoid entering positions in choppy markets.
4. Optimize stop-loss logic to prevent overly aggressive stop-losses from being triggered.

## Optimization Directions

The strategy can be further optimized by focusing on the following areas:

1. Adding more indicators to form a cluster, improving signal quality.
2. Selecting optimal parameters based on the characteristics of different asset classes.
3. Incorporating machine learning models to estimate reversal probabilities using historical data.
4. Including slippage in backtests to make results closer to live performance.
5. Refining stop-loss methods to become more smooth and reasonable.
6. Detecting trend conditions to distinguish between ranging and trending environments before entering positions blindly.

## Conclusion

Overall, the VRSI-EMA Crossover Combined with VMACD Wavefinder Strategy is quite capable of identifying downtrend reversal opportunities. It generates buy signals effectively by combining multiple indicators to determine optimal timing for reversals. However, there are still some areas that can be improved upon. If further optimized, the strategy's performance in live trading could be even better. This represents a typical example of a quantitative strategy based on the fusion of multiple indicators.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|20|length|
|v_input_2|2|confirmBars|
|v_input_3|12|Short period|
|v_input_4|26|Long period|
|v_input_5|9|Smoothing period|
|v_input_6|14|lengthRSI|
|v_input_7|14|lengthStoch|
|v_input_8|3|smoothK|
|v_input_9|3|smoothD|
|v_input_10|25|OverSold|
|v_input_11|75|OverBought|

> Source (PineScript)

```pinescript
//@version=3
strategy("Wavefinder+", overlay=true)
length = input(20)
confirmBars = input(2)
price = close

slow = input(12, "Short period")
fast = input(26, "Long period")
signal = input(9, "Smoothing period")

maFast = ema(volume * price, fast) / ema(volume, fast)
maSlow = ema(volume * price, slow)

rsiLength = input(14, title="lengthRSI")
stochLength = input(14, title="lengthStoch")
kSmooth = input(3, title="smoothK")
dSmooth = input(3, title="smoothD")

overSold = input(25, title="OverSold")
overBought = input(75, title="OverBought")

stochRsi = rsi(stochastic(rsi(price, rsiLength), stochLength), kSmooth)
emaCross = crossover(maFast, maSlow)

buyCondition = (stochRsi > overSold) and emaCross
if (buyCondition)
    strategy.entry("Buy", strategy.long)

stopLoss = sma(price, signal)
drawDown = input(5, title="Drawdown")

if (price < stopLoss or price > drawDown)
    strategy.exit("Stop Loss", "Buy")
```