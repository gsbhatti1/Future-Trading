> Name

Auto-Trading-Strategy-Based-on-STOCH

> Author

ChaoZhang

> Strategy Description


This strategy designs a simple auto trading system based on the STOCH indicator. It is suitable for Forex, stock indices, commodities and can be extended to stocks and crypto markets.

## Strategy Overview

This strategy identifies overbought and oversold statuses using the STOCH indicator combined with PIVOT points to set stop loss positions, realizing trend following. It goes long or short when the STOCH indicator shows overbought or oversold signals. Stop loss points are set near the PIVOT points of the day to effectively control risks. Partial take profit points are set to close partial positions after certain profit level.

## Strategy Logic

This strategy utilizes the crossing of %K and %D lines of the STOCH indicator to generate long and short signals. Specifically, when the %K line crosses above the %D line, it will go long. When the %K line crosses below the %D line, it will go short. This captures the overbought and oversold statuses.

To control risks, the long stop loss point is set near the daily lowest PIVOT point and the short stop loss point is set near the daily highest PIVOT point. This effectively locks in the risks. 

For partial take profit, it closes 50% of the position after a certain profit level after opening the position. This optimizes capital utilization efficiency.

In summary, this strategy Captures overbought and oversold points appropriately; Controls risks using stop loss; and Optimizes capital usage efficiency. It combines Capture, Control and Optimize organically.

## Strategy Strengths

- Using the STOCH indicator effectively captures overbought and oversold statuses. With PIVOT points, it controls risks comprehensively.
- The partial take profit mechanism optimizes capital usage efficiency. Partial closing ensures some profit while retaining room for further gains.
- Customizable parameters allow flexibility based on market conditions and risk preference.
- Simple and clear logic, easy to understand and master for all traders. Clean code facilitates modifications and maintenance.


## Strategy Risks

- As a trend following strategy, it may get stuck in range-bound markets and fail to profit.
- STOCH may generate false signals, causing unnecessary trades. Proper signal filtering is needed to avoid unwanted trades.
- Stop loss near pivot points may be too close after breakouts. Widen stop loss distance properly.
- Some parameters like period may need adjustments for different markets, otherwise it affects strategy performance.
- Backtest only relies on historical data. Cannot guarantee future performance. More uncontrollable factors in live trading.
- Auto trading systems require stable connections to avoid trade execution issues.

## Strategy Optimization

- Add trend filter to avoid trading without clear trends. Such as using MA to determine trend direction.
- Add volume analysis to detect false breakouts and avoid traps. E.g., bullish/bearish volume.
- Adjust parameters like STOCH inputs based on different products and timeframes to optimize performance.
- Consider machine learning algorithms to train models using big data and auto-optimize parameters.
- Set profit factor ratio to introduce risk control and avoid huge losing trades.
- Add more filters like trading conditions, fundamentals to improve win rate.

## Conclusion

This strategy adopts a simple and intuitive trend following approach based on the STOCH indicator to identify overbought/oversold points. With PIVOT stop loss to control risk and partial take profit to optimize capital efficiency. The design covers Capture, Control and Optimize. The logic is simple and customizable. But it also has some risks and can be further optimized. Continuous testing and improvement in live trading is crucial for steady profitability.

||


> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|400|TakeProfitLevel|
|v_input_2|150|TakePartialProfitLevel|
|v_input_3|13|K|
|v_input_4|3|D|
|v_input_5|4|Smooth|

> Source (PineScript)

``` pinescript
/*backtest
start: 2022-09-21 00:00:00
end: 2023-09-27 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Peter_O

//@version=4
strategy(title="Auto-Trading-Strategy-Based-on-STOCH", ...
```