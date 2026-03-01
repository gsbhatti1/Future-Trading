> Name

Weighted-Standard-Deviation-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/5d12a6715b43b18723.png)
[trans]

## Overview

This strategy employs the weighted standard deviation indicator, combined with moving averages, to implement trend trading in cryptocurrencies. It calculates a price channel of weighted standard deviation based on closing prices and volumes over a certain period. When the price breaks through the upper or lower channel, long or short positions are taken. Stop loss and take profit conditions are also set to limit per-trade losses.

## Strategy Logic

The code defines two custom functions to calculate weighted standard deviation from time series and arrays. The key steps are:

1. Calculate the weighted average price based on closing prices and volumes.
2. Compute the squared error of each candle relative to the average price.
3. Calculate variance based on sample size, weights, and adjusted mean.
4. Take the square root to derive standard deviation.

This yields a channel centered around the weighted average price, with upper and lower bounds at one standard deviation away. When the price breaks through the channel bottom from below, go long. When it breaches the top from above, go short.

## Advantage Analysis

The primary advantage of this strategy lies in its integration of moving averages and volatility analysis. The moving average judges market trend direction while the standard deviation sets a reasonable range—both verify each other for higher reliability. Additionally, volume weighting helps filter false breaks, increasing the probability of actual breaks.

Stop loss and take profit points further assist in trading with the trend to avoid excessive losses due to reversals. This is often a subtle aspect that novice traders fail to implement effectively.

## Risk Analysis

The main risk comes from violent market swings, which can cause the standard deviation channel to swing wildly too, making judgments difficult. Also, choosing too short periods might lead to being misled by noise and errors.

To mitigate this, appropriately smooth the parameters and period settings. Consider combining other indicators like RSI to improve breakout confirmation.

## Optimization Directions

1. Optimize period parameters—test 5-minute, 15-minute, 30-minute intervals for the best combination.
2. Optimize stop loss/take profit ratios for maximum return.
3. Add filters such as volume to avoid false breaks.
4. Incorporate candlestick filters based on close price and wick length to enhance accuracy.

## Conclusion

This strategy successfully employs the weighted standard deviation indicator alongside moving averages to track cryptocurrency trends. Reasonable stop loss/take profit setups also help trade market rhythms and avoid excessive reversal losses. Further optimizations through parameter tuning and multi-indicator verification can improve reliability for a robust algo trading strategy.

||


## Overview

This strategy uses the weighted standard deviation indicator combined with moving average to implement trend trading on cryptocurrencies. It calculates a price channel of weighted standard deviation based on closing prices and volumes over a certain period. When the price breaks through the upper or lower channel, long or short positions are taken. Stop loss and take profit conditions are also set to limit losses per trade.

## Strategy Logic

The code defines two custom functions to calculate weighted standard deviation from time series and arrays. The key steps are:

1. Calculate the weighted average price based on closing prices and volumes.
2. Compute the squared error of each candle relative to the average price.
3. Calculate variance based on sample size, weights, and adjusted mean.
4. Take the square root to derive standard deviation.

This gives us a channel centered around the weighted average price, with upper and lower bounds at one standard deviation away. When the price breaks through the channel bottom from below, go long. When it breaches the top from above, go short.

## Advantage Analysis

The biggest edge of this strategy is the combination of moving averages and volatility analysis. The moving average judges market trend direction while the standard deviation sets a sensible range—both verify each other for higher reliability. Also, volume weighting helps filter false breaks, increasing the probability of actual breaks.

Stop loss and take profit points further help trade with the trend to avoid excessive losses due to reversals. This is often a subtle aspect that novice traders fail to implement effectively.

## Risk Analysis

The main risk comes from violent market swings, which can cause the standard deviation channel to swing wildly too, making judgments difficult. Also, choosing too short periods might lead to being misled by noise and errors.

To mitigate this, appropriately smooth the parameters and period settings. Consider combining other indicators like RSI to improve breakout confirmation.

## Optimization Directions

1. Optimize period parameters—test 5-minute, 15-minute, 30-minute intervals for the best combination.
2. Optimize stop loss/take profit ratios for maximum return.
3. Add filters such as volume to avoid false breaks.
4. Incorporate candlestick filters based on close price and wick length to enhance accuracy.

## Conclusion

This strategy successfully employs the weighted standard deviation indicator together with moving averages to track cryptocurrency trends. Reasonable stop loss/take profit setups also help trade market rhythms and avoid excessive reversal losses. Further optimizations through parameter tuning and multi-indicator verification can improve reliability for a solid algo trading strategy.

||


## Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|len|
|v_input_2|3.11|Stop Loss %|
|v_input_3|7.5|Take Profit %|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-11-16 00:00:00
end: 2023-11-23 00:00:00
period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © rumpypumpydumpy   © cache_that_pass

//@version=4
strategy("[cache_that_pass] 1m 15m Function - Weighted Standard Deviation", overlay=true, pyramiding=0, default_qty_type=strategy.percent_of_equity, default_qty_value=20, initial_capital=10000, commission_type=strategy.commission.percent, commission_value=0.075)

f_weighted_sd_from_series(_src, _weight, _n) => //{
    //  @function: Calculates weighted mean, variance, standard deviation, MSE and RMSE from time series variables
    //  @parameters:
    //      _src: time series variable of sample values
    //      _weight: time series of corresponding weight values.
    //      _n : number of samples
    _xw = _src * _weight
    _sum_weight = sum(_weight, _n)
    _mean = sum(_xw, _n) / _sum_weight
    float _sqerror_sum = 0
    int _nonzero_n = 0
    for _i = 0 to _n - 1
        _sqerror_sum := _sqerror_sum + pow(_mean - _src[_i], 2) * _weight[_i]
        _nonzero_n := _weight[_i] != 0 ? _nonzero_n + 1 : _nonzero_n
    _variance = _sqerror_sum / ((_nonzero_n - 1) * _sum_weight / _nonzero_n)
    _dev = sqrt(_variance)
    _mse = _sqerror_sum / _sum_weight
    _rmse = sqrt(_mse)
    [_mean, _variance, _dev, _mse, _rmse]
//}

f_weighted_sd_from_arrays(_a_src, _a_weight, _n) => //{
    //  @function: Calculates weighted mean, variance, standard deviation, MSE and RMSE from arrays
    //  Expects index 0 of the arrays to be the most recent sample and weight values!
    //  @parameters:
    //      _a_src: array of sample values
    //      _a_weight: array of corresponding weight values.
    //      _n : number of samples
    float _mean = na, float _variance = na, float _dev = na, float _mse = na
```