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
// Backtest settings
strategy("MACD Golden Cross Death Cross Trend Following Strategy", shorttitle="MACD-GCDCTFS", overlay=false, pyramiding=0)

// Input arguments
fastLength = input(12, title="Fast Length")
slowLength = input(26, title="Slow Length")
source = input(close, title="Source")
signalSmoothing = input(9, title="Signal Smoothing")
oscillatorSMA = input(false, title="Simple MA(Oscillator)")
signalSMA = input(false, title="Simple MA(Signal Line)")
signalType = input(0, title="Choose your signal", options=["Continuation", "Reversal", "Histogram", "MACD Line ZC", "Signal Line ZC"])
isJPYPair = input(false, title="JPY Pair?")
testYears = input(3, title="How many years of testing?", minval=1)

// MACD Calculation
[macdLine, signalLine, _] = macd(source, fastLength, slowLength, signalSmoothing)
macdHistogram = macdh(macdLine, signalLine)

// Stop Loss and Take Profit using ATR
atrLength = input(14, title="ATR Length")
atrMultiplier = input(3.0, title="ATR Multiplier")
atrValue = atr(atrLength)
stopLossLevel = na
takeProfitLevel = na

if isJPYPair
    stopLossLevel := close * (1 - atrMultiplier / 100)
    takeProfitLevel := close * (1 + atrMultiplier / 100)
else
    stopLossLevel := close - atrValue * atrMultiplier
    takeProfitLevel := close + atrValue * atrMultiplier

// Entry Logic based on chosen signal type
var float entryPrice = na
if signalType == "Continuation" and crossover(macdLine, signalLine)
    strategy.entry("Golden Cross", strategy.long, when=crossover(macdLine, signalLine))
    entryPrice := close
elif signalType == "Reversal" and crossunder(macdLine, signalLine)
    strategy.entry("Death Cross", strategy.short, when=crossunder(macdLine, signalLine))
    entryPrice := close
elif signalType == "Histogram" and macdHistogram > 0
    strategy.entry("Golden Cross", strategy.long, when=macdHistogram > 0)
    entryPrice := close
elif signalType == "MACD Line ZC" and crossover(macdLine, 0)
    strategy.entry("Golden Cross", strategy.long, when=crossover(macdLine, 0))
    entryPrice := close
elif signalType == "Signal Line ZC" and crossunder(signalLine, 0)
    strategy.entry("Death Cross", strategy.short, when=crossunder(signalLine, 0))
    entryPrice := close

// Exit Logic based on stop loss/take profit levels
if not na(entryPrice) and barstate.islast
    if isJPYPair
        strategy.exit("Stop Loss/Profit", "Golden Cross", stop=stopLossLevel)
        strategy.exit("Stop Loss/Profit", "Death Cross", stop=takeProfitLevel)
    else
        strategy.exit("Stop Loss/Profit", "Golden Cross", stop=stopLossLevel, limit=takeProfitLevel)
        strategy.exit("Stop Loss/Profit", "Death Cross", stop=takeProfitLevel, limit=stopLossLevel)

// Plot ATR and MACD
plot(atrValue, title="ATR", color=color.blue)
hline(0, "Zero Line", color=color.black)
plot(macdLine, title="MACD Line", color=color.orange)
plot(signalLine, title="Signal Line", color=color.green)
```