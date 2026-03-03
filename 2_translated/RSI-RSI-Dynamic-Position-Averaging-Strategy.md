<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

> Name

RSI Dynamic Position Averaging Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/83517f5bd3bd11440a.png)
[trans]
## Overview
This strategy combines the Relative Strength Index (RSI) and the martingale position averaging principle. It initiates a long position when RSI falls below the oversold line; if the price continues to decline, it doubles down the position with an index of 2 for profit-taking. This strategy is suitable for spot trading of high-market-cap coins, providing stable long-term gains.

## Strategy Logic
1. Use the RSI indicator to determine market oversold conditions, setting the RSI period to 14 and the oversold threshold at 30.
2. Initiate a long position with 5% of account equity when RSI < 30.
3. If the price declines by 0.5% from the initial entry price, double the position size; if it continues to decline, quadruple the position size.
4. Close positions for profit at every 0.5% increase in price.
5. Repeat these steps in a cycle.

## Advantage Analysis
- Use RSI to identify relative low points for initiating long positions.
- Martingale position averaging lowers average entry prices.
- Small profit-taking ensures continuous and steady gains.
- Suitable for high-market-cap coin spot trading, providing controlled risks.

## Risk Analysis
- Long-term market downturns can expand holding losses.
- No stop loss sets limits on maximum losses.
- Excessive doubling down can increase losses.
- Directional risk remains with a long bias.

## Optimization Directions
1. Incorporate stop loss to limit maximum loss.
2. Optimize RSI parameters for the best overbought/oversold signals.
3. Set appropriate profit-taking ranges based on specific coin volatility.
4. Determine doubling-down pace based on total assets or position sizing rules.

## Summary
This strategy integrates RSI and martingale position averaging to take advantage of oversold conditions by appropriately doubling down, with small profit-taking for steady gains. It can generate consistent returns but carries certain risks that can be mitigated through stop losses and parameter adjustments.
[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|RSI Length|
|v_input_2|30|Oversold Threshold|
|v_input_3|0.5|Profit Target (%)|
|v_input_4|5|Initial Investment % of Equity|

> Source (PineScript)

``` pinescript
/*backtest
start: 2024-01-06 00:00:00
end: 2024-02-05 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Stavolt

//@version=5
strategy("RSI Martingale Strategy", overlay=true, default_qty_type=strategy.cash, currency=currency.USD)

// Inputs
rsiLength = input(14, title="RSI Length")
oversoldThreshold = input(30, title="Oversold Threshold") // Keeping RSI threshold
profitTargetPercent = input(0.5, title="Profit Target (%)") / 100
initialInvestmentPercent = input(5, title="Initial Investment % of Equity")

// Calculating RSI
rsiValue = ta.rsi(close, rsiLength)

// State variables for tracking the initial entry
var float initialEntryPrice = na
var int multiplier = 1

// Entry condition based on RSI
if (rsiValue < oversoldThreshold and na(initialEntryPrice))
    initialEntryPrice := close
    strategy.entry("Initial Buy", strategy.long, qty=(strategy.equity * initialInvestmentPercent / 100) / close)
    multiplier := 1

// Adjusting for errors and simplifying the Martingale logic
// Note: This section simplifies aggressive position size adjustments without loops
if (not na(initialEntryPrice))
    if (close < initialEntryPrice * 0.995) // 0.5% drop from initial entry
        strategy.entry("Martingale Buy 1", strategy.long, qty=((strategy.equity * initialInvestmentPercent / 100) / close) * 2)
        multiplier := 2 // Adjusting multiplier for the next potential entry

    if (close < initialEntryPrice * 0.990) // Further drop
        strategy.entry("Martingale Buy 2", strategy.long, qty=((strategy.equity * initialInvestmentPercent / 100) / close) * 4)
        multiplier := 4

    // Additional conditional entries could follow the same pattern

// Checking for profit target to close positions
if (strategy.position_size > 0 and (close - strategy.position_avg_price) / strategy.position_avg_price >= profitTargetPercent)
    strategy.close_all(comment="Take Profit")
    initialEntryPrice := na // Reset for next cycle

```

> Detail

https://www.fmz.com/strategy/441137

> Last Modified

2024-02-06 09:44:05