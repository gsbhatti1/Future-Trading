> Name

Price-Volatility-Mean-Reversion-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy detects price reversal opportunities by calculating the standard deviation of price volatility. When there is an anomalously large price fluctuation, it is considered as an opportunity for price reversal, and reverse trading positions are taken.

## Principle 

The strategy uses two main indicators:

1. VixFix indicator: Calculates the standard deviation of price over a certain period to determine if there is anomalous price volatility. The specific calculation is:

```pine
wvf = ((highest(close, pd) - low) / (highest(close, pd))) * 100 
sDev = mult * stdev(wvf, bbl)
midLine = sma(wvf, bbl)
lowerBand = midLine - sDev
upperBand = midLine + sDev
```

Where `wvf` is price volatility, `sDev` is standard deviation, `midLine` is the average line, `lowerBand` and `upperBand` are the lower and upper limit lines. When price exceeds the upper limit line, it is considered anomalous volatility.

2. RSI indicator: Calculates the Relative Strength Index of price to determine timing of price reversal. The calculation is:

```pine
fastup = rma(max(change(close), 0), 7)
fastdown = rma(-min(change(close), 0), 7) 
fastrsi = fastdown == 0 ? 100 : fastup == 0 ? 0 : 100 - (100 / (1 + fastup / fastdown))
```

When RSI is below a threshold, it indicates oversold status and potential bounce back. When RSI exceeds a threshold, it indicates overbought status and potential pullback.

## Entry and Exit

The entry and exit logic is:

Long entry: When price exceeds upper limit or volatility exceeds threshold, and RSI is below a value, go long.

Short entry: When price exceeds upper limit or volatility exceeds threshold, and RSI exceeds a value, go short.

Exit: When candlestick body direction is opposite of position direction, close position.

## Advantages

- Uses statistical properties of anomalous price volatility to determine price reversal with wide coverage.
- Combining with RSI to judge overbought/oversold improves entry precision.  
- Breaking lower deviation band as entry signal reduces missing opportunities.
- Candlestick body reversal as stop loss realizes quick stop loss and reduces losses.

## Risks

- Lower deviation band may need adjustment for parameter optimization.
- Breaking lower band does not guarantee reversal, risks being trapped.
- RSI parameters need optimization, improper values lead to inaccurate signals.
- Candlestick body stop loss may be too aggressive, needs adjustment.

## Optimization Directions 

- Optimize calculation period of standard deviation to better capture anomalous volatility.
- Optimize RSI parameters to find better overbought/oversold criteria. 
- Try combining other indicators like KDJ, MACD to determine reversal timing.
- Optimize stop loss mechanism, set price retracement as stop loss benchmark.

## Conclusion

The strategy detects anomalous price volatility through calculating standard deviation of price volatility, to capture reversal opportunities. RSI is combined to judge overbought/oversold status for improving entry precision. Simple candlestick body direction stop loss is used. Overall, the strategy is effective in using statistical data to detect anomalous volatility, but needs further parameter optimization to improve stability. If the stop loss mechanism can be reasonably optimized to reduce losses, the strategy would perform even better.

|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|true|leverage|
|v_input_4|40|RSI Limit|
|v_input_5|22|LookBack Period Standard Deviation High|
|v_input_6|20|Bolinger Band Length|
|v_input_7|2|Bollinger Band Standard Devaition Up|
|v_input_8|50|Look Back Period Percentile High|
|v_input_9|0.85|Highest Percentile - 0.90=90%, 0.95=95%, 0.99=99%|
|v_input_10|1.01|Lowest Percentile - 1.10=90%, 1.05=95%, 1.01=99%|
|v_input_11|false|Show High Range - Based on Percentile and LookBack Period?|
|v_input_12|false|Show Standard Deviation Line?|
|v_input_13|1900|From Year|
|v_input_14|2100|To Year|
|v_input_15|true|From Month|
|v_input_16|12|To Month|
|v_input_17|true|From day|
|v_input_18|31|To day|

> Source (PineScript)

```pinescript
/*backtest
start: 2022-10-04 00:00:00
end: 2023-10-10 00:00:00
period: 2d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Noro
// 2018

//@version=2
strategy(title = "Noro's VixFix + RSI Strategy v1.0", shorttitle = "VixFix")