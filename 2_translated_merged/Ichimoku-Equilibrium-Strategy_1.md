``` pinescript
/*backtest
start: 2023-09-29 00:00:00
end: 2023-10-29 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 26/09/2018
//  Ichimoku Strategy
//
// You can change long to short in the Input Settings
// WARNING:
// - For purpose educate only
// - This script to change bars colors.
////////////////////////////////////////////////////////////
middleDonchian(Length) =>
    lower = lowest(Length)
    upper = highest(Length)
    avg(upper, lower)

strategy(title="Ichimoku2c Backtest", shorttitle="Ichimoku2c", overlay = true)
conversionPeriods = input(9, minval=1),
basePeriods = input(26, minval=1)
laggingSpan2Periods = input(52, minval=1),
displacement = input(26, minval=1)
reverse = input(false, title="Trade reverse")
Tenkan = middleDonchian(conversionPeriods)
Kijun = middleDonchian(basePeriods)

// Calculate Senkou A and Senkou B lines
SenkouA = middleDonchian(laggingSpan2Periods) + displacement
SenkouB = (Tenkan + Kijun) / 2

// Determine buy/sell signals based on close price relative to Senkou A and Senkou B
pos = na(pos)
if (close > SenkouA)
    pos := 1
else if (close < SenkouB)
    pos := -1

plot(pos, title="Position", color=color.red)

// Trading logic based on the reverse input parameter
possig = not reverse ? pos : -pos

if (possig == 1)
    strategy.entry("Buy", strategy.long)
else if (possig == -1)
    strategy.exit("Sell", "Buy")

plot(SenkouA, title="Senkou A", color=color.blue)
plot(SenkouB, title="Senkou B", color=color.orange)
```

This updated Pine Script code completes the Ichimoku Equilibrium strategy by incorporating the buy/sell logic and plotting the Senkou lines. The `middleDonchian` function is used to calculate Tenkan and Kijun lines, while the strategy determines positions based on the relationship between close price and Senkou A/B lines, with an additional reverse parameter to adjust trade direction.