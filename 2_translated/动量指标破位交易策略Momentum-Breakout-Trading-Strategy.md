> Name

Momentum-Breakout-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]

## Overview

This strategy uses the momentum indicator Bollinger Bands for breakout trading, primarily determining if price breaks through the upper or lower Bollinger Bands to generate buy/sell signals.

## Principles 

The strategy is primarily based on using Bollinger Bands to determine trend direction. Bollinger Bands consist of a middle band based on a moving average and upper/lower bands defined by standard deviations. The middle band is an n-period moving average, the upper band is the middle band + 2 times the standard deviation, and the lower band is the middle band - 2 times the standard deviation. When price approaches the upper band, it indicates overbought conditions; when it approaches the lower band, it signals oversold conditions.

Specifically, the strategy first calculates the highest high and lowest low over the last n periods, and then calculates the center price ((highest high + lowest low)/2). It then uses an exponential moving average of the distance between the closing price and the center price to form the middle band, and adds/subtracts 2 times the standard deviation above and below this to create the upper and lower bands.

When the closing price breaks through the upper band, it signals an uptrend; when it breaks the lower band, it signals a downtrend. The strategy goes long when the upper band is broken, and short when the lower band is broken.

In addition, the strategy incorporates a counter-trend mechanism. When the price breaks the upper band but the MACD is declining, it will take a contrarian short position.

## Advantages

1. Using Bollinger Bands to determine trend direction provides certain trend following capability.
2. Counter-trend design allows profiting from reversals.
3. Customizable parameters like period and standard deviation multiples make it adaptable to different trading horizons.
4. Disable counter-trend trading to reduce risk.

## Risks and Mitigations

1. Bollinger Bands work best for high volatility stocks, may not be suitable for stable commodities or indices. Can test different period parameters.
2. Breakout signals may have false breakouts. Can add filters with other indicators.
3. Counter-trend trading can further increase losses. Can disable counter-trend module.
4. Drawdowns may be significant. Can adjust position sizing.

## Enhancement Opportunities

1. Consider adding trend filter to avoid whipsaw in non-directional markets.
2. Test different standard deviation multiples to find optimal parameters.
3. Incorporate stop loss to control single trade loss.
4. Optimize entry and add-on logic for clearer trading signals.

## Summary

The strategy uses Bollinger Bands as the primary indicator and trades based on trend breakouts. With simple parameters, it provides basic trend following capabilities. But false breakout risks exist, requiring additional filters. Parameters, stop loss, and risk controls can be enhanced. Overall, it serves as a reasonable baseline breakout strategy.

[/trans]

> Strategy Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| v_input_1 | true    | Long        |
| v_input_2 | true    | Short       |
| v_input_3 | false   | take, %     |
| v_input_4 | true    | Bands Entry |
| v_input_5 | false   | Counter-trend entry |
| v_input_6 | 10      | Body length |
| v_input_7 | true    | Trend bars  |
| v_input_8 | 20      | Period      |
| v_input_9 | true    | Show Bands  |
| v_input_10 | true   | Show Background |
| v_input_11 | 1900    | From Year   |
| v_input_12 | 2100    | To Year     |
| v_input_13 | true    | From Month  |
| v_input_14 | 12      | To Month    |

> Source (PineScript)

```pinescript
/*backtest
start: 2023-08-18 00:00:00
end: 2023-09-17 00:00:00
period: 4h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//Noro
//2018

//@version=2
strategy("Noro's Bands Scalper Strategy v1.6", shorttitle = "Scalper str 1.6", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100.0, pyramiding = 0)

//Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
takepercent = input(0, defval = 0, minval = 0, maxval = 1000, title = "take, %")
needbe = input(true, defval = true, title = "Bands Entry")
needct = input(false, defval = false, title = "Counter-trend entry")
bodylen = input(10, defval = 10, minval = 0, maxval = 50, title = "Body length")
trb = input(1, defval = 1, minval = 1, maxval = 5, title = "Trend bars")
len = input(20, defval = 20, minval = 2, maxval = 200, title = "Period")
needbb = input(true, defval = true, title = "Show Bands")
needbg = input(true, defval = true, title = "Show Background")
fromyear = input(1900, defval = 1900, minval = 1900, maxval = 2100, title = "From Year")
toyear = input(2100, defval = 2100, minval = 1900, maxval = 2100, title = "To Year")
frommonth = input(1, defval = 1, minval = 1, maxval = 12, title = "From Month")
tomonth = input(12, defval = 12, minval = 1, maxval = 12, title = "To Month")
src = close

//PriceChannel 1
lasthigh = highest(src, len)
lastlow = lowest(src, len)
center = (lasthigh + lastlow) / 2

//Distance
dist = abs(src - center)

```