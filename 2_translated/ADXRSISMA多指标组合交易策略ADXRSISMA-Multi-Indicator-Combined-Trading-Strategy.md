> Name

ADXRSISMA Multi-Indicator Combined Trading Strategy ADXRSISMA-Multi-Indicator-Combined-Trading-Strategy

> Author

ChaoZhang

> Strategy Description


[trans]

## Strategy Principle

This strategy uses a combination of technical indicators to identify trend directions and overbought and oversold areas, thereby generating trading signals.

Key indicators include:

1. Average Directional Index (ADX): Determines the strength of the trend.
2. Relative Strength Index (RSI): Identifies overbought and oversold conditions.
3. Simple Moving Average (SMA): Determines short-term trends.
4. SuperTrend: Identifies long-term and short-term trends.
5. Channel Breakout: Entry on trend breakout.

Specific transaction logic:

1. ADX confirms the presence of a strong trend.
2. SuperTrend confirms alignment between long-term and short-term trends.
3. RSI identifies overbought and oversold ranges.
4. Enter when the price crosses above the SMA moving average.
5. Enter on channel breakout.

Multiple indicators verify each other to enhance signal accuracy, and different strategies are combined to form a systematic trading system.

## Strategic Advantages

- Multiple indicator combinations improve signal quality.
- Different strategy combinations provide systematic entry.
- ADX identifies trends while RSI determines overbought/oversold conditions.
- SuperTrend captures trends, with SMA and channel breakouts serving as entry points.

## Strategy Risk

- Multiple parameter settings require repeated testing and optimization.
- Combined conditions occur less frequently.
- Difficulty in handling conflicting signals from indicators.

## Summary

This strategy fully leverages the strengths of various indicators to build a robust trading system. However, optimal parameter settings are crucial for maintaining reasonable trade frequency. Overall, it integrates strong trend identification with efficient entry.

[/trans]

> Strategy Arguments


| Argument      | Default | Description                        |
|---------------|---------|------------------------------------|
| v_input_1     | 7       | ADX Smoothing                      |
| v_input_2     | 7       | DI Length                          |
| v_input_3     | 70      | OB                                 |
| v_input_4     | 30      | OS                                 |
| v_input_int_1 | 5       | Length                             |


> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-12 00:00:00
end: 2023-09-13 00:00:00
Period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Combined Strategy", overlay=true, default_qty_value=100, initial_capital=1000, margin_long=0.1)

adxlen = input(7, title="ADX Smoothing")
dilen = input(7, title="DI Length")
[plus, minus] = dirmov(dilen)
sum = plus + minus
adx = 100 * ta.rma(math.abs(plus - minus) / (sum == 0 ? 1 : sum), adxlen)
sig = adx(dilen, adxlen)

// Pine Script equivalent for SuperTrend and direction
pine_supertrend(factor, atrPeriod) =>
    src = hl2
    atr = ta.atr(atrPeriod)
    upperBand = src + factor * atr
    lowerBand = src - factor * atr
    prevLowerBand = nz(lowerBand[1])
    prevUpperBand = nz(upperBand[1])

    lowerBand := lowerBand > prevLowerBand or close[1] < prevLowerBand ? lowerBand : prevLowerBand
    upperBand := upperBand < prevUpperBand or close[1] > prevUpperBand ? upperBand : prevUpperBand

    int direction = na
    float superTrend = na
    prevSuperTrend = superTrend[1]
    if (na(atr[1]) and ta.rsi(close, 21) < 66 and ta.rsi(close,3) > 80 and ta.rsi(close, 28) > 49 and sig > 20)
        direction := 1
    else if prevSuperTrend == prevUpperBand
        direction := close > upperBand ? -1 : 1
    else
        direction := close < lowerBand ? 1 : -1

    superTrend := direction == -1 ? lowerBand : upperBand
    [superTrend, direction]

[pineSupertrend, pineDirection] = pine_supertrend(3, 10)
upTrend = pineDirection < 0
downTrend = pineDirection > 0

// Define the 20-period SMA
sma20 = ta.sma(close, 20)

a = ta.rsi(close, 14)
OB = input(70)
OS = input(30)
os = a > OB
ob = a < OS

if upTrend and close > pineSupertrend and close > sma20 and os
    strategy.entry("Buy", strategy.long)

if ta.crossunder(close, sma20) or ob
    strategy.close_all()

// Define when to breakout of channel
length = input.int(title="Length", minval=1, maxval=1000, defval=5)
upBound = ta.highest(high, length)
downBound = ta.lowest(low, length)

if (not na(close[length]))
    strategy.entry("ChBrkLE", strategy.long, stop=upBound + syminfo.mintick, comment="ChBrkLE")
    strategy.entry("ChBrkSE", strategy.short, stop=downBound -
```