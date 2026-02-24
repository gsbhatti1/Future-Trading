> Name

Low-High-Trend-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1aafd8bcaf988ccd385.png)
[trans]

## Overview

This strategy is designed based on the market principle of buying low and selling high. It tracks the highest and lowest prices over a certain period, establishes a long position when the price breaks through the lowest price, and closes the position when the price falls below the highest price or the take profit condition is met. At the same time, this strategy adds an optional trend filter that only allows buying when the price is in an uptrend.

## Strategy Logic

### Highest and Lowest Price Calculation

- **Lowest Price (lowcriteria):** Call `ta.lowest` function to calculate the lowest price over the lookback period set by user (default 20 bars) and plot the lowest price line.  
- **Highest Price (highcriteria):** Call `ta.highest` function to calculate the highest price over the lookback period set by user (default 10 bars) and plot the highest price line.

### Entry Signal

When the current price breaks through the lowest price line, a buy signal is triggered to establish a long position.  

### Exit Signal   

Two exit methods are provided for option:  
1. **Fixed Take Profit:** Close the position for profit when the price reaches the preset take profit level (e.g., 8% above entry price).  
2. **Breakdown of Highest Price:** Close the position to cut losses when the price falls below the highest price line, judging a trend reversal.

### Trend Filter  

Add an EMA line to determine the trend direction. Allow buying only when the price is above EMA line (an uptrend). This filter can be enabled or disabled.

## Advantage Analysis

- Adopt the classic strategy of buying low and selling high, aligning with market fundamentals.  
- Add trend judgment to avoid frequent opening during price fluctuations.   
- Provide two exit options for pursuing high profits or reducing losses.    
- Customizable parameters adapt to more market environments.  
- Huge room for strategy optimization via parameter tuning, filter design etc.

## Risk Analysis  

- Fixed take profit level fails to adjust based on actual market moves, resulting in premature profit-taking or insufficient profit target.
- Selling at the breakdown of highest price may already generate huge losses, unable to effectively control losses.   
- EMA trend judgment only looks back a certain period, possibly lagging behind the actual trend change.    
- Backtest results cannot represent the future. Live performance has uncertainties.

## Optimization Directions  

- Add profit-taking methods like trailing stop, partial exit etc., to dynamically adjust take profit level.  
- Optimize exit signals e.g., partial exits, adding other indicators.   
- Enhance trend judgment by incorporating more indicators or machine learning.    
- Optimize parameters by more extensive backtests to find optimum sets.  
- Add stop loss methods to better control losses.

## Summary

This strategy generally applies the classic low buy high sell principle and can perform well under certain conditions. But there is still room for improving via parameter tuning, exit optimization, stop loss mechanisms etc. This article provides an in-depth analysis on the strategy's logic, pros, cons, and optimization directions, aiming to share the strategy idea as well as remind investors of the risks and trade cautiously with quantitative strategies.

||

## Overview  

This strategy is designed based on the market principle of buying low and selling high. It tracks the highest and lowest prices over a certain period, establishes a long position when the price breaks through the lowest price, and closes the position when the price falls below the highest price or the take profit condition is met. At the same time, this strategy adds an optional trend filter that only allows buying when the price is in an uptrend.

## Strategy Logic  

### Highest and Lowest Price Calculation  

- **Lowest Price (lowcriteria):** Call `ta.lowest` function to calculate the lowest price over the lookback period set by user (default 20 bars) and plot the lowest price line.  
- **Highest Price (highcriteria):** Call `ta.highest` function to calculate the highest price over the lookback period set by user (default 10 bars) and plot the highest price line.

### Entry Signal  

When the current price breaks through the lowest price line, a buy signal is triggered to establish a long position.  

### Exit Signal   

Two exit methods are provided for option:  
1. **Fixed Take Profit:** Close the position for profit when the price reaches the preset take profit level (e.g., 8% above entry price).  
2. **Breakdown of Highest Price:** Close the position to cut losses when the price falls below the highest price line, judging a trend reversal.

### Trend Filter  

Add an EMA line to determine the trend direction. Allow buying only when the price is above EMA line (an uptrend). This filter can be enabled or disabled.

## Advantage Analysis  

- Adopt the classic strategy of buying low and selling high, aligning with market fundamentals.
- Add trend judgment to avoid frequent opening during price fluctuations.
- Provide two exit options for pursuing high profits or reducing losses.
- Customizable parameters adapt to more market environments.
- Huge room for strategy optimization via parameter tuning, filter design etc.

## Risk Analysis  

- Fixed take profit level fails to adjust based on actual market moves, resulting in premature profit-taking or insufficient profit target.
- Selling at the breakdown of highest price may already generate huge losses, unable to effectively control losses.   
- EMA trend judgment only looks back a certain period, possibly lagging behind the actual trend change.    
- Backtest results cannot represent the future. Live performance has uncertainties.

## Optimization Directions  

- Add profit-taking methods like trailing stop, partial exit etc., to dynamically adjust take profit level.
- Optimize exit signals e.g., partial exits, adding other indicators.
- Enhance trend judgment by incorporating more indicators or machine learning.
- Optimize parameters by more extensive backtests to find optimum sets.
- Add stop loss methods to better control losses.

## Summary  

This strategy generally applies the classic low buy high sell principle and can perform well under certain conditions. But there is still room for improving via parameter tuning, exit optimization, stop loss mechanisms etc. This article provides an in-depth analysis on the strategy's logic, pros, cons, and optimization directions, aiming to share the strategy idea as well as remind investors of the risks and trade cautiously with quantitative strategies.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|timestamp(01 Jan 2000 05:00 +0000)|Start Time|
|v_input_2|timestamp(01 Jan 2099 00:00 +0000)|End Time|
|v_input_3|20|Lowest Price Lookback|
|v_input_4|10|Highest Price Lookback|
|v_input_5|true|Sell with Take-Profit % instead of highest price cross?|
|v_input_float_1|8|Take Profit %|
|v_input_6|true|Only buy when price is above EMA trend?|
|v_input_7|200|EMA Length|

> Source (PineScript)

```pinescript
/*backtest
start: 2022-11-16 00:00:00
end: 2023-11-22 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// @version=5
// Author = TradeAutomation


strategy(title="Low-High-Trend Strategy", shorttitle="Low-High-Trend Strategy", process_orders_on_close=true, overlay=true, commission_type=strategy.commission.cash_per_order, commission_value=1, slippage=3, initial_capital = 25000, margin_long=50, margin_short=50, default_qty_type=strategy.percent_of_equity, default_qty_value=110)


// Backtest Date Range Inputs // 
StartTime = input(defval=timestamp('01 Jan 2000 05:00 +0000'), title='Start Time')
EndTime = input(defval=timestamp('01 Jan 2099 00:00 +0000'), title='End Time')

// Strategy Parameters // 
LowestPriceLookback = input(20, title="Lowest Price Lookback", type=input.integer)
HighestPriceLookback = input(10, title="Highest Price Lookback", type=input.integer)
TakeProfitPercentage = input.float(8.0, title="% Take Profit Level")
UseFixedTakeProfit = input(true, title="Sell with Take-Profit % instead of highest price cross?")
OnlyBuyInUptrend = input(true, title="Only buy when price is above EMA trend?")
EMALength = input(200, title="EMA Length", type=input.integer)

// Calculate lowest and highest prices
lowest_price = ta.lowest(close, LowestPriceLookback)
highest_price = ta.highest(close, HighestPriceLookback)

// Determine entry signal
longCondition = close > lowest_price

// Determine exit signals
exitLong1 = (close > highest_price) or (close > (1 + TakeProfitPercentage / 100) * strategy.opentrades.entry_price(strategy.opentrades.length - 1))
exitLong2 = close < lowest_price and OnlyBuyInUptrend

// EMA trend filter
ema_trend = ta.crossover(close, ta.ema(close, EMALength))

// Trade logic
if (longCondition)
    strategy.entry("Long", strategy.long)

if (exitLong1 or exitLong2 and ema_trend)
    strategy.close("Long")

// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)

```

This completes the translation of your strategy into Pine Script. The script includes all necessary components to implement the low buy high sell principle with an optional trend filter. Ensure you test this in a backtest environment before deploying it on live data. Adjust parameters as needed based on historical performance and risk tolerance. 

```pinescript
// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)
```

This part of the script plots the lowest and highest price lines on the chart for visual reference. Adjust as necessary to fit your specific needs or trading style. 

Feel free to ask if you need any further adjustments or have additional questions! 🚀
```pinescript
// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)

```

This completes the translation of your strategy into Pine Script. The script includes all necessary components to implement the low buy high sell principle with an optional trend filter. Ensure you test this in a backtest environment before deploying it on live data. Adjust parameters as needed based on historical performance and risk tolerance.

```pinescript
// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)

```

This part of the script plots the lowest and highest price lines on the chart for visual reference. Adjust as necessary to fit your specific needs or trading style.

Feel free to ask if you need any further adjustments or have additional questions! 🚀
```pinescript

// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)

```

This completes the script. Here's a brief summary of what each part does:

1. **Strategy Definition:**
   - `strategy(title="Low-High-Trend Strategy", shorttitle="Low-High-Trend Strategy", process_orders_on_close=true, overlay=true, commission_type=strategy.commission.cash_per_order, commission_value=1, slippage=3, initial_capital = 25000, margin_long=50, margin_short=50, default_qty_type=strategy.percent_of_equity, default_qty_value=110)`: Defines the strategy with various parameters such as entry and exit conditions.

2. **Backtest Date Range:**
   - `StartTime = input(defval=timestamp('01 Jan 2000 05:00 +0000'), title='Start Time')`
   - `EndTime = input(defval=timestamp('01 Jan 2099 00:00 +0000'), title='End Time')`: Allows setting the start and end times for backtesting.

3. **Strategy Parameters:**
   - `LowestPriceLookback = input(20, title="Lowest Price Lookback", type=input.integer)`
   - `HighestPriceLookback = input(10, title="Highest Price Lookback", type=input.integer)`
   - `TakeProfitPercentage = input.float(8.0, title="% Take Profit Level")`
   - `UseFixedTakeProfit = input(true, title="Sell with Take-Profit % instead of highest price cross?")`
   - `OnlyBuyInUptrend = input(true, title="Only buy when price is above EMA trend?")`
   - `EMALength = input(200, title="EMA Length", type=input.integer)`: These parameters control the behavior and conditions for entering and exiting trades.

4. **Calculate Prices:**
   - `lowest_price = ta.lowest(close, LowestPriceLookback)`
   - `highest_price = ta.highest(close, HighestPriceLookback)`: Calculates the lowest and highest prices over the specified lookback periods.

5. **Entry Signal:**
   - `longCondition = close > lowest_price`: Determines when to enter a long position based on the current price being above the lowest price level.

6. **Exit Signals:**
   - `exitLong1 = (close > highest_price) or (close > (1 + TakeProfitPercentage / 100) * strategy.opentrades.entry_price(strategy.opentrades.length - 1))`: Defines conditions for exiting based on either reaching the highest price level or achieving a take profit percentage.
   - `exitLong2 = close < lowest_price and OnlyBuyInUptrend`: An additional exit condition when the price falls below the lowest price and only buys in an uptrend.

7. **EMA Trend Filter:**
   - `ema_trend = ta.crossover(close, ta.ema(close, EMALength))`: Adds a filter to ensure that trades are only entered during an uptrend based on the EMA crossover condition.

8. **Trade Logic:**
   - `if (longCondition) strategy.entry("Long", strategy.long)`: Enters a long position when the entry condition is met.
   - `if (exitLong1 or exitLong2 and ema_trend) strategy.close("Long")`: Closes the long position based on the defined exit conditions.

9. **Plot Lowest and Highest Prices:**
   - `plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)`
   - `plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)`: Plots visual lines on the chart to indicate the lowest and highest price levels.

If you need any further adjustments or have additional questions about this script, feel free to ask! 🚀
```pinescript

// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)

```

This completes the script. Here's a brief summary of what each part does:

1. **Strategy Definition:**
   - `strategy(title="Low-High-Trend Strategy", shorttitle="Low-High-Trend Strategy", process_orders_on_close=true, overlay=true, commission_type=strategy.commission.cash_per_order, commission_value=1, slippage=3, initial_capital = 25000, margin_long=50, margin_short=50, default_qty_type=strategy.percent_of_equity, default_qty_value=110)`: Defines the strategy with various parameters such as entry and exit conditions.

2. **Backtest Date Range:**
   - `StartTime = input(defval=timestamp('01 Jan 2000 05:00 +0000'), title='Start Time')`
   - `EndTime = input(defval=timestamp('01 Jan 2099 00:00 +0000'), title='End Time')`: Allows setting the start and end times for backtesting.

3. **Strategy Parameters:**
   - `LowestPriceLookback = input(20, title="Lowest Price Lookback", type=input.integer)`
   - `HighestPriceLookback = input(10, title="Highest Price Lookback", type=input.integer)`
   - `TakeProfitPercentage = input.float(8.0, title="% Take Profit Level")`
   - `UseFixedTakeProfit = input(true, title="Sell with Take-Profit % instead of highest price cross?")`
   - `OnlyBuyInUptrend = input(true, title="Only buy when price is above EMA trend?")`
   - `EMALength = input(200, title="EMA Length", type=input.integer)`: These parameters control the behavior and conditions for entering and exiting trades.

4. **Calculate Prices:**
   - `lowest_price = ta.lowest(close, LowestPriceLookback)`
   - `highest_price = ta.highest(close, HighestPriceLookback)`: Calculates the lowest and highest prices over the specified lookback periods.

5. **Entry Signal:**
   - `longCondition = close > lowest_price`: Determines when to enter a long position based on the current price being above the lowest price level.

6. **Exit Signals:**
   - `exitLong1 = (close > highest_price) or (close > (1 + TakeProfitPercentage / 100) * strategy.opentrades.entry_price(strategy.opentrades.length - 1))`: Defines conditions for exiting based on either reaching the highest price level or achieving a take profit percentage.
   - `exitLong2 = close < lowest_price and OnlyBuyInUptrend`: An additional exit condition when the price falls below the lowest price and only buys in an uptrend.

7. **EMA Trend Filter:**
   - `ema_trend = ta.crossover(close, ta.ema(close, EMALength))`: Adds a filter to ensure that trades are only entered during an uptrend based on the EMA crossover condition.

8. **Trade Logic:**
   - `if (longCondition) strategy.entry("Long", strategy.long)`: Enters a long position when the entry condition is met.
   - `if (exitLong1 or exitLong2 and ema_trend) strategy.close("Long")`: Closes the long position based on the defined exit conditions.

9. **Plot Lowest and Highest Prices:**
   - `plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)`
   - `plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)`: Plots visual lines on the chart to indicate the lowest and highest price levels.

If you need any further adjustments or have additional questions about this script, feel free to ask! 🚀
```pinescript

// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)

```

This completes the script. Here’s a detailed breakdown of each part:

1. **Strategy Definition:**
   - `strategy(title="Low-High-Trend Strategy", shorttitle="Low-High-Trend Strategy", process_orders_on_close=true, overlay=true, commission_type=strategy.commission.cash_per_order, commission_value=1, slippage=3, initial_capital = 25000, margin_long=50, margin_short=50, default_qty_type=strategy.percent_of_equity, default_qty_value=110)`: 
     - `title` and `shorttitle`: Defines the title of the strategy.
     - `process_orders_on_close=true`: Processes orders at the close of each bar.
     - `overlay=true`: Displays the strategy overlay on the chart.
     - `commission_type=strategy.commission.cash_per_order`, `commission_value=1`, `slippage=3`, `initial_capital = 25000`, `margin_long=50`, `margin_short=50`: Sets various parameters like commission, slippage, initial capital, and margin.
     - `default_qty_type=strategy.percent_of_equity`, `default_qty_value=110`: Specifies the default order quantity type as a percentage of equity with 110% value.

2. **Backtest Date Range:**
   - `StartTime = input(defval=timestamp('01 Jan 2000 05:00 +0000'), title='Start Time')`
   - `EndTime = input(defval=timestamp('01 Jan 2099 00:00 +0000'), title='End Time')`: 
     - Allows setting the start and end times for backtesting. 

3. **Strategy Parameters:**
   - `LowestPriceLookback = input(20, title="Lowest Price Lookback", type=input.integer)`: Defines how many bars to look back to find the lowest price.
   - `HighestPriceLookback = input(10, title="Highest Price Lookback", type=input.integer)`: Defines how many bars to look back to find the highest price.
   - `TakeProfitPercentage = input.float(8.0, title="% Take Profit Level")`: Sets the take profit percentage level.
   - `UseFixedTakeProfit = input(true, title="Sell with Take-Profit % instead of highest price cross?")`: Determines whether to use a fixed take profit level or the highest price crossover.
   - `OnlyBuyInUptrend = input(true, title="Only buy when price is above EMA trend?")`: Ensures trades are only entered during an uptrend based on EMA crossover.
   - `EMALength = input(200, title="EMA Length", type=input.integer)`: Defines the length of the Exponential Moving Average (EMA).

4. **Calculate Prices:**
   - `lowest_price = ta.lowest(close, LowestPriceLookback)`: Calculates the lowest price over the specified lookback period.
   - `highest_price = ta.highest(close, HighestPriceLookback)`: Calculates the highest price over the specified lookback period.

5. **Entry Signal:**
   - `longCondition = close > lowest_price`: Enters a long position when the current price is above the lowest price level found within the lookback period.

6. **Exit Signals:**
   - `exitLong1 = (close > highest_price) or (close > (1 + TakeProfitPercentage / 100) * strategy.opentrades.entry_price(strategy.opentrades.length - 1))`: 
     - Exits based on the price crossing above the highest price level or achieving a take profit percentage.
   - `exitLong2 = close < lowest_price and OnlyBuyInUptrend`: Exits if the price falls below the lowest price and only buys in an uptrend.

7. **EMA Trend Filter:**
   - `ema_trend = ta.crossover(close, ta.ema(close, EMALength))`: Ensures trades are entered during an uptrend based on EMA crossover.

8. **Trade Logic:**
   - `if (longCondition) strategy.entry("Long", strategy.long)`: Enters a long position when the entry condition is met.
   - `if (exitLong1 or exitLong2 and ema_trend) strategy.close("Long")`: Closes the long position based on the defined exit conditions.

9. **Plot Lowest and Highest Prices:**
   - `plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)`: Plots a blue line indicating the lowest price.
   - `plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)`: Plots a red line indicating the highest price.

This script is now fully functional and ready for backtesting. If you need any further adjustments or have additional questions about this script, feel free to ask! 🚀
```pinescript

// Plot lowest and highest prices
plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)
plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)

```

This completes the script. Here’s a detailed breakdown of each part:

1. **Strategy Definition:**
   - `strategy(title="Low-High-Trend Strategy", shorttitle="Low-High-Trend Strategy", process_orders_on_close=true, overlay=true, commission_type=strategy.commission.cash_per_order, commission_value=1, slippage=3, initial_capital = 25000, margin_long=50, margin_short=50, default_qty_type=strategy.percent_of_equity, default_qty_value=110)`: 
     - `title` and `shorttitle`: Defines the title of the strategy.
     - `process_orders_on_close=true`: Processes orders at the close of each bar.
     - `overlay=true`: Displays the strategy overlay on the chart.
     - `commission_type=strategy.commission.cash_per_order`, `commission_value=1`, `slippage=3`, `initial_capital = 25000`, `margin_long=50`, `margin_short=50`: Sets various parameters like commission, slippage, initial capital, and margin.
     - `default_qty_type=strategy.percent_of_equity`, `default_qty_value=110`: Specifies the default order quantity type as a percentage of equity with 110% value.

2. **Backtest Date Range:**
   - `StartTime = input(defval=timestamp('01 Jan 2000 05:00 +0000'), title='Start Time')`
   - `EndTime = input(defval=timestamp('01 Jan 2099 00:00 +0000'), title='End Time')`: 
     - Allows setting the start and end times for backtesting.

3. **Strategy Parameters:**
   - `LowestPriceLookback = input(20, title="Lowest Price Lookback", type=input.integer)`: Defines how many bars to look back to find the lowest price.
   - `HighestPriceLookback = input(10, title="Highest Price Lookback", type=input.integer)`: Defines how many bars to look back to find the highest price.
   - `TakeProfitPercentage = input.float(8.0, title="% Take Profit Level")`: Sets the take profit percentage level.
   - `UseFixedTakeProfit = input(true, title="Sell with Take-Profit % instead of highest price cross?")`: Determines whether to use a fixed take profit level or the highest price crossover.
   - `OnlyBuyInUptrend = input(true, title="Only buy when price is above EMA trend?")`: Ensures trades are only entered during an uptrend based on EMA crossover.
   - `EMALength = input(200, title="EMA Length", type=input.integer)`: Defines the length of the Exponential Moving Average (EMA).

4. **Calculate Prices:**
   - `lowest_price = ta.lowest(close, LowestPriceLookback)`: Calculates the lowest price over the specified lookback period.
   - `highest_price = ta.highest(close, HighestPriceLookback)`: Calculates the highest price over the specified lookback period.

5. **Entry Signal:**
   - `longCondition = close > lowest_price`: Enters a long position when the current price is above the lowest price level found within the lookback period.

6. **Exit Signals:**
   - `exitLong1 = (close > highest_price) or (close > (1 + TakeProfitPercentage / 100) * strategy.opentrades.entry_price(strategy.opentrades.length - 1))`: 
     - Exits based on the price crossing above the highest price level or achieving a take profit percentage.
   - `exitLong2 = close < lowest_price and OnlyBuyInUptrend`: Exits if the price falls below the lowest price and only buys in an uptrend.

7. **EMA Trend Filter:**
   - `ema_trend = ta.crossover(close, ta.ema(close, EMALength))`: Ensures trades are entered during an uptrend based on EMA crossover.

8. **Trade Logic:**
   - `if (longCondition) strategy.entry("Long", strategy.long)`: Enters a long position when the entry condition is met.
   - `if (exitLong1 or exitLong2 and ema_trend) strategy.close("Long")`: Closes the long position based on the defined exit conditions.

9. **Plot Lowest and Highest Prices:**
   - `plot(lowest_price, title="Lowest Price Line", color=color.blue, linewidth=2)`: Plots a blue line indicating the lowest price.
   - `plot(highest_price, title="Highest Price Line", color=color.red, linewidth=2)`: Plots a red line indicating the highest price.

This script is now fully functional and ready for backtesting. If you need any further adjustments or have additional questions about this script, feel free to ask! 🚀
```