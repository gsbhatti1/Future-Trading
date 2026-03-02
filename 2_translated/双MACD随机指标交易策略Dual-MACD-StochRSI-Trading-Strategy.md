> Name

Dual-MACD-StochRSI-Trading-Strategy

> Author

ChaoZhang

> Strategy Description


## Overview

This strategy combines dual MACD indicators and the StochRSI oscillator for trade signal judgment. The dual MACD uses different parameters to achieve fast and slow effects, while StochRSI verifies momentum divergence. Trend filters and stop loss conditions are also added to control risk.

## Strategy Logic

Trade signals are based on:

- Dual MACD: Fast MACD uses a short lookback period, while slow MACD uses a long lookback period for smoothing effects.
- StochRSI: Calculates the RSI's high/low range over a certain period to identify overbought and oversold levels.

Entry rules:

- Long: When fast MACD crosses above zero line and slow MACD also crosses above zero line. StochRSI is oversold, and K crosses above D. In an uptrend.
- Short: When fast MACD crosses below zero line and slow MACD also crosses below zero line. StochRSI is overbought, and K crosses below D. In a downtrend.

## Advantages

- Dual MACD avoids false breakouts for higher signal quality.
- StochRSI identifies overbought/oversold levels to avoid chasing.
- Considers overall trend direction to reduce countertrend losses.
- Cross-timeframe validation improves signal effectiveness.
- Stop loss conditions control risk.

## Risks

- MACD prone to false signals, needs further validation.
- Poorly set StochRSI parameters may miss trades.
- Improper stop loss levels may be too conservative or aggressive.
- Lacks position management for dynamic stops.

Improvements:

1. Add filters like volume or MA slope.
2. Optimize or add other oscillators.
3. Dynamic stop loss tracking.
4. Add position sizing based on performance.

## Optimization

Main areas to optimize:

1. Optimize indicator parameters.
2. Add filters to remove false signals.
3. Optimize stops for dynamic trailing.
4. Incorporate position sizing based on strategy performance.
5. Add machine learning for auto optimization.

## Summary

The strategy combines multiple indicators for stronger signals, but needs optimization in parameters, filtering, and dynamic stops to reduce unwanted trades and improve profitability. Overall the logic is sound with good optimization potential.

|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Uncheck to use custom res./intrv. for 2nd MACD indicator|
|v_input_2|45|Resolution/interval to use for 2nd MACD:|
|v_input_3|true|Uncheck to use custom res/intrv for StochRSI|
|v_input_4|45|Resolution to use for StochRSI indicator:|
|v_input_5|10|MACD fast length|
|v_input_6|21|MACD slow length|
|v_input_7|9|MACD signal length|
|v_input_8|31|2nd MACD fast length|
|v_input_9|63|2nd MACD slow length|
|v_input_10|30|2nd MACD signal length|
|v_input_11|3|smoothK|
|v_input_12|3|smoothD|
|v_input_13|11|lengthRSI|
|v_input_14|11|lengthStoch|
|v_input_15|90|RSI_buyTrig|
|v_input_16|20|RSI_sellTrig|

```pinescript
//@version=2

//This strategy is an ongoing work in progress. Last updated 8/6/16.
//Feel free to modify it as you see fit, if you do borrow code then send me a link so I 
//can see and maybe borrow some of your code to improve this.
//Thanks to ChrisMoody who I stole the code for setting custom resolution from.

//
//more info in comments at end of script

strategy("MACDouble & StochRSI w/ safeties v0.3", overlay=true)

source = close
useCurrentRes = input(true, title="Uncheck to use custom res./intrv. for 2nd MACD indicator")
resCustom = input(title="Resolution/interval to use for 2nd MACD:", defval="45")
res = useCurrentRes ? timeframe.period : resCustom

useCurrentRes2 = input(true, title="Uncheck to use custom res/intrv for StochRSI")
resCustom2 = input(title="Resolution to use for StochRSI indicator:", defval="45")
res2 = useCurrentRes2 ? timeframe.period : resCustom2


//MACD1
fastLength = input(10, title="MACD fast length")
slowlength = input(21, title="MACD slow length")
sigLength = input(9, title="MACD signal length")

MACD = ema(source, fastLength) - ema(source, slowlength)
signal = sma(MACD, sigLength)
delta = MACD - signal



//MACD2
fastLength2 = input(31, title= "2nd MACD fast length")
slowlength2 = input(63, title= "2nd MACD slow length")
sigLength2 = input(30, title= "2nd MACD signal length")

MACD2 = ema(source, fastLength2) - ema(source, slowlength2)
signal2 = sma(MACD2, sigLength2)
delta2 = MACD2 - signal2

MACDRes = security(syminfo.tickerid, res, MACD2)
signalRes = security(syminfo.tickerid,res, signal2)
deltaRes = security(syminfo.tickerid, res, delta2)


uptrend = (close + high)/(close[1] + high[2])
downtrend = (close + low)/(close[1] + low[2])

smoothK = input(3, minval=1)
smoothD = input(3, minval=1)
lengthRSI = input(11, minval=1)
lengthStoch = input(11, minval=1)
src = close

rsi1 = rsi(src, lengthRSI)
k = sma(stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = sma(k, smoothD)
RSI_buyTrigger = input(90, title="RSI buy trigger")
RSI_sellTrigger = input(20, title="RSI sell trigger")

longCondition = (crossed_above(MACDRes, 0) and crossed_above(signalRes, 0)) and k > d and uptrend
shortCondition = (crossed_below(MACDRes, 0) and crossed_below(signalRes, 0)) and k < d and downtrend

plotshape(series=longCondition, title="Long Signal", location=location.belowbar, color=color.green, style=shape.triangleup, text="LONG")
plotshape(series=shortCondition, title="Short Signal", location=location.abovebar, color=color.red, style=shape.triangledown, text="SHORT")

strategy.entry("Buy", strategy.long, when=longCondition)
strategy.exit("Take Profit/Stop Loss", "Buy", loss=RSI_sellTrigger, profit=RSI_buyTrigger)

```

Note: The `plotshape` and `strategy.entry`, `strategy.exit` parts are added to visualize the signals and actions for clarity.