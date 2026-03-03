> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|10|Length|
|v_input_2|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-08 00:00:00
end: 2024-01-07 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version = 2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 15/12/2016
// 	Market prices do not have a Gaussian probability density function
// 	as many traders think. Their probability curve is not bell-shaped.
// 	But trader can create a nearly Gaussian PDF for prices by normalizing
// 	them or creating a normalized indicator such as the relative strength
// 	index and applying the Fisher transform. Such a transformed output 
// creates the peak swings as relatively rare events.
// 	Fisher transform formula is: y = 0.5 * ln ((1+x)/(1-x))
// 	The sharp turning points of these peak swings clearly and unambiguously
// identify price reversals in a timely manner. 
//
// You can change long to short in the Input Settings
// Please, use it only for learning or paper trading. Do not for real trading.
////////////////////////////////////////////////////////////
strategy(title="Fisher Transform Indicator by Ehlers Backtest", shorttitle="Fisher Transform Indicator by Ehlers")
Length = input(10, minval=1)
reverse = input(false, title="Trade reverse")
xHL2 = hl2
xMaxH = highest(xHL2, Length)
xMinL = lowest(xHL2, Length)
nValue1 = 0.33 * 2 * ((xHL2 - xMinL) / (xMaxH - xMinL) - 0.5)

// Apply Fisher Transform
nFish = 0.5 * math.log((1 + nValue1) / (1 - nValue1))

// Determine trade direction based on Fisher indicator turning points
if (nFish > nz(nFish[1]))
    pos := 1  // Long position
else if (nFish < nz(nFish[1]))
    pos := -1 // Short position
else 
    pos := 0

// Generate trading signals based on trade direction
strategy.entry("Long", onlybacktest=true, when=pos == 1)
strategy.exit("Short", "Long", when=nFish < nz(nFish[1]), trailpercent=1)

```

Note: The original PineScript provided a basic structure but lacked the complete implementation of the trading logic based on Fisher Transform. The updated script includes applying the Fisher transform and generating trade signals accordingly, as described in the strategy description.