``` pinescript
/*backtest
start: 2020-05-04 00:00:00
end: 2022-05-03 23:59:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Bitfinex","currency":"BTC_USD"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © dannylimardi

//@version=4
strategy("Sentiment Oscillator with Backtest", "Sentiment Oscillator", overlay=false)

// Inputs
msLen = input(49, title="Market Sentiment Lookback Length", group="Parameters")
emaLen1 = input(40, title="Fast EMA Length", group="Parameters")
emaLen2 = input(204, title="Slow EMA Length", group="Parameters")
signalLen = input(20, title="Signal Length", group="Parameters")
showMs = input(false, title="Show Market Sentiment Line?", group="Plots")
showHist = input(true, title="Show Momentum Histogram?", group="Plots")
showMacd = input(true, title="Show MACD Line?", group="Plots")
showSignal = input(true, title="Show Signal Line?", group="Plots")
showDots = input(true, title="Plot Dots when MACD and Signal Line cross?", group="Plots")
showCpv = input(false, title="[Show Change/Volume of Each Bar?]", group="Plots")
showEma1 = input(false, title="[Show Fast EMA?]", group="Plots")
showEma2 = input(false, title="[Show Slow EMA?]", group="Plots")
longStrategy = input(true, title="Backtest Long Strategy?", group="Long Strategy")
entryVar1 = input(title="Long Entry Variable 1", defval="Histogram", options=["Market Sentiment", "Fast EMA", "Slow EMA", "MACD", "Signal Line", "Histogram"], group="Long Strategy")
entryCond = input(title="Long Entry Condition", defval="Crossing Over", options=["Crossing Over", "Crossing Under"], group="Long Strategy")
entryVar2 = input(title="Long Entry Variable 2", defval="Zero Line", options=["Market Sentiment", "Fast EMA", "Slow EMA", "MACD", "Signal Line", "Histogram", "Zero Line"], group="Long Strategy")
exitVar1 = input(title="Long Exit Variable 1", defval="MACD", options=["Market Sentiment", "Fast EMA", "Slow EMA", "MACD", "Signal Line", "Histogram"], group="Long Strategy")
exitCond = input(title="Long Exit Condition", defval="Crossing Under", options=["Crossing Over", "Crossing Under"], group="Long Strategy")
exitVar2 = input(title="Long Exit Variable 2", defval="Zero Line", options=["Market Sentiment", "Fast EMA", "Slow EMA", "MACD", "Signal Line", "Histogram", "Zero Line"], group="Long Strategy")
useCPV = input(false, title="Use Alternate Calculation Method?", group="Other Settings", tooltip="If checked, the Market Sentiment will be the EMA of Change Per Volume of each bar, instead of the default calculation method (Price Change EMA divided by Volume EMA). The alternate method may be slightly more responsive, but will result in bigger fluctuations when there is a huge change in volume. If this method is checked, I recommend changing the Long Exit Strategy to 'Signal Line Crossing Under Zero'.")
mcTheme = input(false, title="Use Alternate Color Scheme?", group="Other Settings", tooltip="If checked, the MACD, Signal, and Histogram will all be plotted as areas and histograms")

// Calculations
priceChange = close - close[1]
changePerVolume = (priceChange/volume) * 10000000  // (The 1000000 doesn't have any significance, it's just to avoid color-change errors when the values are too small.)
priceChangeEma = ema(priceChange, msLen)
volumeEma = ema(volume, msLen)
marketSentiment = useCPV ? ema(changePerVolume, msLen) : priceChangeEma/volumeEma * 1000000000
msEma1 = ema(marketSentiment, emaLen1)
msEma2 = ema(marketSentiment, emaLen2)
macd = msEma1 - msEma2
signal = ema(macd, signalLen)
hist = macd - signal

// Strategy Function and String Definitions
var entryVar1_ = 0.0
var entryVar2_ = 0.0
var exitVar1_ = 0.0
var exitVar2_ = 0.0

if entryVar1 == "Market Sentiment" 
    entryVar1_ := marketSentiment
else if entryVar1 == "Fast EMA"
    entryVar1_ := msEma1
else if entryVar1 =="Slow EMA"
    entryVar1_ := msEma2
else if entryVar1 == "MACD"
    entryVar1_ := macd
else if entryVar1 == "Signal Line" 
    entryVar1_ := signal
else if entryVar1 == "Histogram" 
    entryVar1_ := hist
    
if entryVar2 == "Market Sentiment" 
    entryVar2_ := marketSentiment
else if entryVar2 == "Fast EMA"
    entryVar2_ := msEma1
else if entryVar2 =="Slow EMA"
    entryVar2_ := msEma2
else if entryVar2 
```