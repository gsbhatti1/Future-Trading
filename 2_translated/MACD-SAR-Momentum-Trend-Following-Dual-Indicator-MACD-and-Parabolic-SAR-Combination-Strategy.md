``` pinescript
/*backtest
start: 2024-02-21 00:00:00
end: 2024-11-25 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("MACD + Parabolic SAR Strategy", shorttitle="MACD+SAR", overlay=true)

//========== User Inputs ==========//
// MACD parameters
fastLength   = input.int(12, "MACD Fast Length")
slowLength   = input.int(26, "MACD Slow Length")
signalLength = input.int(9,  "MACD Signal Length")

// SAR parameters (start, step, maximum)
afStart     = input.float(0.02, "SAR Start")
afIncrement = input.float(0.02, "SAR Increment")
afMax       = input.float(0.2,  "SAR Max")

//========== MACD Calculation ==========//
[macdLine, signalLine, histLine] = ta.macd(close, fastLength, slowLength, signalLength)

//========== SAR Calculation ==========//
sar = ta.sar(high, low, afStart, afIncrement, afMax)

//========== Entry Rules ==========//
longCondition  = macdLine > signalLine and close > sar
shortCondition = macdLine < signalLine and close < sar

//========== Exit Rules ==========//
isLongPosition = strategy.position_size >= 0
isShortPosition = strategy.position_size <= 0

exitLongCondition = not longCondition or isShortPosition
exitShortCondition = not shortCondition or isLongPosition

//========== Strategy Execution ==========//
when exitLongCondition
    strategy.close("Long")

when exitShortCondition
    strategy.close("Short")
```

This Pine Script implementation translates the provided Chinese text into English while maintaining the original code blocks and formatting.