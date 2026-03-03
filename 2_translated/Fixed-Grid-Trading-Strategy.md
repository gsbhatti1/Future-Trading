> Name

Fixed-Grid-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/15e6ec9ac09a36234c8.png)
[trans]


## Overview

This strategy adopts a fixed grid trading approach, setting an initial price and the distance between each layer. Based on this, it calculates 10 fixed buy and sell prices to implement a low-buy-high-sell grid trading strategy.

## Strategy Logic

The strategy first sets the starting price `sprice` and the grid distance percentage `gridpercent`. Then, it calculates 10 layers of buy and sell prices based on the starting price and percentage.

Buy price formula:

```
b1 = sprice - (sprice * p1)
b2 = sprice - (sprice * p2)
b3 = sprice - (sprice * p3)
...
```

Where `p1` to `p10` are percentages calculated layer by layer based on `gridpercent`.

Sell price formula:

```
s1 = b1 + (sprice * p1)
s2 = b2 + (sprice * p1)
s3 = b3 + (sprice * p1)
...
```

The buy condition triggers when the close price is lower than the corresponding buy price:

```pinescript
if (close < b1)
    strategy.entry("b1", strategy.long, when=(close < b1))
```

Similarly, the sell condition triggers when the close price is higher than the corresponding sell price:

```pinescript
if (close > s1)
    strategy.exit("b1", when=(close > s1))
```

This implements the low-buy-high-sell grid trading strategy.

## Advantages

The fixed grid strategy has the following advantages:

1. It achieves automatic low-buy-high-sell without timing the market, reducing trading difficulty.
2. Setting proper grid distance effectively controls risk and avoids chasing trends.
3. Profitable whether the market goes up or down.
4. Flexibility to adjust grid parameters for different market conditions.
5. Scaling up position size by adding more grid layers.
6. Incorporating stop loss orders can avoid significant losses during extreme market events.

## Risks

The strategy also has some risks:

1. Trading fees may erode profits during range-bound markets.
2. Improper starting price and grid settings can lead to losses.
3. Large price gaps may cause losses during extreme events.
4. Mechanical trading systems have the risk of order insertion.
5. Concentrated market events can amplify losses.

Solutions:

1. Optimize grid parameters to ensure profit exceeds fees.
2. Backtest to find optimal starting prices and grid distances.
3. Add stop loss orders to control risks.
4. Relax order prices to avoid order insertion.
5. Set risk controls to limit maximum losses.

## Enhancements

The strategy can be enhanced in the following ways:

1. Dynamically adjust grid distance based on volatility levels.
2. Calculate price ranges and dynamically set starting prices.
3. Incorporate machine learning models for predicting price movements and adjusting grids accordingly.
4. Optimize stop loss positions based on historical data.
5. Integrate position sizing strategies to optimize profit levels.
6. Enhance position management to maximize capital utilization.
7. Improve trade execution using algorithms like TWAP to reduce transaction costs.

## Conclusion

This strategy implements fixed grid trading by setting buy and sell prices based on the starting price and grid percentage, achieving automatic low-buy-high-sell operations. It's important to manage risks through optimizing parameters, dynamic adjustments, and stop losses for profit locking and loss control. Incorporating advanced machine learning and capital management techniques can further improve strategy profitability and win rates.

||
## Overview

This strategy adopts a fixed grid trading approach by setting the starting price and percentage between each grid layer. Then it calculates 10 fixed buy and sell prices based on the percentage to implement a low-buy-high-sell grid trading strategy.

## Strategy Logic

The strategy first sets the starting price `sprice` and the grid distance percentage `gridpercent`. Then, it calculates 10 layers of buy and sell prices based on the starting price and percentage. 

Buy price formula:

```pinescript
b1 = sprice - (sprice * p1)
b2 = sprice - (sprice * p2) 
b3 = sprice - (sprice * p3)
...
```

Where `p1` to `p10` are percentages calculated layer by layer based on `gridpercent`.

Sell price formula:  

```pinescript
s1 = b1 + (sprice * p1)
s2 = b2 + (sprice * p1) 
s3 = b3 + (sprice * p1)
...
```

The buy condition triggers when the close price is lower than the corresponding buy price:

```pinescript
if (close < b1)
    strategy.entry("b1", strategy.long, when=(close < b1))
```

Similarly, the sell condition triggers when the close price is higher than the corresponding sell price:

```pinescript
if (close > s1) 
    strategy.exit("b1", when=(close > s1)) 
```

This implements the low-buy-high-sell grid trading strategy.

## Strategy Arguments



| Argument | Default | Description |
| --- | --- | --- |
| `v_input_1` | 40500 | Starting price |
| `v_input_2` | true | Percent |

## Source (PineScript)

```pinescript
/*backtest
start: 2022-11-09 00:00:00
end: 2023-11-15 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Lionkind

//@version=5
strategy("Grid HW", overlay = true, margin_long = 1, margin_short = 1)

// Fix 35k price as starting point and 1% as a distance

sprice = input(40500, "Starting price")
gridpercent = input(1, "Percent")

// calculate the % of the 10 layers 

p1 = ((gridpercent * 1) / 100)
p2 = ((gridpercent * 2) / 100)
p3 = ((gridpercent * 3) / 100)
p4 = ((gridpercent * 4) / 100)
p5 = ((gridpercent * 5) / 100)
p6 = ((gridpercent * 6) / 100)
p7 = ((gridpercent * 7) / 100)
p8 = ((gridpercent * 8) / 100)
p9 = ((gridpercent * 9) / 100)
p10 = ((gridpercent * 10) / 100)

// set buy prices 

b1 = sprice - (sprice * p1)
b2 = sprice - (sprice * p2)
b3 = sprice - (sprice * p3)
b4 = sprice - (sprice * p4)
b5 = sprice - (sprice * p5)
b6 = sprice - (sprice * p6)
b7 = sprice - (sprice * p7)
b8 = sprice - (sprice * p8)
b9 = sprice - (sprice * p9)
b10 = sprice - (sprice * p10)

// set sell prices

s1 = b1 + (sprice * p1)
s2 = b2 + (sprice * p1)
s3 = b3 + (sprice * p1)
s4 = b4 + (sprice * p1)
s5 = b5 + (sprice * p1)
s6 = b6 + (sprice * p1)
s7 = b7 + (sprice * p1)
s8 = b8 + (sprice * p1)
s9 = b9 + (sprice * p1)
s10 = b10 + (sprice * p1)
```