> Name

Dual-Moving-Average-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/19cc992015e07f4eeab.png)
[trans]
## Overview

This strategy uses dual moving averages to form a channel, capturing the direction of trends. Trading signals are generated when price breaks through the channel. RSI is also incorporated to filter false breakouts. It trades only during London session with a maximum of 5 trades per day, with a maximum daily loss not exceeding 2%.

## Strategy Logic

The strategy employs two moving averages of length 5, one calculated from the highest price and the other from the lowest price, to form a price channel. Long signals are triggered when the close price breaks above the upper band, and short signals when it breaks below the lower band.

To avoid false breakouts, the RSI indicator is added to gauge overbought/oversold levels. Go long only if RSI is above 80, and go short only if RSI is below 20.

Also, the strategy trades only during the London session (3am - 11am), with a maximum of 5 orders per day and a maximum 2% daily loss of equity.

## Advantage Analysis

### Catch the Trend

The dual MA channel can effectively detect the direction of the price trend. Breaking the upper band catches the upside trend, while breaking the lower band catches the downside trend.

### Reduce False Breakouts

Using the RSI overbought/oversold filter can reduce some false breakout signals caused by price fluctuations.

### Effective Risk Control

Trading only during the major session and having a maximum of orders per day limits trading frequency. A maximum 2% daily loss also defines the risk tolerance.

## Risk Analysis

### False Breakout with Volatility

Significant price swings can cause some false breakout signals, leading to unnecessary losses. Parameters can be optimized and more filters added to reduce such risks.

### Fixed SL/TP Risk

Using fixed pips for stop loss and take profit risks being stopped out or missing profits in a volatile market. Consider percentage-based or dynamic stop loss/take profit instead.

### Limited Trading Session Risk

Opening positions only during fixed sessions runs the risk of missing potential trades in other hours. Consider expanding the session or adjust dynamically based on real-time situations.

## Optimization Directions

### Parameter Tuning
Optimize parameters like MA length, RSI figures, fixed SL/TP pips, etc., to find the best combination.

### Additional Filters
Add more indicators or conditions to verify signals, e.g., higher volume, reduced BB width, etc., to avoid false breakouts.

### Dynamic SL/TP
Use percentage-based or dynamic stop loss/take profit instead of fixed pips to better handle one-sided market moves.

### Manual Review
Manually review signals or only enter on confirmed breakouts to prevent being trapped.

## Conclusion
The strategy is fairly simple and practical overall, using dual MA channels to determine trends and RSI to filter false breakouts. Risk management via trading hours and loss limits also define the risk tolerance. There is still a large room for improvements, e.g., parameter tuning, better SL/TP mechanisms, etc.

||

## Overview

This strategy uses dual moving averages to form a channel and capture trend direction. Trading signals are generated when price breaks through the channel. RSI is also incorporated to filter false breakouts. It trades only during London session with a maximum of 5 trades per day and a maximum daily loss of 2% of equity.

## Strategy Logic

The strategy employs two moving averages of length 5, one calculated from the highest price and the other from the lowest price, to form a price channel. Long signals are triggered when the close price breaks above the upper band, and short signals when it breaks below the lower band.

To avoid false breakouts, the RSI indicator is added to gauge overbought/oversold levels. Go long only if RSI is above 80, and go short only if RSI is below 20.

Also, the strategy trades only during the London session (3am - 11am), with a maximum of 5 orders per day and a maximum 2% daily loss of equity.

## Advantage Analysis

### Catch the Trend

The dual MA channel can effectively detect the direction of the price trend. Breaking the upper band catches the upside trend, while breaking the lower band catches the downside trend.

### Reduce False Breakouts

Using the RSI overbought/oversold filter can reduce some false breakout signals caused by price fluctuations.

### Effective Risk Control

Trading only during the major session and having a maximum of orders per day limits trading frequency. A maximum 2% daily loss also defines the risk tolerance.

## Risk Analysis

### False Breakout with Volatility

Significant price swings can cause some false breakout signals, leading to unnecessary losses. Parameters can be optimized and more filters added to reduce such risks.

### Fixed SL/TP Risk

Using fixed pips for stop loss and take profit risks being stopped out or missing profits in a volatile market. Consider percentage-based or dynamic stop loss/take profit instead.

### Limited Trading Session Risk

Opening positions only during fixed sessions runs the risk of missing potential trades in other hours. Consider expanding the session or adjust dynamically based on real-time situations.

## Optimization Directions

### Parameter Tuning
Optimize parameters like MA length, RSI figures, fixed SL/TP pips, etc., to find the best combination.

### Additional Filters
Add more indicators or conditions to verify signals, e.g., higher volume, reduced BB width, etc., to avoid false breakouts.

### Dynamic SL/TP
Use percentage-based or dynamic stop loss/take profit instead of fixed pips to better handle one-sided market moves.

### Manual Review
Manually review signals or only enter on confirmed breakouts to prevent being trapped.

## Conclusion
The strategy is fairly simple and practical overall, using dual MA channels to determine trends and RSI to filter false breakouts. Risk management via trading hours and loss limits also define the risk tolerance. There is still a large room for improvements, e.g., parameter tuning, better SL/TP mechanisms, etc.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|5|Length|
|v_input_2_high|0|Source: high|close|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_3|false|Offset|
|v_input_4|5|Length|
|v_input_5_low|0|Source: low|high|close|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_6|false|Offset|
|v_input_7|5|length|
|v_input_8|10|overSold|
|v_input_9|80|overBought|
|v_input_10_close|0|Source RSI: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_11|150|tp|
|v_input_12|80|sl|


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-01 00:00:00
end: 2024-01-16 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © SoftKill21
//@version=4
strategy(title="Moving Average", shorttitle="MA", overlay=true)
timeinrange(res, sess) => time(res, sess) != 0
len = input(5, minval=1, title="Length")
src = input(high, title="Source")
offset = input(title="Offset", type=input.integer, defval=0, minval=-500, maxval=500)
out = sma(src, len)
plot(out, color=color.white, title="MA", offset=offset)

len2 = input(5, minval=1, title="Length")
src2 = input(low, title="Source")
offset2 = input(title="Offset", type=input.integer, defval=0, minval=-500, maxval=500)
out2 = sma(src2, len2)
plot(out2, color=color.white, title="MA", offset=offset2)

length = input( 5 )
overSold = input( 10 )
overBought = input( 80 )
price = input(close, title="Source RSI")

vrsi = rsi(price, length)

longcond= close > out and close > out2 and vrsi > overBought
shortcont = close < out and close < out2 and vrsi < overSold
tp=input(150,title="tp")
sl=input(80,title="sl")


strategy.entry("long",1,when=longcond)
//strategy.close("long",when= close < out2)
strategy.exit("long", profit=tp, loss=sl)
```