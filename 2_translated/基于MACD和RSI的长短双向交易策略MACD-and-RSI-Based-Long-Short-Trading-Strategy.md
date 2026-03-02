``` pinescript
/*backtest
start: 2023-09-08 00:00:00
end: 2023-10-08 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=3
// Revision:        290
// Author:          @Hugo_Moriceau
//study("Moriceau_Crypto_strategies_Long_short_indicator_thesis",overlay=true)

// Pyramide 10 order size 100, every tick

strategy("Moriceau_Crypto_strategies_Long_short_indicator",overlay=true)

// === GENERAL INPUTS ===

fast = 12, slow = 26
fastMA = ema(close, fast)
slowMA = ema(close, slow)

macd = fastMA - slowMA
signal = sma(macd, 9)
rsi = rsi(close,14)

dataB = macd < -0.1  and rsi<27 and fastMA < slowMA
// data1 = macd > 0.125  and rsi>81 and fastMA> slowMA
dataS = macd > 0.125 and rsi > 81 and fastMA > slowMA

tradeInvert     = input(defval = false, title = "Invert Trade Direction?")

// === LOGIC ===

// is fast ma above slow ma?
Achat = macd < -0.1  and rsi < 27 and fastMA < slowMA ? true : false
vente = macd > 0.125 and rsi > 81 and fastMA > slowMA ? true : false

// are we inverting our trade direction?
tradeDirection = vente ? Achat ? false : true : Achat ? true : false

// === Plot Setting ===

plot(fastMA,color=red)
plot(slowMA,color=blue)
barcolor(color=iff(fastMA > slowMA, yellow, na))
barcolor(color=iff(fastMA < slowMA, black, na))
//barcolor(color=iff(macd > 0.12*close , fuchsia, na))
//barcolor(color=iff(macd < -0.1*close , lime, na))
plotchar(dataB, char='B',color=black,size = size.auto,location = location.belowbar,transp= 0)  
plotchar(dataS, char='S',color=black,size = size.auto,location = location.abovebar,transp= 0)

//fast = plot(maFast, title = "FastMA", color = yellow, linewidth = 2, style = line, transp = 50)
//slow = plot(maSlow, title = "SlowMA", color = black, linewidth = 2, style = line, transp = 50)

// === BACKTEST RANGE ===
FromMonth = input(defval = 05, title = "From Month", minval = 1)
FromDay   = input(defval = 23, title = "From Day", minval = 1)
FromYear  = input(defval = 2021, title = "From Year", minval = 2017)
ToMonth   = input(defval = 5, title = "To Month", minval = 1)
ToDay     = input(defval = 25, title = "To Day", minval = 1)
ToYear    = input(defval = 2021, title = "To Year", minval = 2017)


// === STRATEGY RELATED INPUTS ===
// the risk management inputs
inpTakeProfit   = input(defval = 2500, title = "Take Profit", minval = 28)
inpStopLoss     = input(defval = 600, title = "Stop Loss", minval = 15)
inpTrailStop    = input(defval = 300, title = "Trailing Stop Loss", minval = 5)
inpTrailOffset  = input(defval = 50, title = "Trailing Stop Loss Offset", minval = 1)

// === RISK MANAGEMENT VALUE PREP ===

// if an input is less than 1, assuming not wanted so we assign 'na' value to disable it.

useTakeProfit   = inpTakeProfit > 0 ? inpTakeProfit : na
useStopLoss     = inpStopLoss > 0 ? inpStopLoss : na
useTrailStop    = inpTrailStop > 0 ? inpTrailStop : na
useTrailOffset  = inpTrailOffset > 0 ? inpTrailOffset : na

// === TRADING LOGIC ===

longCondition  = dataB and not tradeInvert
shortCondition = dataS and not tradeInvert

if (longCondition)
    strategy.entry("Long", strategy.long, when = Achat)

if (shortCondition) 
    strategy.entry("Short", strategy.short, when = vente)

// === EXIT LOGIC ===

for i = 0 to bar_index
    if (strategy.opens["Long"] and close > open + useTakeProfit)
        strategy.close("Long")
        
    if (strategy.holds["Long"] and close < open - useStopLoss) 
        strategy.close("Long")

    if (strategy.holds["Short"] and close < open - useTrailOffset)
        strategy.exit("Trailing Stop Loss", from_entry = "Short", limit = open + useTrailStop)

// === END OF STRATEGY ===
```

This script includes the necessary Pine Script to implement the described trading strategy using MACD and RSI indicators. The logic for entering long and short positions, as well as managing take profit, stop loss, and trailing stop loss, is included within the script.