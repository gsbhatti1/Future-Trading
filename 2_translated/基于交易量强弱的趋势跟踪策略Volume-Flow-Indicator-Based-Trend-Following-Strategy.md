> Name

Volume-Flow-Indicator-Based-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description


![IMG](https://www.fmz.com/upload/asset/1a4b5c11b4eb09180c7.png)
[trans]

## Overview

This strategy judges market trend direction by calculating changes in trading volume and adopts a trend-following approach, establishing positions at the beginning of trends and closing positions when trends end.

## Strategy Logic

1. Calculate typical price `typical`, log return `inter`, and return variance `vinter`
2. Calculate average trading volume `vave` and maximum trading volume threshold `vmax`
3. Calculate price change `mf`, compare with variance threshold `cutoff` to get price-driven momentum `vcp`
4. Sum `vcp` to get the volume-price indicator `vfi`, calculate its moving average `vfima`
5. Compare `vfi` and `vfima` to determine the difference `dVFI` for trend direction
6. When `dVFI` crosses above 0, it is a bullish signal; when crossing below 0, it is a bearish signal
7. Establish long and short strategies based on the patterns of `dVFI`

## Advantage Analysis

1. The strategy fully considers the impact of trading volume changes on trend judgment, using momentum indicators to measure trend strength, which can more accurately capture trend turning points.
2. Trading volume threshold calculation is incorporated to filter out normal fluctuations, capturing only significant collective behavior by large funds and avoiding being misled by market noise.
3. Combining price and volume considerations can effectively avoid false breakouts.
4. The use of moving averages and logical criteria filters out most false signals.
5. Following trends rather than predicting reversals makes it suitable for medium-to-long term trend trading, helping to capture the main market direction.

## Risk Analysis

1. The strategy primarily relies on changes in trading volume to determine trends; its effectiveness may be reduced in products with inactive trading volumes.
2. Trading volume data can be manipulated, potentially generating misleading signals, so price-volume divergences need to be monitored.
3. Price-volume relationships are often lagging, which could result in missing the optimal entry timing at the beginning of trends.
4. Crude stop-loss methods may prematurely exit trades, unable to persistently capture trends.
5. The strategy is not well-suited for responding to short-term corrections and may be insensitive to sudden events.

Consider incorporating moving averages, volatility indicators, etc., to optimize entries and stops; analyzing price-volume relationships with more data sources to avoid misleading signals; incorporating appropriate technical indicators to improve responsiveness to short-term corrections.

## Optimization Directions

1. Optimize entry conditions by incorporating moving averages, Ichimoku Kinko Hyo, etc., to confirm entries after the start of trends.
2. Optimize stop-loss methods using trailing stops, staged stops, etc., to make stops adhere closely to price movements and track trend stops.
3. Add trend metrics like ADX to avoid incorrect trades in range-bound and choppy markets.
4. Optimize parameters through longer backtests to find the optimal parameter combinations.
5. Expand the strategy to more products by searching for higher-quality instruments with active trading volumes.
6. Consider adding machine learning models to leverage more data for price-volume analysis, thereby improving signal quality.

## Conclusion

The overall strategy logic is clear, and core indicators are intuitive and reliable in identifying trend directions. The advantage of this strategy lies in emphasizing changes in trading volume, making it suitable for tracking medium-to-long term trends, but misleading signals need to be monitored. Further improvements through parameter optimization, stop-loss methods, indicator combinations, etc., can enhance the live performance.

[/trans]

> Source (PineScript)

```pinescript
/*backtest
start: 2022-11-08 00:00:00
end: 2023-11-14 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("Volume Flow Indicator-Based Trend Following Strategy with Alerts and Markers on the Chart", overlay=true)
// This indicator has been copied from Lazy Bear's code
lengthVFI = 130 
coefVFI = 0.2 
vcoefVFI = 2.5 
signalLength= 5 
smoothVFI=true 

ma(x,y) => smoothVFI ? sma(x,y) : x

typical=hlc3
inter = log( typical ) - log( typical[1] )
vinter = stdev(inter, 30 )
cutoff = coefVFI * vinter * close
vave = sma( volume, lengthVFI )[1]
vmax = vave * vcoefVFI
vc = iff(volume < vmax, volume, vmax)
mf = typical - typical[1]
vcp = iff( mf > cutoff, vc, iff ( mf < -cutoff, -vc, 0 ) )

vfi = ma(sum( vcp , lengthVFI)/vave, 3)
vfima=ema( vfi, signalLength )
dVFI=vfi-vfima

bullishVFI = dVFI > 0 and dVFI[1] <=0
bearishVFI =  dVFI < 0 and dVFI[1] >=0

longCondition = dVFI > 0 and dVFI[1] <=0
shortCondition = dVFI < 0 and dVFI[1] >=0
```