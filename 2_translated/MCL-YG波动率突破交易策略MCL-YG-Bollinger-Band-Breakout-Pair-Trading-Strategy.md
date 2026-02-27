> Name

MCL-YG Volatility Breakout Pair Trading Strategy MCL-YG-Bollinger-Band-Breakout-Pair-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/ea1fb4a77fbb0620a3.png)
[trans]

### Overview

This strategy uses Bollinger Band breakouts to generate trading signals and implement pair trading between two positively correlated assets, MCL and YG. It goes long on MCL and shorts YG when the MCL price touches the upper band, and it goes short on MCL and long on YG when the MCL price touches the lower band, trading along with the prevailing trend.

### Strategy Logic

Firstly, the strategy calculates the Simple Moving Average (SMA) line and Standard Deviation (StdDev) based on closing prices over a certain period. Then it adds an offset above and below the SMA to form the upper and lower bands of Bollinger Bands. A buy signal is generated when price touches the upper band, and a sell signal when price touches the lower band.

The strategy utilizes the breakout trading logic of Bollinger Bands—go long when price breaks above the upper band and go short when it breaks below the lower band. Bollinger Bands dynamically adjust the width of the bands based on market volatility, which helps filter out market noise during ranging periods. Unlike fixed channel bands, Bollinger Bands widen during high volatility and narrow during low volatility. This allows them to filter some noise when volatility is high and capture smaller breakouts when volatility is low.

It implements pair trading between two positively correlated assets MCL and YG. When the MCL price breaks above the upper band, it indicates that MCL is in an uptrend. The strategy then goes long on MCL and shorts YG—buying the stronger asset and selling the weaker one—to benefit from the divergence in their prices.

### Advantages

1. Breakout trading based on Bollinger Bands can effectively filter market noise and identify trends.
2. Pair trading on correlated assets can gain alpha returns from price divergence.
3. Dynamic position sizing helps control risk for individual trades.
4. Standard breakout entry and reversion exit logic makes the strategy simple and clear.

### Risks

1. Poor Bollinger Bands parameter tuning may lead to too many signals or unclear signals.
2. Declining correlation between the assets can reduce profits from pair trading.
3. Breakouts may be fooled by false signals in choppy markets, causing losses.
4. No stop loss mechanism may result in increased single trade losses.

Risks can be reduced by optimizing parameters, selecting assets with stronger correlation and liquidity, setting proper stop losses, etc.

### Optimization Opportunities

1. Optimize Bollinger Bands parameters to find the best combination.
2. Test more correlated asset pairs and select the optimal combinations.
3. Add stop loss logic to limit single trade losses.
4. Add more filters to avoid false breakout signals.
5. Incorporate other factors like volume confirmation to improve entry timing.

### Summary

Overall, this strategy is relatively simple and straightforward, capturing trends using Bollinger Bands and gaining alpha from pair trading. However, there are areas for improvement in parameter tuning, stop loss settings, and pair selection. Further testing of parameters, trading vehicles, trend filters, etc., can enhance the strategy's performance.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|20|SMA Length|
|v_input_int_2|20|StdDev Length|
|v_input_float_1|true|Upper Band Offset|
|v_input_float_2|true|Lower Band Offset|
|v_input_bool_1|true|Use Position Sizing?|
|v_input_float_3|0.5|Risk %|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-11-07 00:00:00
end: 2023-11-13 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © shark792

//@version=5

// 1. Define strategy settings
strategy(title="MCL-YG Pair Trading Strategy", overlay=true,
     pyramiding=0, initial_capital=10000,
     commission_type=strategy.commission.cash_per_order,
     commission_value=4, slippage=2)

smaLength = input.int(title="SMA Length", defval=20)
stdLength = input.int(title="StdDev Length", defval=20)

ubOffset = input.float(title="Upper Band Offset", defval=1, step=0.5)
lbOffset = input.float(title="Lower Band Offset", defval=1, step=0.5)

usePosSize = input.bool(title="Use Position Sizing?", defval=true)
riskPerc   = input.float(title="Risk %", defval=0.5, step=0.25)


// 2. Calculate strategy values
smaValue = ta.sma(close, smaLength)
stdDev   = ta.stdev(close, stdLength)

upperBand = smaValue + (stdDev * ubOffset)
lowerBand = smaValue - (stdDev * lbOffset)

riskEquity  = (riskPerc / 100) * strategy.equity
atrCurrency = (ta.atr(20) * syminfo.pointvalue)
posSize     = usePosSize ? math.floor(riskEquity / atrCurrency) : 1


// 3. Output strategy data
plot(series=smaValue,