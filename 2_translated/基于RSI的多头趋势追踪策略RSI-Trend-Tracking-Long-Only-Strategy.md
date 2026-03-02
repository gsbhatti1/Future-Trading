<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

---

**Name**

RSI-Based Long Only Trend Tracking Strategy RSI-Trend-Tracking-Long-Only-Strategy

**Author**

ChaoZhang

**Strategy Description**

![IMG](https://www.fmz.com/upload/asset/1483945845b7d65d5e7.png)
[trans]

## Overview

This strategy implements a long-only trend tracking approach using the RSI indicator. It enters into a long position when the RSI reaches an overbought level and employs fixed take profit and stop loss ratios. The strategy is simple and straightforward, suitable for bull markets.

## Strategy Logic

The strategy uses the RSI indicator to determine entry signals. When the RSI drops below 25 (over-sold level), it enters a long position. After entering, fixed take profit and stop loss levels are set based on the entry price. Specifically, the take profit level is 7% above the entry price, while the stop loss level is 3.5% below the entry price.

The strategy only goes long and does not go short, making it a trend tracking strategy. It aims to capture the upward trend after prices bounce back from over-sold RSI levels. When the RSI is over-sold, it suggests that the price might be in a short-term oversold condition. Entering a long position at this point can benefit from the rebound.

## Advantage Analysis

The advantages of this strategy include:

1. Clear and simple logic, easy to understand and implement.
2. Only goes long, avoiding risks associated with regularity FD003.
3. Long signals come from the RSI indicator, effectively identifying over-sold reversal opportunities.
4. Fixed take profit/stop loss ratios control single trade losses.

## Risk Analysis

There are also some risks associated with this strategy:

1. It works better in bull markets and cannot generate profits in bear markets.
2. It misses opportunities to enter based on new high breakouts.
3. The fixed stop loss ratio does not adapt to changing market volatility.
4. Incorrect RSI parameter settings may lead to over-trading or insufficient signals.

## Optimization Directions

The strategy can be optimized by:

1. Adding a short-side strategy to profit from bear markets.
2. Considering additional entry conditions, such as new high breakouts or pattern signals, to improve accuracy.
3. Optimizing RSI parameters through training to reduce errors.
4. Making the stop loss mechanism more intelligent by combining it with ATR (Average True Range) to adjust based on volatility.

## Summary

Overall, this strategy has a clear and straightforward logic for identifying over-sold opportunities and tracking bull trends. Its advantages include simplicity and reliability but have limitations in only working for bull markets, with significant room for improvement. This can serve as the foundation for a long-side trend tracking strategy. Additional conditions, filters, and indicators could be introduced to turn it into a reliable positive swing system.

||

## Overview  

This strategy implements a long-only trend tracking approach based on the RSI indicator. It goes long when the RSI reaches an overbought level and uses fixed take profit and stop loss ratios. The strategy is simple and straightforward, suitable for bull markets.

## Strategy Logic

The strategy uses the RSI indicator to determine entry signals. When the RSI drops below 25 (over-sold level), it enters a long position. After entering, fixed take profit and stop loss levels are set based on the entry price. Specifically, the take profit level is 7% above the entry price, while the stop loss level is 3.5% below the entry price.

The strategy only goes long and does not go short, making it a trend tracking strategy. It aims to capture the upward trend after prices bounce back from over-sold RSI levels. When the RSI is over-sold, it suggests that the price might be in a short-term oversold condition. Entering a long position at this point can benefit from the rebound.

## Advantage Analysis

The advantages of this strategy include:

1. Clear and simple logic, easy to understand and implement.
2. Only goes long, avoiding risks associated with regularity FD003.
3. Long signals come from the RSI indicator, effectively identifying over-sold reversal opportunities.
4. Fixed take profit/stop loss ratios control single trade losses.

## Risk Analysis

There are also some risks associated with this strategy:

1. It works better in bull markets and cannot generate profits in bear markets.
2. It misses opportunities to enter based on new high breakouts.
3. The fixed stop loss ratio does not adapt to changing market volatility.
4. Incorrect RSI parameter settings may lead to over-trading or insufficient signals.

## Improvement Areas

The strategy can be improved by:

1. Adding a short-side strategy to profit from bear markets.
2. Considering additional entry conditions, such as new high breakouts or pattern signals, to improve accuracy.
3. Optimizing RSI parameters through training to reduce errors.
4. Making the stop loss mechanism more intelligent by combining it with ATR (Average True Range) to adjust based on volatility.

## Conclusion

In summary, this strategy has a clear and straightforward logic for identifying over-sold opportunities and tracking bull trends. Its advantages include simplicity and reliability but have limitations in only working for bull markets, with significant room for improvement. This can serve as the foundation for a long-side trend tracking strategy. Additional conditions, filters, and indicators could be introduced to turn it into a reliable positive swing system.

---

**Strategy Arguments**

|Argument|Default|Description|
|---|---|---|
|v_input_1|14|RSI Length|
|v_input_2|25|Overbought Level|
|v_input_3|0.07|Long Take Profit %|
|v_input_4|0.035|Long Stop Loss %|

**Source (PineScript)**

```pinescript
/*backtest
start: 2023-12-28 00:00:00
end: 2024-01-03 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI BENI strategy (Long Only)", overlay=true, shorttitle="RSI BENI Long")

length = input(14, title="RSI Length")
overSold = input(25, title="Overbought Level")
price = close
vrsi = ta.rsi(price, length)

// Plot Entry and Levels in the Chart for Over-sold Zones
plotshape(series=strategy.position_avg_price > 0 and vrsi[1] <= overSold and vrsi > overSold,
         title="Long Entry",
         color=color.green,
         style=shape.triangleup,
         size=size.small,
         location=location.belowbar)

long_tp_inp = input(0.07, title='Long Take Profit %')
long_sl_inp = input(0.035, title='Long Stop Loss %')

long_take_level = strategy.position_avg_price * (1 + long_tp_inp)
long_stop_level = strategy.position_avg_price * (1 - long_sl_inp)

plot(long_take_level, color=color.green, title="Long Take Profit Level", linewidth=2)
plot(long_stop_level, color=color.red, title="Long Stop Loss Level", linewidth=2)

if (not na(vrsi))
    if vrsi < overSold
        // Long Entry
        strategy.entry("Long", strategy.long, comment="enter long")

        strategy.exit("Take Profit/Stop Loss", "Long", limit=long_take_level, stop=long_stop_level)
```

**Detail**

https://www.fmz.com/strategy/437800

**Last Modified**

2024-01-05 16:19:57