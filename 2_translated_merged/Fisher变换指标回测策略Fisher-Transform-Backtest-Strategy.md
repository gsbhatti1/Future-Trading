``` pinescript
/*backtest
start: 2023-11-26 00:00:00
end: 2023-12-03 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version = 2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v2.0 22/12/2016
// 	Market prices do not have a Gaussian probability density function
// 	as many traders think. Their probability curve is not bell-shaped.
// 	But trader can create a nearly Gaussian PDF for prices by normalizing
// 	them or creating a normalized indicator such as the relative strength
// 	index and applying the Fisher transform. Such a transformed output 
// creates the peak swings as relatively rare events.
// 	Fisher transform formula is: y = 0.5 * ln ((1+x)/(1-x))
// 	The sharp turning points of these peak swings clearly and unambiguously
// 	identify price reversals in a timely manner. 
//
//  For signal used zero. 
// You can change long to short in the Input Settings
// Please, use it only for learning or paper trading. Do not for real trading.
////////////////////////////////////////////////////////////
strategy(title="Fisher Transform Indicator by Ehlers Backtest", shorttitle="Fisher Transform Indicator by Ehlers")
Length = input(10, minval=1)
reverse = input(false, title="Trade reverse")
hline(0, color=blue)
xHL2 = hl2
xMaxH = highest(xHL2, Length)
xMinL = lowest(xHL2, Length)
nValue1 = 0.33 * 2 * ((xHL2 - xMinL) / (xMaxH - xMinL) - 0.5) + 0.67 * nz(nValue1[1])
nValue2 = iff(nValue1 > nValue1[1], nValue1, nValue2[1])
plot(nValue2, color=red, title="Fisher Transform")
if (reverse)
    strategy.entry("Buy", strategy.long, when=nValue2 < 0)
    strategy.close("Sell", when=nValue2 >= 0)
else
    strategy.entry("Sell", strategy.short, when=nValue2 > 0)
    strategy.close("Buy", when=nValue2 <= 0)
```

This translation maintains the original code structure and formatting while translating the human-readable text to English.