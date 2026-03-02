> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|RSI Length|
|v_input_2|70|RSI Overbought Level|
|v_input_3|30|RSI Oversold Level|
|v_input_4|0.03|Trade Risk (3%)|
|v_input_5|true|Stop-Loss Distance in Pips|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("RSI and EMA Risk Management Strategy", overlay=true)

// Strategy parameters
rsiLength = input(14, "RSI Length")
rsiOverbought = input(70, "RSI Overbought Level")
rsiOversold = input(30, "RSI Oversold Level")

// RSI calculation
rsiValue = rsi(close, rsiLength)

// EMA parameters
ema20 = ema(close, 20)
ema50 = ema(close, 50)
ema200 = ema(close, 200)

// Trade risk per trade parameter
riskPerTrade = input(0.03, "Trade Risk (3%)")

// Stop-loss distance in pips (adjust according to your strategy)
stopLossPips = input(1, "Stop-Loss Distance in Pips")

// Calculate position size and stop-loss
calculatePositionSize(entryPrice, stopLossPips) =>
    stopLossPrice = entryPrice - stopLossPips * syminfo.mintick
    riskPerTradeValue = strategy.equity * riskPerTrade
    positionSize = riskPerTradeValue / (entryPrice - stopLossPrice)
    positionSize

// Entry conditions
longCondition = (rsiValue < rsiOversold) and (close > ema20 or close > ema50 or close > ema200)
if longCondition
    strategy.entry("Long", strategy.long, qty=1)

// Exit conditions
exitCondition = (rsiValue >
```