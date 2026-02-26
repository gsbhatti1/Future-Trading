> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|RSI Length|
|v_input_2|20|Bollinger Bands Length|
|v_input_3|2|Bollinger Bands Multiplier|
|v_input_4|true|Stop Loss Percentage|
|v_input_5|2|Take Profit Percentage|
|v_input_6|14|Channels Length|
|v_input_7|2|Channels Multiplier|
|v_input_8|14|ATR Length|
|v_input_9|1.5|Threshold Percentage (%)|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-01-30 00:00:00
end: 2024-01-30 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Ichimoku Entries Strategy", overlay=true)

// Input parameters
rsiLength = input(14, title="RSI Length")
bbLength = input(20, title="Bollinger Bands Length")
bbMultiplier = input(2, title="Bollinger Bands Multiplier")
stopLossPct = input(1, title="Stop Loss Percentage")
takeProfitPct = input(2, title="Take Profit Percentage")

// Calculate Ichimoku Cloud components
tenkan = ta.sma(high + low, 9) / 2
kijun = ta.sma(high + low, 26) / 2
senkouA = (tenkan + kijun) / 2
senkouB = ta.sma(high + low, 52) / 2

// Bollinger Bands
basis = ta.sma(close, bbLength)
upperBB = basis + bbMultiplier * ta.stdev(close, bbLength)
lowerBB = basis - bbMultiplier * ta.stdev(close, bbLength)

// RSI
rsiValue = ta.rsi(close, rsiLength)

// Trade Proximity Oscillator (TPO) 
tppLength = input(14, title="Channels Length")
tppMultiplier = input(2, title="Channels Multiplier")
tppChannelA = ta.sma(high + low, tppLength) / 2
tppChannelB = ta.sma(high + low, 56) / 2

// Trading logic
longCondition = ta.crossover(tenkankijun, kijun) and close > upperBB and rsiValue < 70
shortCondition = ta.crossunder(tenkankijun, kijun) and close < lowerBB and rsiValue > 30

if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit logic
exitLongCondition = not longCondition and ta.crossover(close, upperBB)
exitShortCondition = not shortCondition and ta.crossunder(close, lowerBB)

if (exitLongCondition)
    strategy.exit("Profit/Stop Loss", "Long")

if (exitShortCondition)
    strategy.exit("Profit/Stop Loss", "Short")

// Stop loss and take profit
if (strategy.position_size > 0)
    stopLoss = close * (1 - stopLossPct / 100)
    takeProfit = close * (1 + takeProfitPct / 100)
    
    strategy.exit("Stop Loss", "Long", stop=stopLoss)
    strategy.exit("Take Profit", "Long", limit=takeProfit)

if (strategy.position_size < 0)
    stopLoss = close * (1 + stopLossPct / 100)
    takeProfit = close * (1 - takeProfitPct / 100)
    
    strategy.exit("Stop Loss", "Short", stop=stopLoss)
    strategy.exit("Take Profit", "Short", limit=takeProfit)

// Plotting Ichimoku Cloud and Bollinger Bands
plot(senkouA, title="Senkou Span A", color=color.blue, linewidth=2)
plot(senkouB, title="Senkou Span B", color=color.red, linewidth=2)
hline(70, "Overbought Level")
hline(30, "Oversold Level")
plot(basis, title="Bollinger Basis", color=color.gray, linewidth=1)
fill(senkouA, senkouB, color=color.new(color.blue, 95))
```

This PineScript code implements the Ichimoku Entries Strategy with the provided inputs and logic.