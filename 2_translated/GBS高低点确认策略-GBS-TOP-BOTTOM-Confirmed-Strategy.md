> Name

GBS高低点确认策略-GBS-TOP-BOTTOM-Confirmed-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/da828c81711ada8e30.png)

[trans]
#### Overview
The GBS TOP BOTTOM Confirmed Strategy is a trading strategy designed to capture trading opportunities based on changes in price highs and lows. The strategy identifies specific high and low point patterns, entering long positions when highs are breached, and closing positions when lows are breached. The main idea behind this strategy is to utilize the fluctuation patterns of prices, opening positions at relatively high levels and closing positions at relatively low levels, to capture price difference profits.

#### Strategy Principles
The core of this strategy lies in identifying potential entry and exit points. The entry condition is met when the current high is lower than the previous high, and the previous high is higher than the high before it (high < high[1] and high[1] > high[2]). When this condition is satisfied, the entry high is marked, and a green line is drawn at that level. The buy condition is triggered when there is a recorded entry high (entryHigh), and the current high breaks above that level while the opening price is below the entry high.

The exit condition mirrors the entry condition. It occurs when the current low is higher than the previous low, and the previous low is lower than the low before it (low > low[1] and low[1] < low[2]). When this condition is met, the exit low is marked, and a red line is drawn at that level. The sell condition is triggered when there is a recorded exit low (exitLow), and the current low falls below that level while the opening price is above the exit low.

#### Strategy Advantages
1. The strategy is based on simple price high and low patterns, making it easy to understand and implement.
2. By opening positions at relatively high levels and closing positions at relatively low levels, the strategy aims to capture the middle portion of price fluctuations to obtain price difference profits.
3. The strategy employs visual plotting tools, such as small dots for entry and exit conditions and triangles for buy and sell signals, making the execution process more intuitive and clear.

#### Strategy Risks
1. The strategy relies on specific high and low point patterns, but not all such patterns lead to profitable opportunities, and false signals may occur.
2. The strategy lacks a clear stop-loss mechanism. If prices experience sharp changes after opening a position, it may result in significant losses.
3. The strategy does not consider trading costs and slippage, which can impact the overall performance of the strategy in real-world applications.

#### Strategy Optimization Directions
1. Incorporate appropriate stop-loss and take-profit mechanisms to control the risk exposure of individual trades.
2. Consider introducing other technical indicators or filtering conditions, such as trading volume and volatility, to improve signal reliability.
3. Optimize strategy parameters, such as adjusting the time window required for confirming highs and lows, to adapt to different market conditions.
4. Conduct thorough backtesting and forward testing before actual application, and make necessary adjustments based on the results.

#### Summary
The GBS TOP BOTTOM Confirmed Strategy is a trading strategy based on price high and low point patterns. It aims to capture price difference opportunities by identifying specific entry and exit conditions. The strategy's advantages lie in its simplicity and intuitiveness, but it also carries potential risks, such as false signals and the lack of risk control measures. To further improve the strategy, one can consider introducing stop-loss and take-profit mechanisms, combining other technical indicators, and optimizing parameters. Comprehensive backtesting and forward testing are essential before actual application.

||

#### Overview
The GBS TOP BOTTOM Confirmed Strategy is a trading strategy that aims to capture trading opportunities based on changes in price highs and lows. The strategy identifies specific high and low point patterns, entering long positions when highs are breached, and closing positions when lows are breached. The main idea behind this strategy is to utilize the fluctuation patterns of prices, opening positions at relatively high levels and closing positions at relatively low levels, in order to capture price difference profits.

#### Strategy Principles
The core of this strategy is to identify potential entry and exit points. The entry condition is met when the current high is lower than the previous high, and the previous high is higher than the high before it (high < high[1] and high[1] > high[2]). When this condition is satisfied, the entry high is marked, and a green line is drawn at that level. The buy condition is triggered when there is a recorded entry high (entryHigh), and the current high breaks above that level while the opening price is below the entry high.

The exit condition is similar to the entry condition. It occurs when the current low is higher than the previous low, and the previous low is lower than the low before it (low > low[1] and low[1] < low[2]). When this condition is met, the exit low is marked, and a red line is drawn at that level. The sell condition is triggered when there is a recorded exit low (exitLow), and the current low falls below that level while the opening price is above the exit low.

#### Strategy Advantages
1. The strategy is based on simple price high and low patterns, making it easy to understand and implement.
2. By opening positions at relatively high levels and closing positions at relatively low levels, the strategy attempts to capture the middle portion of price fluctuations to obtain price difference profits.
3. The strategy employs visual plotting tools, such as small dots for entry and exit conditions and triangles for buy and sell signals, making the execution process more intuitive and clear.

#### Strategy Risks
1. The strategy relies on specific high and low point patterns, but not all such patterns lead to profitable opportunities, and false signals may occur.
2. The strategy lacks a clear stop-loss mechanism. If prices experience sharp changes after opening a position, it may result in significant losses.
3. The strategy does not consider trading costs and slippage, which can impact the overall performance of the strategy in real-world applications.

#### Strategy Optimization Directions
1. Incorporate appropriate stop-loss and take-profit mechanisms to control the risk exposure of individual trades.
2. Consider introducing other technical indicators or filtering conditions, such as trading volume and volatility, to improve signal reliability.
3. Optimize strategy parameters, such as adjusting the time window required for confirming highs and lows, to adapt to different market conditions.
4. Conduct thorough backtesting and forward testing before actual application, and make necessary adjustments based on the results.

#### Summary
The GBS TOP BOTTOM Confirmed Strategy is a trading strategy based on price high and low point patterns. It aims to capture price difference opportunities by identifying specific entry and exit conditions. The strategy's advantages lie in its simplicity and intuitiveness, but it also carries potential risks, such as false signals and the lack of risk control measures. To further improve the strategy, one can consider introducing stop-loss and take-profit mechanisms, combining other technical indicators, and optimizing parameters. Comprehensive backtesting and forward testing are essential before actual application.

||

> Source (PineScript)

```pinescript
//@version=5
strategy("GBS TOP BOTTOM Confirmed", overlay=true)

// Entry condition
var float entryHigh = na
var line entryLine = na
entryCondition = high < high[1] and high[1] > high[2]
if (entryCondition)
    entryHigh := high[1]

// Buy condition based on nearest entry
buyCondition = not na(entryHigh) and high > entryHigh and open < entryHigh

// Exit condition
var float exitLow = na
var line exitLine = na
exitCondition = low > low[1] and low[1] < low[2]
if (exitCondition)
    exitLow := low[1]

// Sell condition based on nearest exit
sellCondition = not na(exitLow) and low < exitLow and open > exitLow

// Plot entry and exit points
plotshape(series=buyCondition, location=location.belowbar, color=color.green, style=shape.labelup, text="Buy")
plotshape(series=sellCondition, location=location.abovebar, color=color.red, style=shape.labeldown, text="Sell")

// Optional: Plot lines for high and low points
// entryLine := line.new(bar_index - 1, entryHigh, bar_index + 10, entryHigh, color=color.green)
// exitLine := line.new(bar_index - 1, exitLow, bar_index + 10, exitLow, color=color.red)
```
[/trans]