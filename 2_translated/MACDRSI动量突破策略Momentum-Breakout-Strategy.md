> Name

MACDRSI Momentum-Breakout Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/164af44da89c7fc888d.png)
[trans]


## Overview

This is a strategy that uses MACD, RSI, and stochastic indicators to determine price momentum direction and makes long or short entries at momentum breakout points. By combining multiple indicators to judge the trend, it reduces the false signal rate of single indicators and can effectively capture medium-to-short-term trends in prices.

## Principle 

The strategy uses MACD, RSI, and stochastic indicators to determine the trend direction of prices. When MACD's DIFF line crosses above DEAL line, RSI is greater than 50, and STOCH's fast line is also greater than 50, it is judged as a bullish trend forming, so it will long at the next day's opening price with all capital at the highest price of the day; Conversely, when MACD's DIFF line crosses below DEAL line, RSI is less than 50, and STOCH's fast line is also less than 50, it is judged as a bearish trend forming, so it will short at the next day's opening price with all capital at the lowest price of the day. The take profit and stop loss are calculated based on the price fluctuation range of the past 7 days, and the profit/loss ratio can be customized.

After entering a position, if any of the three indicators generates a reverse signal, it means the trend has reversed and should exit the current position. It also sets special time condition filters that skip the entire month of March 2020 to avoid extreme market impact.

## Advantages

- Combining multiple indicators to judge the trend can effectively filter false signals
- Taking advantage of breakouts can capture the early stage of trends
- Using dynamic take profit and stop loss can lock in reasonable profits
- Skipping periods can prevent interference from extreme markets
- Combining trend following and reversal mechanisms can reduce unnecessary trades

## Risks

- Multiple indicator combos may cause lag, missing best entry timing
- Breakout signals are prone to being trapped
- Dynamic stops may be too aggressive and stopped out by Preis 
- Skipping special periods may miss opportunities if configured improperly
- Reversal signals may be too sensitive leading to over-trading

Improvement directions:

- Adjust indicator parameters to reduce lag
- Add filters like volume to avoid traps
- Use tracker stops to prevent Preis stops
- Optimize and test skipped date ranges 
- Tune reversal signal parameters to reduce frequency

## Summary

Overall, this is a typical trend-following strategy. It uses multiple indicators to determine trends for entries, and reversal signals to judge the end of trends for exits, combining both trend following and reversal mechanisms. However, the strategy itself also has some improper parameter settings and lag issues that need extensive backtesting to optimize and improve, in order to adjust all strategy parameters to their optimal state.

In summary, the logic of this strategy is clear, and the indicators used are typical. It performs well in some details of optimization and risk control, making it a practical quant trading strategy. However, there are still some gaps from perfection, requiring further testing and optimization to achieve professional-level return/drawdown ratios. With continuous optimization and updates, this strategy can become one worth tracking long-term.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Day|
|v_input_2|7|From Month|
|v_input_3|2019|From Year|
|v_input_4|true|To Day|
|v_input_5|true|To Month|
|v_input_6|2021|To Year|
|v_input_7|1.5|risk|
|v_input_8|3|reward|
|v_input_9|true|test long|
|v_input_10|true|test short|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-07 00:00:00
end: 2023-11-06 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=4
// Backtest the MACDRSI momentum breakout strategy.
strategy("MACDRSI Momentum Breakout Strategy", overlay=true, initial_capital=10000)

// ####################### Start of User Inputs #######################
// From Date Inputs
fromDay = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
fromMonth = input(defval = 7, title = "From Month", minval = 1, maxval = 12)
fromYear = input(defval = 2019, title = "From Year", minval = 1970)

// To Date Inputs
toDay = input(defval = 1, title = "To Day", minval = 1, maxval = 31)
toMonth = input(defval = 1, title = "To Month", minval = 1, maxval = 12)
toYear = input(defval = 2021, title = "To Year", minval = 1970)

// Calculate start/end date and time condition
startDate = timestamp(fromYear, fromMonth, fromDay, 0, 0)
endDate = timestamp(toYear, toMonth, toDay, 0, 0)

// MACD Settings
macdFastLength = input(12, title="MACD Fast Length")
macdSlowLength = input(26, title="MACD Slow Length")
macdSignalSmoothing = input(9, title="MACD Signal Smoothing")

// RSI Settings
rsiLength = input(14, title="RSI Length")
rsiOverbought = input(70, title="RSI Overbought Level")
rsiOversold = input(30, title="RSI Oversold Level")

// Stochastic Settings
stochKLength = input(5, title="Stochastic K Length")
stochDSmoothing = input(3, title="Stochastic D Smoothing")

// Calculate MACD, RSI, and Stochastic
[macdLine, signalLine, _] = macd(close, macdFastLength, macdSlowLength, macdSignalSmoothing)
rsiValue = rsi(close, rsiLength)
stochK, stochD = stochastic(close, high, low, stochKLength, stochDSmoothing)

// Entry Conditions
longCondition = crossover(macdLine, signalLine) and rsiValue > 50 and stochK > 50
shortCondition = crossunder(macdLine, signalLine) and rsiValue < 50 and stochK < 50

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit Conditions
exitCondition = or(
    inentry == false,
    macdLine < signalLine,
    rsiValue <= 50,
    stochK <= 50
)

if (exitCondition and isLong)
    strategy.close("Long")

if (exitCondition and isShort)
    strategy.close("Short")

// Set Take Profit and Stop Loss based on past 7 days' price range
takeProfit = input(1.5, title="Take Profit Ratio")
stopLoss = input(3, title="Stop Loss Ratio")

[high7, low7] = ta.hlc4(high, low, close, 7)
priceRange = high7 - low7

longTP = strategy.position_avg_price * (1 + takeProfit / 100) * priceRange
longSL = strategy.position_avg_price * (1 - stopLoss / 100) * priceRange

shortTP = strategy.position_avg_price * (1 - takeProfit / 100) * priceRange
shortSL = strategy.position_avg_price * (1 + stopLoss / 100) * priceRange

strategy.exit("Long Take Profit", "Long", limit=longTP, stop=longSL)
strategy.exit("Short Take Profit", "Short", limit=shortTP, stop=shortSL)

// Skip March 2020
if (time >= timestamp(2020, 3, 1, 0, 0) and time <= timestamp(2020, 3, 31, 23, 59))
    strategy.close_all()
```

This PineScript code implements the MACDRSI momentum breakout strategy with detailed explanations of its backtesting parameters and conditions.