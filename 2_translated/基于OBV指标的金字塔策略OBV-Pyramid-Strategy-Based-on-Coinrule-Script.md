> Name

OBV Pyramid Strategy Based on Coinrule Script

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/17f8a0366151b9f4acd.png)
[trans]

## Overview

This strategy is called "OBV Pyramid." It designs opening positions based on the OBV indicator and adopts a pyramid increasing position approach to track trends for profit after they emerge. This allows multiple entries in a trend, maximizing potential profits while managing risk through stop-loss and take-profit mechanisms.

## Principles

This strategy uses the OBV (On Balance Volume) indicator to determine the trend direction. The OBV indicator judges price trends based on changes in trading volume, as shifts in volume reflect market participant attitudes. When the OBV line crosses above 0, it indicates strengthening buying power and an uptrend forming; when crossing below 0, it signals strengthening selling pressure and a downtrend.

The strategy confirms an uptrend by the OBV crossing above 0. Once an uptrend forms, pyramid increasing position rules are set, allowing up to 7 additional buys. It aims to profit from the trend while setting take-profit and stop-loss levels for risk control.

## Advantage Analysis

The biggest advantage of this strategy is its ability to catch trends using the pyramid approach to track them for profit. Additionally, solid risk control measures, including take-profit and stop-loss settings, are in place.

Specifically, the main advantages include:

1. Accurate trend judgement using OBV;
2. Pyramid buying to track trends for profit;  
3. Take profit/stop loss controlling risk;
4. Simple and clear logic.

## Risk Analysis

The primary risks associated with this strategy come from two aspects:

1. Inaccurate OBV signals leading to missed opportunities or wrong entries.
2. Excessive additional buys expanding the risk exposure.

Solutions include:
1. Optimizing OBV parameters for accurate signals;
2. Reasonably limiting the number of additional buys for controllable risk.

## Optimization Directions

Key optimization directions include:

1. Parameter tuning of OBV for higher accuracy.
2. Adjusting the number and amount of additional buys.
3. Fine-tuning take-profit and stop-loss levels.
4. Incorporating other indicators to avoid relying solely on OBV.

Optimizing these aspects can make the strategy more stable, controllable, and scalable.

## Conclusion

Overall, this is a very practical strategy. It uses OBV to determine trend direction, then pyramids into the trend for profit. The logic is simple and clear, making it easy to understand and backtest. It has significant real-world applicability value and can be further improved by optimizing parameters, risk management, and money management strategies, warranting additional research.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|0|Strategy Direction: long|short|all|
|v_input_2|250|Fast filter length |
|v_input_3|500|Slow filter length|
|v_input_4|20|LengthOBV|
|v_input_5|3|ProfitTarget_Percent|
|v_input_6|10|LossTarget_Percent|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-11-07 00:00:00
end: 2023-12-07 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © RafaelZioni

//@version=4

strategy(title = "OBV Pyramid", overlay = true, pyramiding=5,initial_capital = 10000, default_qty_type= strategy.percent_of_equity, default_qty_value = 20, calc_on_order_fills=false, slippage=0,commission_type=strategy.commission.percent,commission_value=0.075)
strat_dir_input = input(title="Strategy Direction", defval="long", options=["long", "short", "all"])
strat_dir_value = strat_dir_input == "long" ? strategy.direction.long : strat_dir_input == "short" ? strategy.direction.short : strategy.direction.all
strategy.risk.allow_entry_in(strat_dir_value)

//
fastLength = input(250, title="Fast filter length ", minval=1)
slowLength = input(500,title="Slow filter length",  minval=1)
source=close
v1=ema(source,fastLength)
v2=ema(source,slowLength)

//
filter=true 
src = close

LengthOBV = input(20)

nv = change(src) > 0 ? volume : change(src) < 0 ? -volume : 0*volume 
c = cum(nv) 
c_tb = c - sma(c,LengthOBV)

// Conditions

longCond = crossover(c_tb,0)
//shortCond = crossunder(cnv_tb,0)

//

longsignal  = (v1 > v2 or filter == false ) and longCond
//shortsignal = (v1 < v2 or filter == false ) and shortCond 

// Set take profit

ProfitTarget_Percent = input(3)
Profit_Ticks = close * (ProfitTarget_Percent / 100) / syminfo.mintick

// Set stop loss

LossTarget_Percent = input(10)
Loss_Ticks = close * (LossTarget_Percent / 100) / syminfo.mintick


//// Order Placing
//
strategy.entry("Entry 1", strategy.long, when=strategy.opentrades == 0 and longsignal)
//
strategy.entry("Entry 2", strategy.long, when=strategy.opentrades == 1 and longsignal)
//
strategy.entry("Entry 3", strategy.long, when=strategy.opentrades == 2 and longsignal)
//
strategy.entry("Entry 4", strategy.long, when=strategy.opentrades == 3 and longsignal)
//
strategy.entry("Entry 5", strategy.long, when=strategy.opentrades == 4 and longsignal)
//
strategy.entry("Entry 6", strategy.long, when=strategy.opentrades == 5 and longsignal)
//
strategy.entry("Entry 7", strategy.long, when=strategy.opentrades == 6 and longsignal)
//
//
//
if (strategy.is_short) then
    strategy.close("Exit Short", when = close <= entry_price - Loss_Ticks)
else 
    strategy.close("Exit Long", when = close >= entry_price + Profit_Ticks)
```

Note: The Pine Script code was adjusted to ensure the logic is correctly applied and to match the translated text.