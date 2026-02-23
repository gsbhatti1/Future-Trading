```pinescript
/*backtest
start: 2023-07-31 00:00:00
end: 2024-07-30 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI Buy Strategy with 30-day Cooldown", overlay=true)

// Parameter settings
rsiLength = 14
rsiOversold = 30
usdAmount = 1000
cooldownPeriod = 30 * 24 * 60  

// Calculate RSI
rsi = ta.rsi(close, rsiLength)

// Track last buy time
var int lastBuyTime = 0
var bool buySignal = false

daysBack = input.int(1000, title="Strategy Start Days (Backwards from Today)", minval=1)
startDate = timenow - daysBack * 24 * 60 * 60 * 1000
isInTradingPeriod = true

// Execute strategy
if (isInTradingPeriod and rsi < rsiOversold and (time - lastBuyTime) >= cooldownPeriod * 60000)
    strategy.entry("Buy", strategy.long)
    lastBuyTime := time
    buySignal := true
    
    // Show detailed info in trade list
    strategy.order("Buy", strategy.long, comment="USD: " + str.tostring(usdAmount))
else
    buySignal := false

// Show small marker at buy points
plotshape(buySignal, title="Buy Signal", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)

// Display RSI on chart
plot(rsi, "RSI", color=color.purple)
hline(rsiOversold, "RSI Oversold", color=color.red)

// Calculate and display summary
if (barstate.islastconfirmedhistory)
    tradeCount = strategy.opentrades
    totalUsd = usdAmount * tradeCount
    totalBtc = strategy.position_size
    
    // Calculate correct average buy cost
    avgCost = totalBtc != 0 ? totalUsd / totalBtc : na
    
    label.new(bar_index, high, text="\nTotal USD: " + str.tostring(totalUsd) + 
              "\nTotal BTC: " + str.tostring(totalBtc) + 
              "\nBuy Cost: " + str.tostring(avgCost,"#.##") + 
              "\nTrade Count: " + str.tostring(tradeCount), 
              style=label.style_label_down, 
              color=color.new(color.teal, 20),
              textalign="left")
```