``` pinescript
/*backtest
start: 2022-10-30 00:00:00
end: 2023-11-05 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI Range Trading Strategy", overlay=true)

var rsiLength = input(2, title="rsi Length")
var float rsiBuyLevel = input(11, title="What rsi level triggers a long")
var float rsiShortLevel = input(91, title="What rsi level triggers a short")
var float maxRiskPerTrade = input(0.05, title="Maximum risk/ trade")
var float stopLossMovement = input(0.005, title="Max Movement in the opposite direction / trade")

var float longEntryPrice = na
var float shortEntryPrice = na

rsiValue = ta.rsi(close, rsiLength)

// Set max risk value based on equity and stop loss movement
maxRiskValue = (strategy.equity * maxRiskPerTrade) / stopLossMovement

// Conditions for entry and exit

if (close <= longEntryPrice - (longEntryPrice * stopLossMovement))
    strategy.close("Long")

if (close >= shortEntryPrice + (shortEntryPrice * stopLossMovement))
    strategy.close("Short")

if (rsiValue <= rsiBuyLevel)
    if (maxRsi == rsiShortLevel)
        maxRsi := rsiBuyLevel 
        strategy.close("Short")
        strategy.entry("Long", strategy.long)
        longEntryPrice := close
        
else if (rsiValue >= rsiShortLevel)
    if (maxRsi == rsiBuyLevel)
        maxRsi := rsiShortLevel
        strategy.close("Long")
        strategy.entry("Short", strategy.short)
        shortEntryPrice := close

```

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|2|rsi Length|
|v_input_2|11|What rsi level triggers a long|
|v_input_3|91|What rsi level triggers a short|
|v_input_4|0.05|Maximum risk/ trade|
|v_input_5|0.005|Max Movment in the opposite direction / trade|