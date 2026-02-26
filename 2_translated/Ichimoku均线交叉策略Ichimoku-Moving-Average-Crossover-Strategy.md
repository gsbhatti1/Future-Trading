> Name

Ichimoku Moving Average Crossover Strategy Ichimoku-Moving-Average-Crossover-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/11cb244a6da64ae9842.png)
[trans]

## Overview  

The Ichimoku moving average crossover strategy identifies long and short signals by calculating a set of moving averages and detecting price crosses. This strategy combines multiple technical indicators, providing solid and reliable trading for middle-to-long term operations.

## Strategy Logic

The Ichimoku strategy utilizes a specialized system consisting of 5 moving average lines: the conversion line, base line, leading span 1, leading span 2, and lagging span. The conversion line depicts recent price momentum, the base line shows medium-to-long-term trends, the leading lines combine the conversion and base to predict future movements, while the lagging span displays historical reference prices. Trading signals are generated when the price breaks through the base line. The strategy also incorporates body filters and candlestick color judgment to avoid false breaks.

## Advantages

The Ichimoku strategy integrates the strengths of various technical indicators into a single system. It blends concepts like moving averages, price channels, and volume confirmation, forming a systematic methodology that ensures accurate and directional trading signals. Compared to single-indicator strategies, this approach significantly reduces false signals and enhances profit factors.

## Risks

As a trend-following system, the Ichimoku strategy has relatively long trading intervals. This means it cannot capture short-term price oscillations effectively. Additionally, moving averages become ineffective during violent market fluctuations. These situations can lead to incorrect signals and losses. It is advisable to use stop-losses to control risks.

## Enhancement Opportunities

The Ichimoku strategy can be improved in several areas: 1) Adjusting average parameters for different periods and assets; 2) Incorporating volume indicators to confirm price-volume relationships; 3) Introducing machine learning models to refine signal determination; 4) Adding more filters to reduce the probability of incorrect trades.

## Conclusion

The stable and reliable Ichimoku moving average crossover strategy is suitable as a core strategy combined with other algorithms. Its clear trend guidance, along with parameter tuning and multi-indicator optimization, makes it worthy of in-depth research and long-term application by quantitative traders.

||

## Source (PineScript)

```pinescript
/*backtest
start: 2023-11-18 00:00:00
end: 2023-12-18 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// Noro
// 2018

//@version=3
strategy(title="Noro's Ichimoku Strategy v1.0", shorttitle="Ichimoku str 1.0", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, pyramiding=0)

// Settings
needlong = input(true, defval=true, title="Long")
needshort = input(true, defval=true, title="Short")
conversionPeriods = input(9, minval=1, title="Conversion Periods")
basePeriods = input(26, minval=1, title="Base Periods")
laggingSpan2Periods = input(52, minval=1, title="Lagging Span")
usebf = input(true, defval=true, title="Use body filter")
usecf = input(true, defval=true, title="Use color filter")
fromyear = input(1900, defval=1900, minval=1900, maxval=2100, title="From Year")
toyear = input(2100, defval=2100, minval=1900, maxval=2100, title="To Year")
frommonth = input(01, defval=01, minval=01, maxval=12, title="From Month")
tomonth = input(12, defval=12, minval=01, maxval=12, title="To Month")
fromday = input(01, defval=01, minval=01, maxval=31, title="From day")
today = input(31, defval=31, minval=01, maxval=31, title="To day")

// Ichimoku
donchian(len) => avg(lowest(len), highest(len))
conversionLine = donchian(conversionPeriods)
baseLine = donchian(basePeriods)
leadLine1 = avg(conversionLine, baseLine)
leadLine2 = donchian(laggingSpan2Periods)

// Lines
plot(conversionLine, color=red, title="Conversion Line")
plot(baseLine, color=blue, title="Base Line")
plot(close, offset=-basePeriods, color=green, title="Lagging Span")
p1 = plot(leadLine1, offset=basePeriods, color=green, title="Lead 1")
p2 = plot(leadLine2, offset=basePeriods, color=red, title="Lead 2")
fill(p1, p2)

// Body Filter
nbody = abs(close - open)
abody = sma(nbody, 10)
body = nbody > abody / 3 or usebf == false

// Color Filter
bar = close > open ? 1 : close < open ? -1 : 0
gb = bar == 1 or usecf == false
rb = bar == -1 or usecf == false

// Signals
up = low > baseLine and rb and body
dn = high < baseLine
```