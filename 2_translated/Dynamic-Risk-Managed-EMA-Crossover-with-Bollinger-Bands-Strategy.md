``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-10-12 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Intraday Strategy with Risk-Reward 1:2, Bollinger Bands, and Stop Loss", overlay=true)

// Parameters
fastLength = input(9, title="Fast EMA Length")
slowLength = input(21, title="Slow EMA Length")
rsiLength = input(14, title="RSI Length")
overbought = input(70, title="RSI Overbought Level")
oversold = input(30, title="RSI Oversold Level")
minVolume = input(100000, title="Min Volume for Confirmation")
bbLength = input(20, title="Bollinger Bands Length")
bbStdDev = input.float(2.0, title="Bollinger Bands Standard Deviation")
stopLossPercent = input.float(1, title="Stop Loss (%)", minval=0.1) // Stop Loss %
riskRewardRatio = 2.0 // Fixed risk-reward ratio 1:2

// Indicators
fastEMA = ta.ema(close, fastLength)
slowEMA = ta.ema(close, slowLength)
rsiValue = ta.rsi(close, rsiLength)
bbUpper = ta.bband(close, bbLength, bbStdDev, 0)[0]
bbLower = ta.bband(close, bbLength, bbStdDev, 2)[0]

// Entry Conditions
longCondition = ta.crossover(fastEMA, slowEMA) and 
                rsiValue < oversold and 
                volume > minVolume and 
                close < bbLower
shortCondition = ta.crossunder(fastEMA, slowEMA) and 
                 rsiValue > overbought and 
                 volume > minVolume and 
                 close > bbUpper

// Trade Management
riskRewardAmount = strategy.equity / riskRewardRatio
stopLossPrice = na
if (longCondition)
    stopLossPrice := close - (close * (stopLossPercent / 100))
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit Long", "Long", stop=stopLossPrice, limit=bbUpper)

if (shortCondition)
    stopLossPrice := close + (close * (stopLossPercent / 100))
    strategy.entry("Short", strategy.short)
    strategy.exit("Exit Short", "Short", stop=stopLossPrice, limit=bbLower)
```

This Pine Script code defines an intraday trading strategy that incorporates EMA crossovers, RSI levels, volume confirmation, and Bollinger Bands to determine entry points. It also includes a fixed risk-reward ratio and percentage-based stop loss mechanism.