> Name

Dual-EMA Crossover Oscillation Tracking Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/13b1d64d0343d4efbf6.png)

[trans]

### Overview

The Dual-EMA Crossover Oscillation Tracking Strategy is a strategy that utilizes the EMA indicator to identify trends and tracks oscillations during volatile market conditions. This strategy combines both trend tracking and oscillation capturing ideas, aiming to achieve better returns by conducting long-term tracking during strong trends and short-term trading during oscillations.

### Strategy Logic

This strategy uses the 20-period EMA as an indicator for judging trends. When the price crosses above the EMA, it signals an upward trend; when the price crosses below, it signals a downward trend.

When the price crosses above the EMA, a long position is entered using the highest price over the past 20 periods as the take profit and the lowest low since the crossover as the stop loss. When the price crosses below the EMA, a short position is entered using the lowest price over the past 20 periods as the take profit and the highest high since the crossover as the stop loss.

At the same time, the strategy also checks if the ADX is greater than 30. Trades are only taken when the trend is strong enough, i.e., when the ADX is higher than 30. This avoids stopouts during market oscillations.

During open trades, the trailing stop continues to adjust based on market conditions to lock in more profits.

### Advantage Analysis

This strategy combines the advantages of both trend tracking and oscillation trading. It can produce larger returns during trending markets and more stable returns during oscillations, making it highly adaptable.

The use of EMA also keeps the parameters simple, lowering the risks of over-optimization and ensuring stability.

### Risk Analysis

The main risk of this strategy is the possibility of frequent stopouts during intensified oscillations. This is where the ADX comes into play. By disabling trading when ADX is low, losses in the absence of a clear trend can be avoided.

Additionally, proper stop loss placement is also key. Excessively wide stops may increase single trade loss amounts; excessively tight stops may be too sensitive and increase stopout probability. A balance needs to be found between profit targets and stop loss risks.

### Optimization Directions

Possible optimizations for this strategy include:

1. Testing different EMA periods to find the optimal combination.
2. Optimizing ADX parameters, including the ADX period and threshold values.
3. Improving the profit taking and stop loss algorithms, such as by introducing dynamic stops.
4. Combining additional indicators like KDJ and MACD to create a multi-indicator confirmation system.

### Summary

In summary, the Dual-EMA Crossover Oscillation Tracking Strategy is a highly practical strategy that combines the strengths of both trend trading strategies and oscillation strategies. It can be used for both long-term tracking and short-term trading. Further improvements in performance can be achieved through parameter optimization and adding confirming indicators. It suits investors with some degree of analytical capabilities regarding market conditions.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|14|ADX period|
|v_input_2|30|adxMin|
|v_input_3|20|emaLength|
|v_input_4|20|highPeriod|
|v_input_5|false|Custom Backtesting Dates|
|v_input_6|2018|Backtest Start Year|
|v_input_7|3|Backtest Start Month|
|v_input_8|6|Backtest Start Day|
|v_input_9|8|Backtest Start Hour|
|v_input_10|2018|Backtest Stop Year|
|v_input_11|12|Backtest Stop Month|
|v_input_12|14|Backtest Stop Day|
|v_input_13|14|Backtest Stop Hour|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-26 00:00:00
end: 2024-01-02 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("Linda Raschke's Holy Grail", shorttitle="RHG", default_qty_type = strategy.percent_of_equity, default_qty_value = 100, overlay = true)
adxlen = input(14, title="ADX period")
adxMin = input(30)
dilen = adxlen
f_highest(_src, _length)=>
    _adjusted_length = _length < 1 ? 1 : _length
    _value = _src
    for _i = 0 to (_adjusted_length-1)
        _value := _src[_i] >= _value ? _src[_i] : _value
    _return = _value

f_lowest(_src, _length)=>
    _adjusted_length = _length < 1 ? 1 : _length
    _value = _src
    for _i = 0 to (_adjusted_length-1)
        _value := _src[_i] <= _value ? _src[_i] : _value
    _return = _value

dirmov(len) =>
	up = change(high)
	down = -change(low)
	plusDM = na(up) ? na : (up > down and up > 0 ? up : 0)
    minusDM = na(down) ? na : (down > up and down > 0 ? down : 0)
	truerange = rma(tr, len)
	plus = fixnan(100 * rma(plusDM, len) / tr
```