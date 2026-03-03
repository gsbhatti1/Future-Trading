> Name

Dual-EMA-Crossover-Trend-Following-Strategy-with-ATR-and-ADX-Filters

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/19caf3e41acd323f5c5.png)
[trans]

## Overview

This strategy uses the classic dual EMA crossover system for trend following, with additional filters from the ATR and ADX indicators, to track strong trends and control risk during consolidations.

## Strategy Logic

The strategy is mainly based on the following:

1. Use a faster 8-period EMA and a slower 20-period EMA to generate crossover signals. EMAs themselves have trend-following properties.

2. The ATR indicator reflects recent volatility. Normalizing ATR allows dynamic adjustment of EMA crossover filter conditions, lowering requirements during strong trends and raising during consolidations to control risk.

3. The ADX indicator determines trend strength. An ADX reading above 30 suggests a strong trend, prompting timely stop loss.

4. Combine with bull/bear trends to determine long/short entry timing. Go long on golden crosses in a bull market, and short on death crosses in a bear market.

5. Volume filter to enter when volume expands.

6. Use a simple USD index to determine USD strength, expanding stop and take profit range during strong USD.

7. Use the SuperTrend indicator to determine overall market direction for additional long/short timing aid.

The strategy combines trend and oscillation indicators to dynamically adjust parameters, tracking trends while controlling risk.

## Advantages of the Strategy

1. The dual EMA system provides trend determination, with EMA smoothness filtering false breaks.

2. ATR-normalized filters allow flexibility for different market environments.  

3. ADX and volume provide additional checks to avoid whipsaws during consolidations.

4. Considering USD and SuperTrend improves decision accuracy on the macro trend.

5. Risk management automatically adapts based on USD strength.

6. Simple golden/dead cross signals and stop/take profit logic make it easy to implement and backtest.

## Risks of the Strategy

1. Dual EMAs lag in detecting trend turning points.

2. Poor ATR parameter selection may be too aggressive or conservative.

3. ADX parameters need optimization, improperly set high points could miss trends.

4. USD and SuperTrend trend determination could be inaccurate. 

5. Stop loss too tight increases losses, too wide risks whipsaws.

## Improvement Ideas

1. Consider adding indicators like MACD for better turnover point detection.

2. Optimize ATR parameters over more historical data.

3. Test different ADX parameters and optimize high point thresholds.

4. Add more variables for USD and market trend analysis.

5. Calculate optimal stop loss percentage from backtest stats.

6. Experiment with trailing or chandelier stops.

7. Continue optimizing entry size and holding period.

## Conclusion

This strategy integrates the classic dual EMA system with multiple auxiliary indicators, using parameterized optimization for a fairly robust trend following approach. It adapts flexibly to changing market environments, tracking trends while controlling risk. Further testing and optimization of stops and indicator parameters would improve results. The concepts are worth learning from and improving upon.

[/trans]

> Source (PineScript)

```pinescript
//@version=5
strategy("Refactored Advanced EMA Cross with Normalized ATR Filter, Controlling ADX", shorttitle="ALP V5", overlay=true)

// Initialize variables to track if a buy order has been placed and number of periods since the last buy
var bool hasBought = false
var int barCountSinceBuy = 0

// Define EMA periods
emaShort = ta.ema(close, 8)
emaLong = ta.ema(close, 20)

// Define ATR period and normalization
atrLength = 14
atrValue = ta.atr(atrLength)
maxHistoricalATR = ta.highest(atrValue, 20)
minHistoricalATR = ta.lowest(atrValue, 20)
normalizedATR = (atrValue - minHistoricalATR) / (maxHistoricalATR - minHistoricalATR)

// Define ADX parameters
adxValue = ta.rma(close, 14)
adxHighLevel = 30
isADXHigh = adxValue > adxHighLevel

// Initialize risk management variables
var float stopLossPercent = na
var float takeProfitPercent = na
var float trailingStop = na

// Calculate USD strength (simplified)
usd_strength = close / ta.ema(close, 50) - 1

// Adjust risk parameters based on USD strength
if (usd_strength > 0)
    stopLossPercent := 3
    takeProfitPercent := 6
else
    stopLossPercent := 4
    takeProfitPercent := 8

// Initialize position variable
var float positionPrice = na
```