``` pinescript
/*backtest
start: 2022-12-28 00:00:00
end: 2024-01-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Improved RSI Scalping Strategy", overlay=true)

// Parameters
rsiLength = input.int(14, title="RSI Length")
rsiOverbought = input.int(70, title="RSI Overbought Threshold")
rsiOversold = input.int(30, title="RSI Oversold Threshold")
takeProfitPips = input.int(10, title="Take Profit (Pips)")
stopLossPips = input.int(5, title="Stop Loss (Pips)")
riskPercentage = input.float(1, title="Risk Percentage", minval=0, maxval=100, step=0.1)

// Calculate RSI
rsiValue = ta.rsi(close, rsiLength)

// Custom AI Conditions
aiCondition1Long = ta.crossover(rsiValue, 50)
aiCondition1Short = ta.crossunder(rsiValue, 50)

// Add more AI conditions here
var aiCondition2Long = ta.crossover(rsiValue, 30)
var aiCondition2Short = ta.crossunder(rsiValue, 70)

// Combine AI conditions with RSI
longCondition = aiCondition1Long or aiCondition2Long or ta.crossover(rsiValue, rsiOversold)
shortCondition = aiCondition1Short or aiCondition2Short or ta.crossunder(rsiValue, rsiOverbought)

// Calculate position size based on risk percentage
equity = strategy.equity
riskAmount = (equity * riskPercentage) / 100
positionSize = riskAmount / (stopLossPips * syminfo.mintick)

// Calculate Take Profit and Stop Loss levels
takeProfitLevel = close + takeProfitPips * syminfo.mintick
stopLossLevel = close - stopLossPips * syminfo.mintick

// Long entry
strategy.entry("Long Entry", strategy.long, when=longCondition[1] and not longCondition, qty=1)
strategy.exit("Take Profit/Stop Loss", from_entry="Long Entry", limit=takeProfitLevel, stop=stopLossLevel)

// Short entry
strategy.entry("Short Entry", strategy.short, when=shortCondition[1] and not shortCondition, qty=1)
strategy.exit("Take Profit/Stop Loss", from_entry="Short Entry", limit=takeProfitLevel, stop=stopLossLevel)

```

This code defines the trading logic as described in the strategy. It includes parameters for RSI settings, take profit, stop loss, risk percentage, and custom AI conditions. The strategy entry and exit points are determined based on these inputs and executed accordingly.