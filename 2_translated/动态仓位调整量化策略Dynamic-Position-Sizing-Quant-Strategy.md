---
## Overview

The core idea of this strategy is to dynamically adjust the position size of each trade based on account equity. It can automatically increase position size when profitable and decrease it when losing, thereby achieving the automatic leverage effect of compounding.

## Strategy Logic

The strategy achieves dynamic position sizing through the following key steps:

1. Set parameters like leverage ratio and max position size as constraints.
2. Calculate the benchmark position size by dividing account equity by the leverage ratio.
3. Compare the benchmark size with the max size setting, take the smaller one as the actual size.
4. Adjust the position size to the calculated actual size when opening positions.
5. Position size will change in real-time based on profit/loss amounts and changes in account equity.

The above steps ensure reasonable position sizing, avoid over-leverage risks while linking size to equity, achieving auto-compounding as profits increase.

## Advantages

The strategy has the following advantages:

1. Achieves dynamic position sizing without manual intervention.
2. Links position size to equity to achieve compounding effect automatically.
3. Sets leverage and max position size as risk limits.
4. Simple and clear logic, easy to understand and customize.
5. Easy to incorporate into other strategies, highly extensible.

## Risks

There are also some risks:

1. Magnified losses when position size increases, risk of missing reversals.
2. Frequent adjustments in extreme market conditions due to real-time linkage to equity.
3. Inappropriate max position size setting can lead to over-leverage.
4. Excessive leverage multiplying risks.

Risks can be mitigated through prudent parameter settings, capital buffering, etc.

## Enhancement Opportunities

The strategy can be enhanced in the following ways:

1. Add slippage to smooth adjustments.
2. Optimize the position sizing formula by incorporating other factors.
3. Statically lock sizes in specific market conditions.
4. Set a minimum step size for adjustments to avoid excessive changes.
5. Add conditional rules to prevent unnecessary adjustments.

The above enhancements can make the strategy behavior more stable and controllable, avoiding sensitivity and frequent position size changes.

## Conclusion

This strategy achieves equity-based dynamic position sizing to automatically magnify profits. It sets leverage and max position size as risk controls with simple and clear logic for ease of understanding and customization. We also analyzed its pros and cons and risks, along with some optimization suggestions. Overall, it provides a flexible and practical approach to achieve automated compound growth in trading.

---

## Strategy Arguments

| Argument | Default | Description |
| ---- | ---- | ---- |
| v_input_1 | 10000 | leverage |
| v_input_2 | 25 | max position size |

## Source (PineScript)

```pinescript
/* backtest
start: 2024-01-01 00:00:00
end: 2024-01-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of Tendies Heist LLC, 2021
//@version=4
strategy("Tendies Heist Auto Compounding Example", overlay=true)

leverage = input(10000)

maxps = input(25, "max position size")
strategy.risk.max_position_size(maxps)

balance = max(1,floor(strategy.equity / leverage))

o        = 1
ps       = true
size     = 0.
balance2 = size[1] < balance
balance3 = size[1] > balance
l        = balance3
w        = balance2

if ps
    size := w ? size[1]+o : l ? size[1]-o : nz(size[1],o)
if size > maxps
    size := maxps

longCondition = crossover(sma(close, 14), sma(close, 28))
if (longCondition)
    strategy.entry("My Long Entry Id", strategy.long, qty=size)

shortCondition = crossunder(sma(close, 14), sma(close, 28))
if (shortCondition)
    strategy.entry("My Short Entry Id", strategy.short, qty=size)
```

## Detail

https://www.fmz.com/strategy/442381

## Last Modified

2024-02-21 14:52:10