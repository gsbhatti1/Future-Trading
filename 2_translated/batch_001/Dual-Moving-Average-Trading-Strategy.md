<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Dual-Moving-Average-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/19593d399da9dc214da.png)
 [trans]
## Overview

The Dual Moving Average Trading Strategy is a quantitative trading strategy that uses two moving average lines with different periods to construct trading signals. This strategy judges market trends and opportunities by calculating the relationship between two moving average lines and performs well in tracking trending markets.

## Strategy Principle

This strategy primarily uses two moving average lines for technical indicator analysis. It defines a short-period 5-day moving average line `ma0` and a longer-period 21-day moving average line `ma1`. The strategy determines the current trend state by comparing whether the differences `osc0` (between price and `ma0`) and `osc1` (between `ma0` and `ma1`) are positive or negative.

When `osc0 > 0` and `osc1 > 0`, it indicates that the short-term moving average has crossed above the long-term one, representing a bullish market. When `osc0 < 0` and `osc1 < 0`, it indicates that the short-term moving average has crossed below the long-term one, representing a bearish market. The strategy opens long positions when a bullish trend is detected and opens short positions when a bearish trend is detected.

After opening a position, the strategy monitors real-time changes in `osc0` and `osc1` to determine the profitability of the position. If `osc0 < 0` and `osc1 < 0` after a long position is opened, it indicates a trend reversal, and the long position is closed. Similarly, if `osc0 > 0` and `osc1 > 0` after a short position is opened, it indicates a trend reversal, and the short position is closed.

## Advantages Analysis

The Dual Moving Average Trading Strategy offers several advantages:

1. Simple operating principles that are easy to understand and implement, making it suitable for beginners in quantitative trading.
2. Follows market trends effectively, resulting in favorable returns in trending markets.
3. Adaptable to different market characteristics by adjusting the period parameters of the moving averages.
4. Can be combined with other indicators or strategies to expand profit potential.

## Risk Analysis

The Dual Moving Average Trading Strategy also presents certain risks:

1. Inability to cut losses promptly during trend reversals may result in significant losses.
2. Frequent stop-losses in ranging markets make profitability challenging.
3. Difficulty in parameter optimization—5-day and 21-day periods may not be optimal.
4. Trading signals may lag, leading to delayed entries that could impact profitability.

## Optimization Directions

The Dual Moving Average Trading Strategy can be optimized in the following ways:

1. Incorporate the VOL indicator to identify genuine trend beginnings and avoid false breakouts.
2. Add supplementary conditions such as price breakouts or increased trading volume to enhance signal reliability.
3. Implement dynamic stop-loss mechanisms for positions to control losses promptly.
4. Optimize parameter thresholds for moving average differences to reduce error rates.
5. Use machine learning methods to automatically optimize the cycle parameters of the moving averages.

## Summary

Overall, the Dual Moving Average Trading Strategy is a classic and practical trend-following strategy. Its straightforward implementation makes it ideal for beginners in quantitative trading. It effectively tracks trends and is highly extensible, allowing easy integration with other technical indicators and strategies. However, the strategy also has limitations that require further optimization to handle abnormal market conditions, reduce risks, and improve stability.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|5|length0|
|v_input_2|21|length1|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("[STRATEGY][RS]MA Strategy test V0", overlay=true)
length0 = input(5)
length1 = input(21)

isinsession = not na(time('1', '0400-1500'))
price = open

ma0 = ema(ema(price, length0), length0)
ma1 = ema(ema(price, length1), length1)
plot(ma0, color=navy)
plot(ma1, color=black)

osc0 = price-ma0
osc1 = ma0-ma1

isbull = osc0 > 0 and osc1 > 0
buy_condition = isinsession and isbull and not isbull[1]
buy_exit_condition = osc0 < 0 and osc1 < 0
strategy.entry("buy", strategy.long, comment="buy", when=buy_condition)
strategy.close(id='buy', when=buy_exit_condition)

isbear = osc0 < 0 and osc1 < 0
sell_condition = isinsession and isbear and not isbear[1]
sell_exit_condition = osc0 > 0 and osc1 > 0
strategy.entry("sell", strategy.short, comment="sell", when=sell_condition)
strategy.close(id='sell', when=sell_exit_condition)

//plot(strategy.equity, title="equity", color=red, linewidth=2, style=areabr)
```

> Detail

https://www.fmz.com/strategy/440078

> Last Modified

2024-01-26 14:45:55