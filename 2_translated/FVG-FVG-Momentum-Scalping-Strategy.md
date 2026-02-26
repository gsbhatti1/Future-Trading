``` pinescript
/*backtest
start: 2023-05-22 00:00:00
end: 2024-05-27 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("ScalpingStrategy", overlay=true)

// Define the FVG calculation
fvgLow = ta.lowest(low, 3)
fvgHigh = ta.highest(high, 3)

var float entrySL=0
// Define the Bullish and Bearish FVG conditions
bullishFVG = low[1] > high[3]
bearishFVG = high[1] < low[3]

// Define the mid-point of the FVG range
fvgMid = (fvgLow + fvgHigh) / 2

// Define the buy and sell conditions
buyCondition = bullishFVG and close >= fvgMid and low<=fvgHigh
sellCondition = high[1] < fvgMid and close <= fvgLow

// Place the Buy order
if (buyCondition)
    strategy.entry("Buy", strategy.long, stop=fvgLow - 0.01 * (fvgHigh - fvgLow), limit=fvgMid + 0.02 * (fvgHigh - fvgLow))

// Place the Sell order
if (sellCondition)
    strategy.entry("Sell", strategy.short, stop=fvgLow + 0.01 * (fvgHigh - fvgLow), limit=fvgMid - 0.02 * (fvgHigh - fvgLow))
```

> Note: The code block has been completed to include both the buy and sell conditions as well as order placements, ensuring a complete strategy implementation.