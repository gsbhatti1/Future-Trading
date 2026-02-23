<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Three Inside Up Reversal Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/10fc9d799add7abfc1e.png)

[trans]


## Overview

The Three Inside Up Reversal Strategy is a reversal trading strategy that achieves buying low and selling high by identifying specific three-candle K-line patterns. It consists of three candles where the first and second form a bullish engulfing pattern, and the third opens higher than the previous day's close and closes higher than the highest price of the first two candles. This candle combination suggests a possible reversal from a short-term downtrend to an uptrend, serving as a signal for reversal operations.

## Strategy Principle

Key judgment conditions for this strategy include:

1. First candle: Bearish candle, opening price higher than closing price

2. Second candle: Bullish candle, closing price higher than opening price, and closing price lower than the opening price of the previous candle

3. Third candle: Bullish candle, opening price higher than the closing price of the previous candle, and closing price higher than the highest prices of the first two candles

When this signal is detected, we initiate a short position and set take-profit and stop-loss conditions. Specific trading logic includes:

1. When a three inside up pattern is detected, enter a short position at the opening price of this bullish candle

2. Set take-profit condition: If the price increase reaches the inputted take-profit points, end the trade and close the short position

3. Set stop-loss condition: If the price decline reaches the inputted stop-loss points, end the trade and close the short position

4. When the price reaches either the take-profit or stop-loss point, clear the position and wait for the next round of trading signals

By doing so, we promptly go short upon detecting an upward reversal signal, decisively taking profits or cutting losses when profits meet expectations or losses exceed controllable ranges, thus implementing a reversal trading strategy of buying low and selling high.

## Strategy Advantages

- Captures reversal turning points, achieving the goal of reversal trading

- Shorting at highs and going long at lows aligns with trend trading logic

- Features clear entry, take-profit, and stop-loss mechanisms

- Simple three-candle pattern, easy to identify and implement

- Customizable take-profit and stop-loss points for risk control

- Concise and clear code implementation, easy to understand and optimize

In summary, this strategy captures reversals, controls risks, and is simple and reliable, making it a practical and efficient short-term reversal trading strategy.

## Strategy Risk

- Inaccurate identification of reversal patterns might result in non-reversal signals

- Improper setting of take-profit and stop-loss points might cause premature exits or miss larger profits

- Frequent trading expectations carry the risk of over-trading

- Areas such as signal identification and position management still have room for optimization

- Stock selection requires caution; this strategy suits more volatile stocks

- Need to consider the impact of transaction costs and slippage on profitability

- Continuous optimization and monitoring are necessary to respond timely to market changes

Overall, through optimizing parameter settings, strict stock selection, continuous monitoring, and other measures, the trading risks of this strategy can be controlled.

## Optimization Directions

- Optimize candle pattern parameters to improve recognition accuracy

- Improve take-profit and stop-loss mechanisms for better risk-reward balance

- Combine with other technical indicators to filter signals and enhance decision-making accuracy

- Add position management mechanisms to dynamically adjust positions based on market conditions

- Optimize fund management for better profit and loss equilibrium

- Test different holding times to determine the best holding period

- Optimize code structure and add annotations to make the strategy clearer

- Add real-time simulation comparisons to verify strategy effectiveness

- Adjust stock pool to test industry and individual stock adaptability of the strategy

- Continuously track strategy performance, promptly identify issues, and adjust strategies

## Summary

The Three Inside Up Reversal Strategy identifies specific three-candle patterns and shorts when a short-term downtrend reversal signal is detected to gain profits. The strategy has clear trading logic, take-profit and stop-loss mechanisms for risk control, and is easy to implement and optimize, making it a reliable and practical short-term reversal trading strategy. However, there are certain uncertainty risks which need to be mitigated through parameter optimization, risk control, and continuous tracking and optimization to achieve stable excess returns in live trading.

||


## Overview

The Three Inside Up reversal strategy is a reversal trading strategy that aims to buy low and sell high by identifying specific three-bar candlestick patterns. It consists of three bars where the first two form a bullish harami pattern and the third bar opens above the previous close and closes above the highs of the first two bars. This candlestick combination indicates a potential reversal from a downtrend to an uptrend and signals an opportunity to enter a reversal trade.

## Strategy Logic

The key conditions for this strategy are:

1. Bar 1: Bearish candle, open higher than close 

2. Bar 2: Bullish candle, close higher than open and lower than Bar 1 open

3. Bar 3: Bullish candle, open higher than Bar 2 close and close higher than highs of Bars 1 and 2

When this pattern is detected, we take a short position and set profit take and stop loss levels. The trading logic is as follows:

1. Enter short at the open of Bar 3 when Three Inside Up pattern is identified

2. Set profit target: Close trade and flatten position if price rises by the input number of profit points  

3. Set stop loss: Close trade and flatten if price declines by the input number of loss points

4. Clear position when target or stop is hit, await next signal

This allows us to quickly enter a short when an uptrend reversal signal is identified, and realize gains or limit losses using pre-defined profit and stop levels, implementing a low buy high sell reversal strategy.

## Advantages

- Captures reversal points for reversal trading

- Shorts tops and buys bottoms aligning with trends  

- Clear entry, profit take, and stop loss mechanics

- Simple 3-bar pattern, easy to identify and implement

- Customizable profit take and stop loss points to control risk

- Code is simple, clean, easy to understand and optimize

In summary, this strategy leverages pattern recognition, risk management, simplicity, and reliability making it an effective short-term reversal trading strategy.

## Risks

- Pattern may be misidentified, leading to false signals

- Inadequate profit take or stop loss levels could lead to premature exit or missed profits

- Frequent trading increases overtrading risk 

- Entry, position sizing, and management can be further optimized

- Careful stock selection required, better for volatile stocks

- Impact of commissions and slippage on profits

- Requires ongoing monitoring and tuning for changing markets

Proper parameter optimization, stock selection, monitoring and other measures can help control the risks.

## Enhancement Opportunities

- Optimize pattern parameters to improve accuracy

- Refine profit take and stop loss for better risk-reward

- Add filters using other indicators to improve signal reliability 

- Incorporate dynamic position sizing aligned to market conditions

- Optimize capital allocation for better profit balancing

- Test different holding periods to determine optimal duration

- Streamline code with comments for clarity

- Backtest versus live performance to validate efficacy

- Adjust stock universe and test sector and name fit

- Continuously track performance and tune as required

## Conclusion

The Three Inside Up Reversal strategy aims to profit from shorting tops when an uptrend reversal signal is identified based on a specific three-candlestick pattern. With clear logic, risk controls, ease of use, and optimization potential, it is a reliable and practical short-term reversal trading strategy. But uncertainties exist requiring ongoing optimizations, risk management, and monitoring to generate consistent excess returns in live trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Take Profit pip|
|v_input_2|20|Stop Loss pip|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-29 00:00:00
end: 2023-10-29 00:00:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 12/02/2019
//    This is a three candlestick bullish reversal pattern consisting of a 
//    bullish harami pattern formed by the first 2 candlesticks then followed 
//    by up candlestick with a higher close than the prior candlestick.
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
strategy(title = "Three Inside Up Backtest", overlay = true)
input_takeprofit = input(20, title="Take Profit pip", step=0.01)
input_stoploss = input(20, title="Stop Loss pip", step=0.01)
barcolor(open[2] > close[2] ? close[1] > open[1] ? close[1] <= open[2] ? close[2] <= open[1] ? close[1] - open[1] < open[2] - close[2] ? close > open ? close > close[1] ? open > open[1] ? close > open[2] ? yellow :na :na : na : na : na:na : na : na : na)
posprice = 0.0
pos = 0.0
barcolor(nz(pos[1], 0) == -1 ? red: nz(pos[1], 0) == 1 ? green : blue ) 
posprice := open[2] > close[2] ? close[1] > open[1] ? close[1] <= open[2] ? close[2] <= open[1] ? close[1] - open[1] < open[2] - close[2] ? close > open ? close > close[1] ? open > open[1] ? close > open[2]  ? close :nz(posprice[1], 0) :nz(posprice[1], 0) : nz(posprice[1], 0) : nz(posprice[1], 0) :nz(posprice[1], 0):nz(posprice[1], 0):nz(posprice[1], 0):nz(posprice[1], 0):nz(posprice[1], 0) 
pos := iff(posprice > 0, -1, 0)
if (pos == 0) 
    strategy.close_all()
if (pos == -1)
    strategy.entry("Short", strategy.short)
posprice := iff(low <= posprice - input_takeprofit and posprice > 0, 0 ,  nz(posprice, 0))
posprice := iff(high >= posprice + input_stoploss and posprice > 0, 0 ,  nz(posprice, 0))
```

> Detail

https://www.fmz.com/strategy/430583

> Last Modified

2023-10-30 15:36:07