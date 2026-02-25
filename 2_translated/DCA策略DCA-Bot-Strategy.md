> Name

DCA Strategy DCA-Bot-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]

## Overview

This is a backtesting strategy that uses the dollar cost averaging (DCA) principle for adding positions. It can add to the position based on preset price deviation percentages and pyramiding rules after an initial entry. The strategy also includes take profit strategies and trailing take profit functionality.

## Strategy Principle

The strategy first opens a long position at the closing price when it is above 0 within the backtest time window. This opening price is recorded as the base price, `bo_level`. If no safety orders (`so`) exist, it places all possible exit orders on the current candle based on the set price deviation percentage and pyramiding rules. Specifically, the safety order price is calculated based on the latest safety order price, `latest_so_level`, using the safety order step scale, `safe_order_step_scale`. This continues until the maximum number of safety orders, `max_safe_order`, is reached.

During the holding period, if the position size is greater than 0, a take profit level is calculated based on the base price and target take profit percentage. If trailing take profit is disabled, this fixed take profit level is used; otherwise, it updates the trailing take profit's highest price, `ttp_max`, based on the candle high to adjust the take profit level dynamically.

## Advantage Analysis

- Utilizes the DCA mechanism to average down the cost basis when prices drop, hedging against systemic risks.
  
- Supports customizable parameters for flexible configuration of entry rules and take profit strategies. Suitable for different assets and trading styles.

- Has built-in trailing take profit functionality that automatically adjusts the take profit level based on price action, avoiding premature take profit triggers.

- Flexible backtest parameter settings allow testing data from different timeframes to evaluate strategy performance.

- Can directly configure live bots using backtest results without additional coding.

## Risk Analysis

- DCA strategies can further increase positions and losses if markets continue to decline. Proper pyramiding rules need to be set.

- Fixed percentage take profit cannot adjust based on market volatility, potentially leading to premature or late exits. Trailing take profit should be enabled.

- Backtest overfitting risks; real-time performance may be affected by transaction costs and other factors. Risk assessment is necessary.

- System stability risks can cause failed executions. Monitoring is required.

## Optimization Directions

- Dynamically adjust price deviation based on the volatility of different assets to optimize pyramiding rules.

- Integrate volatility indicators to determine a more scientific take profit percentage.

- Set reasonable backtest timeframes based on specific asset trading sessions.

- Include stop loss mechanisms for significant losses.

- Employ machine learning algorithms to dynamically optimize parameters.

## Conclusion

Overall, this is a very practical DCA backtesting program. It supports extensive customization of entry and take profit rules. The built-in trailing take profit complements the fixed take profit well. Flexible backtest parameter settings allow testing different assets and timeframes. With proper parameter tuning, this strategy can yield excellent results by hedging systemic risks with DCA on high-opportunity assets. However, in live trading, attention should be paid to pyramiding and take profit risks, along with system stability. Further optimizations like dynamic parameters and stop loss mechanisms can make this a highly powerful DCA trading bot.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Price deviation to open safety orders (%)|
|v_input_2|true|Target Take Profit (%)|
|v_input_3|0.5|Trailing Take Profit (%) [0 = Disabled]|
|v_input_4|10|Base order size|
|v_input_5|20|Safe order size|
|v_input_6|2|Safety order volume scale|
|v_input_7|1.5|Safety order step scale|
|v_input_8|5|Maximum number of safety orders|
|v_input_9|true|Start month|
|v_input_10|true|Start day|
|v_input_11|2021|Start year|
|v_input_12|true|End month|
|v_input_13|true|End day|
|v_input_14|9999|End year|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-18 00:00:00
end: 2023-09-25 00:00:00
period: 15h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © rouxam

// Author: ChaoZhang
// Inspired by the original work of ericlin0122

//@version=4
strategy("Backtesting DCA Bot", overlay=true, pyramiding=99, process_orders_on_close=true, commission_type=strategy.commission.percent, commission_value=0.1)

// Strategy Inputs
price_deviation         = input(1.0, type=input.float, title='Price deviation to open safety orders (%)')
target_take_profit      = input(50.0, type=input.float, title='Target Take Profit (%)')
trailing_take_profit    = input(0.5, type=input.float, title='Trailing Take Profit (%) [0 = Disabled]')
base_order              = input(10.0, type=input.float, title='Base order size')
safe_order              = input(20.0, type=input.float, title='Safe order size')
volume_scale            = input(2.0, type=input.float, title='Safety order volume scale')
step_scale              = input(1.5, type=input.float, title='Safety order step scale')
max_safe_orders         = input(5.0, type=input.int, title='Maximum number of safety orders')
start_month             = input(true, type=input.bool, title='From Month')
start_day               = input(true, type=input.bool, title='From Day')
start_year              = input(2021, type=input.int, title='From Year')
end_month               = input(true, type=input.bool, title='To Month')
end_day                 = input(true, type=input.bool, title='To Day')
end_year                = input(9999, type=input.int, title='To Year')

// Strategy logic goes here
```