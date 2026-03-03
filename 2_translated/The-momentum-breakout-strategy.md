> Name

The-momentum-breakout-strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/f308115b184cce4fc3.png)
[trans]
## Overview
The momentum breakout strategy is a trend-following strategy that tracks the market's momentum. It combines multiple indicators to determine whether the market is currently in an upward or downward trend and enters long positions when breaking through key resistance levels, and short positions when breaking through key support levels.

## Strategy Logic
This strategy mainly uses Donchian Channels of different timeframes to determine market trends and key price levels. Specifically, when prices break through the upper rail of a longer-term Donchian Channel such as 40 days, it is judged as an uptrend. Together with additional filters like new highs within the year and the alignment of moving averages, long signals are triggered. When prices break below the lower rail of the longer-term Donchian Channel, it is judged as a downtrend. Together with filters like new lows within the year, short signals are triggered.

In terms of exiting positions, this strategy provides two options: fixed invalidation line and trailing stop loss. The fixed invalidation line uses the lower/upper rail of a shorter Donchian Channel such as 20 days. The trailing stop loss calculates a dynamic stop loss line each day based on ATR values. Both methods can effectively control risks.

## Advantage Analysis
This strategy combines trend judgment and breakout operations, which can effectively capture short-term directional opportunities in the market. Compared with single indicators, it uses multiple filters that can filter out some false breakouts and improve the quality of entry signals. In addition, the application of stop loss strategies also enhances its resilience and can effectively control losses even if the market pulls back briefly.

## Risk Analysis
The main risk of this strategy is that prices may fluctuate violently, triggering stop losses to exit positions. If prices reverse rapidly afterwards, opportunities could be missed. Additionally, the use of multiple filters may also filter out some opportunities and reduce the frequency of trades.

To reduce risks, ATR multiples can be adjusted or Donchian Channel intervals can be widened to decrease the likelihood of stop loss being hit. Some filters could also be removed or relaxed to increase entry frequency, but risks would also increase.

## Optimization Directions
This strategy can be optimized in the following aspects:
1. Optimize the lengths of the Donchian Channels to find the best combination of parameters.
2. Try different types of moving averages as filter indicators.
3. Adjust the ATR multiplier or use fixed point stop loss.
4. Add more trend judging indicators like MACD.
5. Optimize the lookback periods for new highs/lows within the year, etc.

By testing different parameters, the optimum combination balancing risks and returns can be found.

## Conclusion
This strategy combines multiple indicators to determine trend direction and triggers trades at key breakout levels. Its stop loss mechanism also makes it resilient to risks. By optimizing parameters, stable excess returns can be achieved. It suits investors who have no clear view on the market but wish to follow trends.
[/trans]

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|40|donchianEntryLength|
|v_input_2|20|donchianExitLength|
|v_input_3|true|considerNewLongTermHighLows|
|v_input_4|120|shortHighLowPeriod|
|v_input_5|180|longHighLowPeriod|
|v_input_6|true|considerMAAlignment|
|v_input_7|0|Moving Average Type: ema, sma, hma, rma, vwma, wma|
|v_input_8|40|LookbackPeriod|
|v_input_9|22|atrLength|
|v_input_10|4|atrMult|
|v_input_11|0|Exit Strategy: tsl, dc|
|v_input_12|true|considerYearlyHighLow|
|v_input_13|10|backtestYears|

> Source (PineScript)

```pinescript
/*backtest
start: 2024-01-23 00:00:00
end: 2024-02-22 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © HeWhoMustNotBeNamed

//@version=4
strategy("BuyHigh-SellLow Strategy", overlay=true, initial_capital = 10000, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, commission_type = strategy.commission.percent, pyramiding = 1, commission_value = 0.01, calc_on_order_fills = true)
donchianEntryLength = input(40, step=10)
donchianExitLength = input(20, step=10)

considerNewLongTermHighLows = input(true)
shortHighLowPeriod = input(120, step=10)
longHighLowPeriod = input(180, step=10)

considerMAAlignment = input(true)
MAType = input(title="Moving Average Type", defval="ema", options=["ema", "sma", "hma", "rma", "vwma", "wma"])
LookbackPeriod = input(40, minval=10, step=10)

atrLength = input(22)
atrMult = input(4)

exitStrategy = input
```