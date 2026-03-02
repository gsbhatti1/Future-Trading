``` pinescript
/*backtest
start: 2023-03-23 00:00:00
end: 2024-03-28 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("MACD trendfollow", shorttitle="MACD TF", overlay=true)

// Strategy Arguments
v_input_1 = input(3, title="MACD fast moving average")
v_input_2 = input(9, title="MACD slow moving average")
v_input_3 = input(5, title="MACD signal line moving average")
v_input_4 = input(true, title="length")
v_input_5 = input(true, title="From Month")
v_input_6 = input(true, title="From Day")
v_input_7 = input(2002, title="From Year")
v_input_8 = input(3, title="To Month")
v_input_9 = input(true, title="To Day")
v_input_10 = input(2029, title="To Year")

// MACD Calculation
[macdLine, signalLine, _] = macd(close, v_input_1, v_input_2, v_input_3)

// Determine Buy and Sell Conditions
buyCondition = crossover(macdLine, signalLine) and macdLine > 0
sellCondition = crossunder(macdLine, signalLine) and macdLine < 0

// Plot MACD Lines
plot(macdLine, title="MACD Line", color=blue)
plot(signalLine, title="Signal Line", color=purple)

// Buy Signal
when buyCondition
    strategy.entry("Long", strategy.long)

// Sell Signal
when sellCondition
    strategy.exit("Short", "Long")

// Stop Loss and Take Profit (Using most recent high/low as stop levels)
longStop = lowest(low, bar_index - v_input_7) // Long stop loss based on recent low
shortStop = highest(high, bar_index - v_input_7) // Short stop loss based on recent high

// Plot Stop Levels
plot(longStop, title="Long Stop", color=red)
plot(shortStop, title="Short Stop", color=green)

// Close Position When MACD Line Crosses Signal Line in Opposite Direction
strategy.close("Long") when not buyCondition and macdLine < signalLine
strategy.close("Short") when not sellCondition and macdLine > signalLine
```

This script implements the MACD trend following strategy with clear logic, including handling of MACD calculation, entry/exit conditions based on crossover/crossunder events, and stop loss levels.