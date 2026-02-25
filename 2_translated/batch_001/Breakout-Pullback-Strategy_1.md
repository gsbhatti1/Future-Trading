<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

A Trend Following Breakout Pullback Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/181c883399e6520b891.png)
[trans]

## Overview

The breakout pullback strategy is a trend-following strategy. Its basic principle is to go long or short when the price breaks above the high or below the low of the previous candle, and then let profits run after setting take-profit and stop-loss levels.

## Strategy Principle  

This strategy mainly determines entry timing by checking whether the price breaks out above the high or below the low of the previous candle. The specific logic is:

If the current candle's high is higher than the previous candle's high, a long signal is generated.

If the current candle's low is lower than the previous candle's low, a short signal is generated.

Enter positions immediately upon receiving long or short signals. After entering, set take-profit at 50 pips and stop-loss at 100 pips.

Actively exit the trade when loss reaches or exceeds the stop-loss level or profit reaches or exceeds the take-profit level.

## Advantages Analysis

This breakout pullback strategy has the following advantages:

1. Simple operational logic that is easy to implement.
2. Effectively captures the beginning of trends for timely entry.
3. Allows profits to continue running after setting take-profit and stop-loss, avoiding premature exits.
4. Strong drawdown and risk control capabilities.

## Risk Analysis 

This strategy also carries certain risks:

1. Breakout signals might be false breakouts, leading to incorrect entries.
2. In consolidation markets, there is a risk of being trapped.
3. Proper take-profit and stop-loss pip settings are necessary to control risk.

## Optimization Directions

The strategy can be further optimized in several ways:

1. Add validity checks for price breakouts to avoid false signals. For example, incorporate indicator filtering and volume verification.

2. Add trend identification mechanisms to avoid being trapped during consolidation periods. Incorporate trend indicators like moving averages.

3. Optimize take-profit and stop-loss strategies, such as trailing stops or moving stops after profit, to maximize gains.

4. Perform parameter optimization to find the best take-profit and stop-loss pip values.

## Summary

Overall, this breakout pullback strategy features simple logic, ease of implementation, and effective trend capture with strong risk and drawdown control. With further optimization, it can become a highly practical quantitative strategy.

||

## Overview  

The breakout pullback strategy is a trend following strategy. Its basic principle is to go long or short when the price breaks through the high or low of the previous candlestick and let the profit continue to run after setting the take profit and stop loss.  

## Strategy Logic   

The core logic of this strategy is to determine the entry timing by judging whether the price breaks through the high or low of the previous candlestick. The specific logic is:  

If the high of the current candlestick is higher than the high of the previous candlestick, a long signal is triggered.  

If the low of the current candlestick is lower than the low of the previous candlestick, a short signal is triggered.

Once receiving the long or short signal, enter the position immediately. After entering the position, set the take profit to 50 pips and stop loss to 100 pips.  

When the loss is greater than or equal to the stop loss pips or profit is greater than or equal to the take profit pips, exit the position actively.

## Advantage Analysis   

This breakout pullback strategy has the following advantages:  

1. The logic is simple and easy to implement.  
2. It can effectively capture the beginning of trends and enter positions in a timely manner.
3. Setting take profit and stop loss allows profits to continue to run, avoiding premature exits.  
4. Good ability of controlling drawdowns and risks.

## Risk Analysis   

This strategy also has some risks:   

1. Breakout signals may be false breakouts, causing wrong entries.
2. It is easy to be trapped in range-bound consolidate markets.   
3. Reasonable take profit and stop loss pips should be set to control risks.  

## Optimization Directions  

The strategy can be further optimized in the following aspects:  

1. Add validity check for price breakouts to avoid false breakouts, such as using indicators filters and volume confirmation.  

2. Add trend determination mechanism to avoid trapping risks in range-bound markets. Moving average and other trend indicators can be used.
  
3. Optimize take profit and stop loss strategy, such as trailing stop loss, moving stop loss after profit, etc, to maximize profits.
  
4. Parameter optimization to find the optimal take profit and stop loss pips.

## Conclusion  

In general, this breakout pullback strategy has the advantage of simple logic, easy implementation, and effectively capturing trend starts. It also has good ability of controlling risks and drawdowns. With further optimizations, it can become a very practical quant strategy.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|50|Take Profit (in pips)|
|v_input_2|100|Stop Loss (in pips)|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-01-25 00:00:00
end: 2024-01-31 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Breakout Strategy", shorttitle="BS", overlay=true)

// Input for take profit and stop loss in pips
tp_pips = input(50, title="Take Profit (in pips)")
sl_pips = input(100, title="Stop Loss (in pips)")

// Calculate take profit and stop loss levels in points
tp_level = tp_pips * syminfo.mintick
sl_level = sl_pips * syminfo.mintick

// Function to check if a breakout has occurred
breakout(high_or_low) =>
    high_or_low > request.security(syminfo.tickerid, "D", high[1]) ? true : false

// Buy condition
buy_condition = breakout(high)
strategy.entry("Buy", strategy.long, when=buy_condition)

// Sell condition
sell_condition = breakout(low)
strategy.entry("Sell", strategy.short, when=sell_condition)

// Take profit and stop loss conditions for Buy
tp_buy_condition = strategy.position_avg_price + tp_level
sl_buy_condition = strategy.position_avg_price - sl_level
strategy.exit("Take Profit/Close Buy", from_entry="Buy", profit=tp_buy_condition, loss=sl_buy_condition)

// Take profit and stop loss conditions for Sell
tp_sell_condition = strategy.position_avg_price - tp_level
sl_sell_condition = strategy.position_avg_price + sl_level
strategy.exit("Take Profit/Close Sell", from_entry="Sell", profit=tp_sell_condition, loss=sl_sell_condition)

```

> Detail

https://www.fmz.com/strategy/440715

> Last Modified

2024-02-01 14:37:02