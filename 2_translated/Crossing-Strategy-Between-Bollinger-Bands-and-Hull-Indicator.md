> Name

Crossing-Strategy-Between-Bollinger-Bands-and-Hull-Indicator

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/fc5cfeabbb7b754b78.png)
[trans]

## Overview

This strategy generates trading signals based on the crossover between Bollinger Bands and the Hull Indicator. When the Hull Indicator crosses above the lower Bollinger Band, go long. When the Hull Indicator crosses below the upper Bollinger Band, go short. The strategy combines the breakout strategy of Bollinger Bands and the trend-following strategy of the Hull Indicator, thus utilizing the strengths of both.

## Strategy Principles

The strategy mainly uses the crossover between Bollinger Bands and the Hull Indicator to generate trading signals.

First, Bollinger Bands consist of three lines: the middle line, the upper line, and the lower line. The middle line is an N-day moving average, while the upper and lower lines are the middle line plus and minus one standard deviation. If the price breaks above the upper line, it indicates a breakout opportunity; if the price breaks below the lower line, it indicates a callback opportunity.

Second, the Hull Indicator is a trend-following indicator. It uses the difference between two weighted moving averages of different periods to determine the current trend. If the short-period moving average is above the long-period one, it indicates an uptrend; otherwise, it indicates a downtrend.

The strategy combines the strengths of both indicators. When the Hull Indicator crosses above the lower Bollinger Band, it is considered that the stock price may enter an uptrend, so go long. When the Hull Indicator crosses below the upper Bollinger Band, it is considered that the stock price may enter a downward correction, so go short.

## Strategy Advantages

1. Combines the strengths of Bollinger Bands and Hull Indicator to make trading signals more reliable.

2. Uses the Hull Indicator to determine trend direction and Bollinger Bands to determine support and resistance levels, generating crossover signals to improve profitability.

3. Parameters of both indicators can be optimized for stocks of different cycles to expand applicability.

## Risks and Solutions

1. During range-bound movements, the strategy may generate more false signals, leading to losses. Parameters can be optimized or filters can be added to reduce false signals.

2. Price fluctuations may cause both indicators to issue signals simultaneously. Ensure signal sequencing to avoid erroneous crossover signal judgment. Consider adding stop loss to control losses.

3. The strategy directly sets the position size to 100%. In actual deployment, position management needs to be adjusted to avoid significant losses due to full position opening.

## Optimization Directions

1. Test and optimize the parameters of both indicators to adapt to more stock cycles.

2. Add filters like trading volume or volatility to avoid false signals during consolidation.

3. Optimize stop loss strategies by setting trailing stop loss or stop limit orders.

4. Adjust position management rules by adding re-entry conditions to avoid loss magnification.

## Conclusion

This strategy combines the breakout strategy of Bollinger Bands and the trend-following strategy of the Hull Indicator by using crossover signals between them to achieve both trend-following and breakout effects. The strategy has strong adaptability to medium- and short-term stocks given no major fundamental changes. But parameters, position management, and stop loss strategies still need optimization during actual deployment to make the strategy more robust.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|3|period|
|v_input_2|true|i|
|v_input_3|20|length1|
|v_input_4_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_5|2|mult|
|v_input_6|500|TP|
|v_input_7|500|SL|
|v_input_8|20|TS|
|v_input_9|10|TO|


> Source (PineScript)

``` pinescript
//@version=3
strategy(title="Strategy Hull Bollinger", shorttitle="Hull bollinger", overlay=true, calc_on_order_fills=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100, overlay=false)

n = input(title="period", defval=3)

n2ma = 2 * wma(close, round(n / 2))
nma = wma(close, n)
diff = n2ma - nma
sqn = round(sqrt(n))

n2ma1 = 2 * wma(close[1], round(n / 2))
nma1 = wma(close[1], n)
diff1 = n2ma1 - nma1
sqn1 = round(sqrt(n))

n1 = wma(diff, sqn)
n2 = wma(diff1, sqn)
c = n1 > n2 ? green : red

i = input(1)
PP = close[i]

length1 = input(20, minval=1)
src = input(close, title="Source")
mult = input(2.0, minval=0.001, maxval=10, step=0.2)
basis = sma(src, length1)
dev = mult * stdev(src, length1)
upper = basis + dev
lower = basis - dev

TP = input(500) * 10
SL = input(500) * 10
TS = input(20) * 10
TO = input(10) * 10
CQ = 
```