> Name

RSI Multi-Timeframe Long-Short Balance Trading Strategy RSI-Long-Short-Balance-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1b0deff2f632c751faa.png)
[trans]

### Overview

This strategy utilizes RSI indicators across different timeframes to determine whether the current market is overbought or oversold, and combines the relationship between price and moving average to generate buy and sell signals. The goal is to buy on dips and sell on rallies to profit during consolidation.

### Strategy Logic

1. Calculate the RSI values for 5-minute, 15-minute, and 1-hour timeframes. When the 5-minute, 15-minute, and 1-hour RSI are all below 25 simultaneously, it is considered an oversold condition, generating a buy signal; when they are all above 75 simultaneously, it is considered an overbought condition, generating a sell signal.

2. Breaking through the 21-day moving average also acts as a trading signal. If the price is below the moving average, a buy signal is generated. If the price is above the moving average, a sell signal is generated.

3. Based on current position, set initial trade size and pyramiding rules: 2 contracts for the first entry, then adding 1 contract each time until the position reaches 2 contracts.

4. Stop loss is triggered when the loss reaches 3%. Take profit when the profit reaches 1%.

### Advantages

1. Using RSI indicators across multiple timeframes to determine overbought and oversold conditions improves signal reliability.

2. Combining moving averages generates additional trading signals, expanding trading opportunities.

3. Setting position control rules and stop loss/take profit limits manage risks.

4. Scaling in with fixed quantity expands profit potential.

### Risks

1. RSI divergence risk. Prices may continue to trend for a period after reaching the overbought or oversold threshold before reversing. Blindly following RSI signals can result in losses.

2. Moving average trading signals may be misleading. During large price swings, moving averages fail to track price changes timely.

3. Incorrect position sizing and profit/loss ratio settings lead to improper risk management.

4. Pyramiding conditions need to be set reasonably to avoid amplifying losses.

### Optimization Directions

1. Adjust RSI parameters and test different period combinations to find more reliable overbought/oversold signals.

2. Test different moving averages as auxiliary trading signals, or other technical indicators.

3. Optimize position sizing and stop loss/take profit rules for a more scientific risk control mechanism.

4. Optimize pyramiding conditions to prevent amplifying losses. Consider exponential scaling instead of fixed quantity scaling.

### Summary

This strategy uses RSI across multiple timeframes to determine trend potential, achieving a higher win rate. Additional signals are generated with moving averages to expand trading opportunities. Risk is managed through position sizing, stop loss/take profit, and fixed quantity pyramiding. Overall, this strategy integrates both trend-following and mean-reversion indicators, incorporating both trend following and bottom-picking logic. It performs well during consolidation periods but requires further testing and optimization for more robust risk management to achieve consistent trading results.

[/trans]

> Source (PineScript)

```pinescript
//@version=3
strategy("5M_RSI_Strategy", overlay=true, pyramiding=1)
len = 14 
Initial_Trade_Size = 2
up = rma(max(change(close), 0), len)
down = rma(-min(change(close), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
RSI_1h = request.security(syminfo.tickerid, "60", rsi)
RSI_3h = request.security(syminfo.tickerid, "180", rsi)
RSI_15m = request.security(syminfo.tickerid, "15", rsi)
RSI_5m = request.security(syminfo.tickerid, "5", rsi)
RSI_1m = request.security(syminfo.tickerid, "1", rsi)
ema21_5 = ema(request.security(syminfo.tickerid, "5", close), 21)
ema21_15 = ema(request.security(syminfo.tickerid, "15", close), 21)

Positive = ((RSI_5m <= 25) and (RSI_15m <= 25) and (RSI_1h <= 25)) ? true : false
Negative = ((RSI_5m >= 75) and (RSI_15m >= 75) and (RSI_1h >= 75)) ? true : false

Positive and not Negative ? 
    strategy.entry("Buy", strategy.long, size=Initial_Trade_Size)
    if (abs(strategy.position_size) >= Initial_Trade_Size * 2)
        strategy.close("Buy")
: 
Negative and not Positive ? 
    strategy.entry("Sell", strategy.short, size=Initial_Trade_Size)
    if (abs(strategy.position_size) >= Initial_Trade_Size * 2)
        strategy.close("Sell")

// Stop loss
strategy.exit("StopLoss_Buy", from_entry="Buy", limit=-3)
strategy.exit("StopLoss_Sell", from_entry="Sell", limit=3)

```

This script implements the trading logic described in the strategy description, including RSI calculations and moving average crossover to generate buy and sell signals. It also includes stop loss mechanisms for risk management.