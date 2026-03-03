``` pinescript
/*backtest
start: 2024-11-21 00:00:00
end: 2024-11-28 00:00:00
period: 15m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("XAUUSD STRATEGY 10MIN", overlay=true)

// Spread Adjustment (38-point spread)
spread = 38 * syminfo.mintick

// MACD Calculation
[macdLine, signalLine, _] = ta.macd(close, 12, 26, 9)
macdBuy = ta.crossover(macdLine, signalLine)
macdSell = ta.crossunder(macdLine, signalLine)

// RSI Calculation
rsi = ta.rsi(close, 14)
rsiOverbought = rsi > 65
rsiOversold = rsi < 35

// Bollinger Bands Calculation
basis = ta.sma(close, 20)
dev = 2 * ta.stdev(close, 20)
upperBand = basis + dev
lowerBand = basis - dev

// ATR Calculation for Volatility-Based Stop Loss and Take Profit
atr = ta.atr(14)
stopLoss = 3 * atr
takeProfit = 5 * atr

// Variables to track entry price and line
var line entryLine = na
var int tradeNumber = 0
var string tradeType = ""
var string tradeSignalComment = ""

// Buy Condition
buyCondition = (macdBuy or rsiOversold or close < lowerBand)

// Sell Condition
sellCondition = (macdSell or rsiOverbought or close > upperBand)

// Strategy Entry and Alerts
if (buyCondition and strategy.opentrades == 0)  // Open a new buy trade
```