<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Central Gap and Trend Following Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/7c129eec8be5b76642.png)

[trans]

## Overview

This strategy uses the CCI indicator and momentum indicator combined with the RSI indicator to identify market trends and enters when gaps appear in overbought/oversold zones. It also utilizes Bollinger Bands to recognize trends and mean reversion ranges. The strategy can effectively identify breakouts and pullbacks, entering at the beginning of trends, and can freely adapt to trading different instruments through parameter adjustments.

## Strategy Logic

Firstly, the strategy determines buy and sell signals based on the zero-line crossings of the CCI indicator or momentum indicator. Simultaneously, it requires the RSI indicator to be in overbought or oversold zones—specifically, above 65 for overbought conditions and below 35 for oversold conditions—to avoid issuing incorrect signals outside these zones.

Additionally, the strategy can optionally check for bullish divergence (slight upward movement) or bearish divergence (slight downward movement) in the RSI to ensure that buy/sell signals are more reliable.

When a buy signal from CCI or momentum occurs along with an RSI in the oversold zone, the strategy checks whether the previous high and low points were both above the central Bollinger Band line. If so, it generates a buy signal. Conversely, when a sell signal occurs and the previous highs and lows are both below the central Bollinger Band line, it generates a sell signal.

Thus, this strategy combines trend-following and oscillating indicators to capture trends early while using the central range to avoid false breakouts. When prices move beyond the upper or lower Bollinger Bands, the strategy closes all positions to lock in profits and prevent increased drawdowns.

## Advantages Analysis

1. Combining trend-following and oscillating indicators allows entry at the start of trends while avoiding unnecessary trades during ranging markets.
2. Utilizing the Bollinger Band centerline combined with price gaps as entry signals effectively filters out false breakouts.
3. Reviewing historical movements of the RSI helps further prevent incorrect trading signals.
4. Fully automated trading requires no human intervention, making it suitable for algorithmic trading.
5. Adjustable strategy parameters allow adaptation to various trading instruments.
6. Stop-loss and take-profit levels help control risk effectively.

## Risk Analysis

1. Incorrect settings for Bollinger Band parameters may lead to inaccurate central range identification.
2. Inappropriate indicator parameters might result in excessive false signals.
3. Failed breakouts require timely stop losses when prices retrace back toward the Bollinger Band's central area.
4. Insufficient liquidity in certain trading instruments could hinder effective breakout performance.
5. Sufficient historical data should be verified before trading to avoid poor curve fitting.
6. Attention should be paid to trading sessions to avoid false breakouts.

## Optimization Directions

1. Optimize Bollinger Band parameters to make the central range more stable.
2. Test how different indicator parameters affect performance across various instruments.
3. Add volume control to prevent excessively large single positions.
4. Include time-based filters to operate primarily during major trading hours.
5. Incorporate machine learning algorithms to enhance signal generation intelligence.
6. Connect to additional data sources to assess overall market direction.
7. Integrate more indicators to form a robust composite indicator system.

## Conclusion

This strategy integrates trend-following and oscillating indicators to enter the market at the onset of trends. By combining Bollinger Bands' central range with price gaps as entry signals, it effectively avoids false breakouts. Its adjustable parameters enable flexibility across different instruments, yielding excellent backtesting results. Future steps involve optimizing parameter settings and integrating models to enhance strategy robustness and achieve long-term, stable excess returns.

||

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_string_1|0|Entry Signal Source: CCI|Momentum|
|v_input_int_1|10|CCI/Momentum Length|
|v_input_bool_1|false|Find Regular Bullish/Bearish Divergence|
|v_input_int_2|65|RSI Overbought Level|
|v_input_int_3|35|RSI Oversold Level|
|v_input_int_4|14|RSI Length|
|v_input_bool_2|true|Plot Mean Reversion Bands on the chart|
|v_input_1|200|Lookback Period (EMA)|
|v_input_float_1|1.6|Outer Bands Multiplier|

> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-18 00:00:00
end: 2023-10-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy(title='BroTheJo Strategy', shorttitle='BTJ', overlay=true)

// Input settings
ccimomCross = input.string('CCI', 'Entry Signal Source', options=['CCI', 'Momentum'])
ccimomLength = input.int(10, minval=1, title='CCI/Momentum Length')
useDivergence = input.bool(false, title='Find Regular Bullish/Bearish Divergence')
rsiOverbought = input.int(65, minval=1, title='RSI Overbought Level')
rsiOversold = input.int(35, minval=1, title='RSI Oversold Level')
rsiLength = input.int(14, minval=1, title='RSI Length')
plotMeanReversion = input.bool(true, 'Plot Mean Reversion Bands on the chart')
emaPeriod = input(200, title='Lookback Period (EMA)')
bandMultiplier = input.float(1.6, title='Outer Bands Multiplier')

// CCI and Momentum calculation
momLength = ccimomCross == 'Momentum' ? ccimomLength : 10
mom = close - close[momLength]
cci = ta.cci(close, ccimomLength)
ccimomCrossUp = ccimomCross == 'Momentum' ? ta.cross(mom, 0) : ta.cross(cci, 0)
ccimomCrossDown = ccimomCross == 'Momentum' ? ta.cross(0, mom) : ta.cross(0, cci)

// RSI calculation
src = close
up = ta.rma(math.max(ta.change(src), 0), rsiLength)
down = ta.rma(-math.min(ta.change(src), 0), rsiLength)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - 100 / (1 + up / down)
oversoldAgo = rsi[0] <= rsiOversold or rsi[1] <= rsiOversold or rsi[2] <= rsiOversold or rsi[3] <= rsiOversold
overboughtAgo = rsi[0] >= rsiOverbought or rsi[1] >= rsiOverbought or rsi[2] >= rsiOverbought or rsi[3] >= rsiOverbought

// Regular Divergence Conditions
bullishDivergenceCondition = rsi[0] > rsi[1] and rsi[1] < rsi[2]
bearishDivergenceCondition = rsi[0] < rsi[1] and rsi[1] > rsi[2]

// Mean Reversion Indicator
meanReversion = plotMeanReversion ? ta.ema(close, emaPeriod) : na
stdDev = plotMeanReversion ? ta.stdev(close, emaPeriod) : na
upperBand = plotMeanReversion ? meanReversion + stdDev * bandMultiplier : na
lowerBand = plotMeanReversion ? meanReversion - stdDev * bandMultiplier : na

// Entry Conditions
prevHigh = ta.highest(high, 1)
prevLow = ta.lowest(low, 1)
longEntryCondition = ccimomCrossUp and oversoldAgo and (not useDivergence or bullishDivergenceCondition) and (prevHigh >= meanReversion) and (prevLow >= meanReversion)
shortEntryCondition = ccimomCrossDown and overboughtAgo and (not useDivergence or bearishDivergenceCondition) and (prevHigh <= meanReversion) and (prevLow <= meanReversion)

// Plotting
oldLongEntryCondition = ccimomCrossUp and oversoldAgo and (not useDivergence or bullishDivergenceCondition)
oldShortEntryCondition = ccimomCrossDown and overboughtAgo and (not useDivergence or bearishDivergenceCondition)
plotshape(oldLongEntryCondition, title='BUY', style=shape.triangleup, location=location.belowbar, color=color.new(color.lime, 0), textcolor=color.new(color.white, 0), size=size.tiny)
plotshape(oldShortEntryCondition, title='SELL', style=shape.triangledown, location=location.abovebar, color=color.new(color.red, 0), textcolor=color.new(color.white, 0), size=size.tiny)

// Strategy logic
if (longEntryCondition)
    strategy.entry("Buy", strategy.long)
if (shortEntryCondition)
    strategy.entry("Sell", strategy.short)

// Close all open positions when outside of bands
closeAll = (high >= upperBand) or (low <= lowerBand)

if (closeAll)
    strategy.close_all("Take Profit/Cut Loss")


// Plotting
plot(upperBand, title='Upper Band', color=color.fuchsia, linewidth=1)
plot(meanReversion, title='Mean', color=color.gray, linewidth=1)
plot(lowerBand, title='Lower Band', color=color.blue, linewidth=1)
```

> Detail

https://www.fmz.com/strategy/430176

> Last Modified

2023-10-25 18:02:11