```pinescript
//@version=4
strategy(shorttitle="Dual-track Oscillator Pattern Strategy", title="Dual-track Oscillator Pattern Strategy", overlay=true)

length = input(20, "Length of Bollinger Bands", type=input.integer)
lengthEMA = input(9, "EMA Length", type=input.integer)
sourceClose = input(close, "Source: close", type=input.source)
sourceEMAClose = input(close, "EMA Source: close", type=input.source)
fromYear = input(2019, "From Year", type=input.int)
fromMonth = input(true, "From Month", type=input.bool)
fromDay = input(true, "From Day", type=input.bool)
toYear = input(9999, "To Year", type=input.int)
toMonth = input(12, "To Month", type=input.int)
toDay = input(31, "To Day", type=input.int)

// Calculate Bollinger Bands
bbands = ta.bbands(sourceClose, length, 2)
middle_band = bbands[0]
upper_band = bbands[1]
lower_band = bbands[2]

// Calculate EMA
ema9 = ta.ema(sourceEMAClose, lengthEMA)

// Buy and Sell Signals
if (close > ema9) and (close > middle_band)
    strategy.entry("Buy", strategy.long)

if (close < ema9) and (close < middle_band)
    strategy.close("Buy")

// Plot Bollinger Bands and EMA
plot(middle_band, color=color.gray)
plot(upper_band, color=color.red)
plot(lower_band, color=color.blue)
plot(ema9, color=color.green)
```

```