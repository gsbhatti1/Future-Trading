> Name

Medium-Long-Term-Quantitative-Trading-Strategy-Based-on-Bollinger-Bands

> Author

ChaoZhang

> Strategy Description

This article explains in detail a medium-long term quantitative trading strategy using Bollinger Bands. It generates trading signals by identifying price breakouts through the Bollinger Bands.

I. Strategy Logic

The strategy mainly employs the following Bollinger Bands indicators:

1. Calculate the moving median price as the baseline over a certain period.

2. Calculate the price standard deviation and multiply it by a factor as the range.

3. The median ± range constructs the upper and lower bands.

4. Price breaking through the bands generates trading signals.

The specific trading logic is:

When price breaks through the lower band, a buy signal is generated to take long positions.

When price breaks the upper band, a sell signal is generated to take short positions.

Take profit and stop loss are set at fixed percentages to lock in profits and losses.

Overall, the strategy identifies mid-long term trends by detecting price breakouts of the Bollinger Bands.

II. Advantages of the Strategy

The main advantages of this strategy are:

Firstly, Bollinger Bands can identify price breakouts and reversals to capture mid-long term trends.

Secondly, direct stop loss and take profit settings aid in prudent money management.

Lastly, simple and clear rules make this strategy easy to implement and optimize.

III. Potential Risks

However, the following risks should be noted:

Firstly, the bands need to be optimized precisely for steady signals.

Secondly, stop loss set too small risks insufficient profit, while too large increases risk.

Lastly, excessive frequent trading needs to be prevented.

IV. Summary

In summary, this article has explained a medium-long term quantitative trading strategy using Bollinger Bands for trend following. It can track price trends over the medium to long term, but requires fine tuning of the band intervals and stop loss levels. Overall it provides a relatively simple and intuitive trend following approach.

|Argument|Default|Description|
|----|----|----|
|v_input_1|51|Moving Average|
|v_input_2|3.01|Multiplier|
|v_input_3|14.2|Take Profit (%)|
|v_input_4|99|Stop Loss (%)|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-08-14 00:00:00
end: 2023-09-13 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－