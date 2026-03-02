> Name

Mean-Reversion-with-Incremental-Entry-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1d4d55de4742fc476d7.png)
[trans]
## Overview

The Mean Reversion with Incremental Entry strategy is a sophisticated quantitative trading script designed by HedgerLabs, focusing on the mean reversion technique in financial markets. This strategy caters to traders who prefer a systematic approach and emphasize gradual entry based on price movements relative to moving averages.

## Strategy Logic

At the core of this strategy lies the Simple Moving Average (SMA). All entries and exits are centered around the SMA. Traders can customize the MA length to fit different trading styles and timeframes.

The unique feature of this strategy is its incremental entry mechanism. When the price deviates from the MA by a certain percentage, it initiates the first position. Subsequently, as the price continues to deviate further from the MA, additional entries are made in predefined increments, as defined by the trader. This approach aims to capture higher returns during increased market volatility.

The strategy intelligently manages positions by going long when prices are below the MA and short when above, adapting to varying market conditions. Exit points are set when the price touches the MA, aiming to catch potential reversals for optimal position closure.

Enabling `calc_on_every_tick`, this strategy continuously evaluates market conditions to respond promptly.

## Advantage Analysis

The Mean Reversion with Incremental Entry strategy offers several advantages:

1. High systematization reduces the risk of subjective errors.
2. Incremental entry can yield higher profits during periods of high volatility.
3. Customizable parameters like MA period cater to different instruments.
4. Intelligent position management automatically adjusts long/short positions.
5. Optimal exit points are chosen to capture reversals and close positions.

## Risk Analysis

Some risks associated with this strategy include:

1. Dependence on technical indicators, which can lead to false signals.
2. Inability to identify market trends, leading to potential drawdowns.
3. Incorrect MA parameter settings may result in frequent stopouts.
4. Larger position sizes due to incremental entry.

Optimizing exits, adding trend filters, and adjusting position sizing can mitigate these risks.

## Optimization Directions

This strategy can be improved by:

1. Adding trend filters to avoid unfavorable trades.
2. Optimizing entry increments based on volatility.
3. Incorporating trailing stops to lock in profits.
4. Experimenting with different types of moving averages.
5. Applying filters to reduce false signals.

## Conclusion

The Mean Reversion with Incremental Entry strategy focuses on mean reversion techniques using a systematic incremental position sizing approach, adaptable across various trading instruments. It performs well in volatile markets and is suitable for short-term systematic traders.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|30|MA Length|
|v_input_float_1|5|Initial Percent for First Order|
|v_input_float_2|true|Percent Step for Additional Orders|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-29 00:00:00
end: 2024-01-28 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Mean Reversion with Incremental Entry by HedgerLabs", overlay=true, calc_on_every_tick=true)

// Input for adjustable settings
maLength = input.int(30, title="MA Length", minval=1)
initialPercent = input.float(5, title="Initial Percent for First Order", minval=0.01, step=0.01)
percentStep = input.float(1, title="Percent Step for Additional Orders", minval=0.01, step=0.01)

// Calculating Moving Average
ma = ta.sma(close, maLength)

// Plotting the Moving Average
plot(ma, "Moving Average", color=color.blue)

var float lastBuyPrice = na
var float lastSellPrice = na

// Function to calculate absolute price percentage difference
pricePercentDiff(price1, price2) =>
    diff = math.abs(price1 - price2) / price2 * 100
    diff

// Initial Entry Condition Check Function
initialEntryCondition(price, ma, initialPercent) =>
    pricePercentDiff(price, ma) >= initialPercent

// Enhanced Entry Logic for Buy and Sell
if (low < ma)
    if (na(lastBuyPrice))
        if (initialEntryCondition(low, ma, initialPercent))
            strategy.entry("Buy", strategy.long)
            lastBuyPrice := low
    else
        if (low < lastBuyPrice and pricePercentDiff(low, lastBuyPrice) >= percentStep)
            strategy.entry("Buy", strategy.long)
            lastBuyPrice := low

if (high > ma)
    if (na(lastSellPrice))
        if (initialEntryCondition(high, ma, initialPercent))
            strategy.entry("Sell", strategy.short)
            lastSellPrice := high
    else
        if (high > lastSellPrice and pricePercentDiff(high, lastSellPrice) >= percentStep)
            strategy.entry("Sell", strategy.short)
            lastSellPrice := high

// Exit
```