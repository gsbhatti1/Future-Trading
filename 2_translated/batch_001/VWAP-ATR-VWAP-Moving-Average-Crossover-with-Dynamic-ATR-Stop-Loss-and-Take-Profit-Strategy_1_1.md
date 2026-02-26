``` pinescript
/*backtest
start: 2023-03-26 00:00:00
end: 2024-03-31 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("VWAP-Moving-Average-Crossover-with-Dynamic-ATR-Stop-Loss-and-Take-Profit-Strategy", overlay=true)

// Inputs
v_input_1 = input(40, "VWAP Period")
v_input_2 = input(14, "ATR Period")
v_input_3 = input(1.5, "ATR Multiplier for Stop Loss")
v_input_4 = input(3, "ATR Multiplier for Take Profit")

// Calculations for VWAP
typicalPrice = (high + low + close) / 3
typicalPriceVolume = typicalPrice * volume
cumulativeTypicalPriceVolume = ta.cum(typicalPriceVolume)
cumulativeVolume = ta.cum(volume)
vwapValue = cumulativeTypicalPriceVolume / cumulativeVolume

// Plot VWAP on the chart
plot(vwapValue, color=color.blue, title="VWAP")

// Entry Conditions based on price crossing over/under VWAP
longCondition = ta.crossover(close, vwapValue)
shortCondition = ta.crossunder(close, vwapValue)

// ATR Calculation for setting dynamic stop loss and take profit
atr = ta.atr(v_input_2)

// Execute Trades with Dynamic Stop Loss and Take Profit based on ATR
if (longCondition)
    strategy.entry("Long", strategy.long)
    stopLossLevel = close - (v_input_3 * atr)
    takeProfitLevel = close + (v_input_4 * atr)
    
    strategy.exit("Stop Loss Exit", "Long", stop=stopLossLevel)
    strategy.exit("Take Profit Exit", "Long", limit=takeProfitLevel)

if (shortCondition)
    strategy.entry("Short", strategy.short)
    stopLossLevel = close + (v_input_3 * atr)
    takeProfitLevel = close - (v_input_4 * atr)
    
    strategy.exit("Stop Loss Exit", "Short", stop=stopLossLevel)
    strategy.exit("Take Profit Exit", "Short", limit=takeProfitLevel)
```

This Pine Script code implements the described VWAP-Moving-Average-Crossover-with-Dynamic-ATR-Stop-Loss-and-Take-Profit-Strategy. The script calculates VWAP, sets dynamic stop loss and take profit levels based on ATR, and enters trades when price crosses over or under the VWAP.