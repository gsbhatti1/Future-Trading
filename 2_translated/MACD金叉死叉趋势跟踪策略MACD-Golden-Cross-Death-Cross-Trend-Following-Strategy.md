> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|12|Fast Length|
|v_input_2|26|Slow Length|
|v_input_3_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_4|9|Signal Smoothing|
|v_input_5|false|Simple MA(Oscillator)|
|v_input_6|false|Simple MA(Signal Line)|
|v_input_7|0|Choose your signal: Continuation|Reversal|Histogram|MACD Line ZC|Signal Line ZC|
|v_input_8|false|JPY Pair ?|
|v_input_9|3|How many years of testing ?|


> Source (PineScript)

```pinescript
//@version=5
indicator("MACD Golden Cross Death Cross Trend Following Strategy", shorttitle="MACD-GCDCTFS", overlay=true)

// Inputs
fastLength = input(12, title="Fast Length")
slowLength = input(26, title="Slow Length")
src = input(close, title="Source")
signalSmoothing = input(9, title="Signal Smoothing")
oscillatorSma = input(false, title="Simple MA (Oscillator)")
signalLineSma = input(false, title="Simple MA (Signal Line)")
signalType = input(0, title="Choose your signal: Continuation|Reversal|Histogram|MACD Line ZC|Signal Line ZC")
isJpyPair = input(false, title="JPY Pair?")
testYears = input(3, title="How many years of testing?")

// MACD Calculation
[macdLine, signalLine, _] = macd(src, fastLength, slowLength, signalSmoothing)

// Stop Loss and Take Profit using ATR
atrPeriod = 14
atrValue = ta.atr(atrPeriod)
stopLoss = atrValue * 2

// Signal Types
continuationSignal = (signalType == 1)
reversalSignal = (signalType == 2)
histogramSignal = (signalType == 3)
macdZcSignal = (signalType == 4)
signalLineZcSignal = (signalType == 5)

// Logic for Entry and Exit
if isJpyPair
    // Adjust logic for JPY pairs if necessary
else
    longCondition = crossover(macdLine, signalLine) and not continuationSignal and not reversalSignal and not histogramSignal and not macdZcSignal and not signalLineZcSignal
    shortCondition = crossunder(macdLine, signalLine) and not continuationSignal and not reversalSignal and not histogramSignal and not macdZcSignal and not signalLineZcSignal

    strategy.entry("Long", strategy.long, when=longCondition)
    strategy.exit("Take Profit/Stop Loss", "Long", stop=stopLoss, limit=(src + atrValue))
    strategy.close("Long", when=crossover(macdLine, signalLine))

    strategy.entry("Short", strategy.short, when=shortCondition)
    strategy.exit("Take Profit/Stop Loss", "Short", stop=stopLoss, limit=(src - atrValue))
    strategy.close("Short", when=crossunder(macdLine, signalLine))

// Plotting
plot(macdLine, title="MACD Line")
plot(signalLine, title="Signal Line")
hline(0, "Zero Line")

// Testing
if (testYears > 0)
    // Backtesting logic can be added here
```
```