``` pinescript
/*backtest
start: 2024-04-23 00:00:00
end: 2024-05-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("BNM INTRADAY SETUP MACD 3M - Version 1.2", shorttitle="Zero Lag MACD Enhanced 1.2")
source = close

fastLength = input(12, title="Fast MM period", minval=1)
slowLength = input(26, title="Slow MM period", minval=1)
signalLength = input(9, title="Signal MM period", minval=1)
useEma = input(true, title="Use EMA (otherwise SMA)")
useOldAlgo = input(false, title="Use Glaz algo (otherwise 'real' original zero lag)")
showDots = input(true, title="Show symbols to indicate crossing")
dotsDistance = input(1.5, title="Symbols distance factor", minval=0.1)

// Fast line
ma1 = useEma ? ema(source, fastLength) : sma(source, fastLength)
// Slow line
ma2 = useEma ? ema(source, slowLength) : sma(source, slowLength)
// Zero-lag fast and slow lines
zemaFast = useOldAlgo ? glaz(ma1, fastLength) : zema(ma1, fastLength)
zemaSlow = useOldAlgo ? glaz(ma2, slowLength) : zema(ma2, slowLength)

// MACD line
macdLine = zemaFast - zemaSlow

// Signal line
signalLine = ema(macdLine, signalLength)

// MACD histogram
histogramValue = macdLine - signalLine

// Buy and sell signals
buySignal = crossover(macdLine, signalLine) and macdLine < 0
sellSignal = crossunder(macdLine, signalLine) and macdLine > 0

// Plotting
plot(macdLine, color=blue, title="MACD Line")
plot(signalLine, color=red, title="Signal Line")
hline(0, "Zero Line", color=black)

// Dots for signals
if (showDots)
    label.new(x=bar_index, y=high * 1.5, text="蓝色表示买入信号", color=color.blue, style=label.style_label_down)
    label.new(x=bar_index, y=low * 0.5, text="红色表示卖出信号", color=color.red, style=label.style_label_up)

// Alerts
alertcondition(buySignal, title="Buy Signal Alert", message="Buy Signal Generated")
alertcondition(sellSignal, title="Sell Signal Alert", message="Sell Signal Generated")

// Strategy execution
if (buySignal)
    strategy.entry("Buy", strategy.long)
if (sellSignal)
    strategy.exit("Sell", "Buy")
```

This Pine Script code implements the described MACD dual crossover zero-lag trading strategy. It calculates the fast and slow moving averages, applies a zero-lag algorithm to reduce delay, generates buy/sell signals based on crossovers, and includes plotting functions for visualization and alerts for timely trading opportunities.