``` pinescript
/*backtest
start: 2023-10-24 00:00:00
end: 2023-11-23 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This is an Open source work. Please do acknowledge in case you want to reuse whole or part of this code.
// Please see the documentation to know the details about this.

//@version=5
strategy('Strategy:Reversal-Catcher', shorttitle="Reversal-Catcher", overlay=true , currency=currency.NONE, initial_capital=100000)

// Inputs
src = input(close, title="Source (close, high, low, open etc.")

BBlength = input.int(defval=20, minval=1,title="Bollinger Period Length, default 20")
BBmult = input.float(defval=1.5, minval=1.0, maxval=4, step=0.1, title="Bollinger Bands Standard Deviation, default is 1.5")

fastMovingAvg = input.int(defval=21, minval=5,title="Fast Exponential Moving Average, default 21", group = "Trends")
slowMovingAvg = input.int(defval=50, minval=8,title="Slow Exponential Moving Average, default 50", group = "Trends")

rsiLenght = input.int(defval=14, title="RSI Lenght, default 14", group = "Momentum")
overbought = input.int(defval=70, title="Overbought limit (RSI), default 70")
oversold = input.int(defval=30, title="Oversold limit (RSI), default 30")

tradeType = input.string("Both", title="(?Trade settings)Trade Type: Both|TrendFollowing|Reversal")
closeTime = input.int(1500, title="Close all trades, default is 3:00 PM, 1500 hours (integer)")
neverClosedMarkets = input.bool(false, title="Markets that never closed (Crypto, Forex, Commodity)")

// Bollinger Bands
bbands = ta.bbands(src, BBlength, BBmult)

// Exponential Moving Averages
emaFast = ta.ema(src, fastMovingAvg)
emaSlow = ta.ema(src, slowMovingAvg)

// RSI
rsiVal = ta.rsi(src, rsiLenght)

// Plot Bollinger Bands
plot(bbands[1][1], title="Bollinger Upper Band", color=color.blue, linewidth=2, style=plot.style_linebr)
plot(bbands[0][1], title="Bollinger Middle Band", color=color.gray, linewidth=1, style=plot.style_candle)
plot(bbands[-1][1], title="Bollinger Lower Band", color=color.red, linewidth=2, style=plot.style_linebr)

// Plot RSI
hline(overbought, "Overbought Level", color=color.red, linestyle=hline.style_dotted)
hline(oversold, "Oversold Level", color=color.green, linestyle=hline.style_dotted)
plot(rsiVal, title="RSI Value", color=rsiVal < oversold ? color.green : rsiVal > overbought ? color.red : na)

// Buy Condition
buyCondition = ta.crossover(emaFast, emaSlow) and bbands[1][1] < close and ta.rsi(close, rsiLenght) <= overbought

// Sell Condition
sellCondition = ta.crossunder(emaFast, emaSlow) and bbands[-1][1] > close and ta.rsi(close, rsiLenght) >= oversold

if (tradeType == "Reversal" or tradeType == "Both")
    if (buyCondition)
        strategy.entry("Buy", strategy.long)

    if (sellCondition)
        strategy.exit("Sell", "Buy")

// Close all trades at a specific time
timeOfTheDay = time - time[1]
if (timeOfTheDay >= closeTime and neverClosedMarkets == false)
    for i = 0 to strategy.opentrades.count - 1
        strategy.close(i)

```

This Pine Script implements the Reversal-Catcher strategy as described. It includes all necessary variables, conditions, and plotting logic in a concise manner.