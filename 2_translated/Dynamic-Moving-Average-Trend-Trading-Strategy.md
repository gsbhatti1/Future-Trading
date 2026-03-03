> Name

Dynamic Moving Average Trend Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1226cac489c12ba0f8e.png)

[trans]


## Overview

This strategy is based on the Dynamic Moving Average indicator, combined with Bollinger Bands and RSI for trade signal filtering. It implements a long-only trend tracking strategy. The strategy judges the trend by calculating the change of Heiken Ashi closing price Dynamic Moving Average and compares it with Bollinger Bands to generate trade signals. With the RSI filter, it can effectively identify trend explosive points for trend tracking.

## Strategy Logic

The core of this strategy is to calculate the change of Heiken Ashi closing price Dynamic Moving Average. Specifically, it calculates the difference between the current bar's MA and the MA of previous two bars, then multiplies it by a sensitivity coefficient to get the accurate MA change value.

Then this change value is compared with the difference between Bollinger Bands upper band and lower band. If the MA change is greater than the BB difference, it is considered as a "trend explosion". When the explosion is positive, i.e., the MA change is positive, it generates a long signal and green bar. When the explosion is negative, i.e., the MA change is negative, it generates a close signal and red bar.

In addition, this strategy has an RSI filter that only allows long signals when RSI is higher than a threshold, avoiding the risk of trend reversal.

## Advantages

- Utilizing dynamic moving average to effectively track trend changes
- Bollinger Bands as a dynamic indicator combined with MA for better trend explosion identification
- RSI filter avoids false signals from low rebounds
- Long only suitable for persistent bull market
- Flexible adjustable parameters for different products and timeframes

## Risks

- Long only cannot profit from downtrend
- Overly dependent on parameter optimization for different products and timeframes
- Unable to capture trend reversal effectively, may lead to large losses
- Improper RSI filter settings may miss trading opportunities
- High sensitivity may generate noisy trades

Risk control measures include: proper parameter tuning for robustness, combining other indicators to judge trend reversal, use only in clear long-term trends, etc.

## Optimization Directions 

This strategy still has some optimization potential:

- Try different price sources, such as close or moving averages, for better smoothing
- Adjust MA and BB period parameters for optimal performance across different products
- Use a ratio relationship instead of sensitivity coefficient to make indicator values more intuitive
- Add other filters like trendlines and volume to improve signal quality
- Develop short strategies based on indicator patterns
- Incorporate stop loss mechanisms for better risk control

## Conclusion

Overall, this is a relatively stable trend following strategy. It uses dynamic moving average to determine trend direction, Bollinger Bands to identify explosive points, RSI to filter false signals, and realizes a long-only trend system. However, it also has some risks, requiring parameter tuning for different products and timeframes, and inability to profit from downtrends. Further improvements like enhancing signal quality, developing short strategies, adding stop loss mechanisms can achieve better performance.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|150|Sensitivity|
|v_input_2|20|MacD FastEMA Length|
|v_input_3|40|MacD SlowEMA Length|
|v_input_4|20|BB Channel Length|
|v_input_5|1.5|BB Stdev Multiplier|
|v_input_6|40|RSI Value trade filter|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-11-08 00:00:00
end: 2023-11-14 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5

///////////Original Script Courtesy of Lazy_Bear.... Absolute Legend\\\\\\\\\\\\\\\

strategy('SmoothedWaddah', overlay=false, initial_capital=1)
sensitivity = input(150, title='Sensitivity')
fastLength = input(20, title='MacD FastEMA Length')
slowLength = input(40, title='MacD SlowEMA Length')
channelLength = input(20, title='BB Channel Length')
mult = input(1.5, title='BB Stdev Multiplier')
RSI14filter = input(40, title='RSI Value trade filter')

////////////MacD Calculation of price//////////////////////////////
calc_macd(source, fastLength, slowLength) =>
    fastMA = ta.ema(source, fastLength)
    slowMA = ta.ema(source, slowLength)
    fastMA - slowMA

/////////BolingerBand Calculation of Price///////////////////////
calc_BBUpper(source, length, mult) =>
    basis = ta.sma(source, length)
    dev = mult * ta.stdev(source, length)
    basis + dev

calc_BBLower(source, length, mult) =>
    basis = ta.sma(source, length)
    dev = mult * ta.stdev(source, length)
    basis - dev
```