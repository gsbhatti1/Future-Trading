---
## Overview

This strategy designs an automated stop loss and take profit trading strategy based on the Relative Strength Index (RSI) indicator. When the RSI indicator crosses above the overbought line or below the oversold line, the strategy will open long or short positions respectively. At the same time, the strategy will automatically set the stop loss price and take profit price based on the opening price and the preset stop loss percentage and take profit percentage.

## Strategy Logic

This strategy uses the RSI indicator to determine overbought and oversold conditions in the market. When the RSI drops below the lower point (default 30), the market is considered oversold, and a long position is opened. When the RSI rises above the upper point (default 70), the market is considered overbought, and a short position is opened.

After opening long or short positions, the strategy automatically sets the stop loss price and take profit price based on the stop loss percentage (default 5%) and take profit percentage (default 10%). For example, after opening long, the stop loss price is set to `(1 - stop loss percentage) * entry price`, and the take profit price is set to `(1 + take profit percentage) * entry price`.

## Advantage Analysis

The biggest advantage of this strategy is that it can automatically set stop loss and take profit to mitigate trading risks. Stop loss helps limit losses, while take profit allows locking in profits. At the same time, RSI is a mature technical indicator that can effectively identify overbought or oversold conditions.

## Risk Analysis

This strategy also has some inherent risks. Incorrect signals from the RSI may lead to unnecessary losses. Additionally, triggering stop loss or take profit could result in partial profit loss. Carefully setting stop loss and take profit percentages is necessary—too loose may fail to control risks effectively, while too tight might cause unnecessary stops.

These risks can be mitigated by optimizing RSI parameters or adjusting the stop loss and take profit settings. Incorporating other indicators to confirm signals can also improve trading decisions' accuracy.

## Strategy Optimization

The strategy can be optimized in several aspects:

1. Optimize RSI parameters to find the best combination
2. Test different stop loss and take profit percentage settings  
3. Add other indicators to filter trading signals  
4. Incorporate trend determination rules to avoid false signals in ranging markets
5. Optimize entry timing, set up a trailing stop to lock in profits

## Conclusion

This strategy designs a simple and practical stop loss and take profit strategy based on the RSI indicator. The logic is clear and easy to implement, with automated stop loss and take profit to control risks. Attention should be given to optimizing parameters and rules to prevent risk associated with incorrect RSI signals. Overall, it provides a good idea for quantitative trading and is worth further research and optimization.

---

### Strategy Arguments

| Argument       | Default   | Description          |
| -------------- | --------- | -------------------- |
| `v_input_1`    | 14        | Length               |
| `v_input_2`    | 35        | OverSold             |
| `v_input_3`    | 65        | OverBought           |
| `v_input_4`    | 5         | Stop Loss (%)        |
| `v_input_5`    | 10        | Take Profit (%)      |

---

### Source (PineScript)

```pinescript
// backtest
// start: 2023-12-29 00:00:00
// end: 2024-01-28 00:00:00
// period: 1h
// basePeriod: 15m
// exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]

//@version=5
strategy("twelve12 first RSI remix", overlay=true)

length = input(14)
overSold = input(35)
overBought = input(65)
stopLossPercent = input(5, title="Stop Loss (%)") / 100
takeProfitPercent = input(10, title="Take Profit (%)") / 100

price = close

vrsi = ta.rsi(price, length)
co = ta.crossover(vrsi, overSold)
cu = ta.crossunder(vrsi, overBought)

if (not na(vrsi))
    if (co)
        strategy.entry("RsiLE", strategy.long, comment="RsiLE")
    if (cu)
        strategy.entry("RsiSE", strategy.short, comment="RsiSE")

// Calculate stop loss and take profit levels for long and short positions
longStopLoss = strategy.position_avg_price * (1 - stopLossPercent)
longTakeProfit = strategy.position_avg_price * (1 + takeProfitPercent)
shortStopLoss = strategy.position_avg_price * (1 + stopLossPercent)
shortTakeProfit = strategy.position_avg_price * (1 - takeProfitPercent)

// Set stop loss and take profit for long position
```

---

### Detail

https://www.fmz.com/strategy/440302

### Last Modified

2024-01-29 10:30:35