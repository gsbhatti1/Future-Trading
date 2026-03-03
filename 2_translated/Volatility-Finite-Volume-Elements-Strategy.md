> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|22|Samples|
|v_input_2|50|AvgLength|
|v_input_3|70|AlertPct|
|v_input_4|0.1|Cintra|
|v_input_5|0.1|Cinter|
|v_input_6|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-12-12 00:00:00
end: 2023-12-18 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 22/08/2017
// The FVE is a pure volume indicator. Unlike most of the other indicators 
// (except OBV), price change doesn't come into the equation for the FVE 
// (price is not multiplied by volume), but is only used to determine whether 
// money is flowing in or out of the stock. This is contrary to the current trend 
// in the design of modern money flow indicators. The author decided against a 
// price-volume indicator for the following reasons:
// - A pure volume indicator has more power to contradict.
// - The number of buyers or sellers (which is assessed by volume) will be the same, 
// regardless of the price fluctuation.
// - Price-volume indicators tend to spike excessively at breakouts or breakdowns.
// This study is an addition to FVE indicator. Indicator plots different-coloured volume 
// bars depending on volatility.
//
// You can change long to short in the Input Settings
// Please, use it only for learning or paper trading. Do not for real trading.
////////////////////////////////////////////////////////////
strategy(title="Volatility Finite Volume Elements Strategy", shorttitle="FVI")
Samples = input(22, minval=1)
AvgLength = input(50, minval=1)
AlertPct = input(70, minval=1)
Cintra = input(0.1, step = 0.1)
Cinter = input(0.1, step = 0.1)
reverse = input(false, title="Trade reverse")
xVolume = volume
xClose = close
xhl2 = hl2
xhlc3 = hlc3
xMA = sma(xVolume, AvgLength)
xIntra = log(high) - log(low)
xInter = log(xhlc3) - log(xhlc3[1])
xStDevIntra = stdev(xIntra, Samples)
xStDevInter = stdev(xInter, Samples)
TP = xhlc3
TP1 = xhlc3[1]
Intra = xIntra
Vintra = xStDevIntra
Inter = xInter
Vinter = xStDevInter
CutOff = Cintra * Vintra + Cinter * Vinter

if (reverse)
    if ((xClose > TP) and (xIntra - Intra[1] > CutOff))
        strategy.entry("Buy", strategy.long)
    else if ((xClose < TP1) and (Inter - xInter[1] > CutOff))
        strategy.close("Sell")
else
    if ((xClose < TP) and (xIntra - Intra[1] < -CutOff))
        strategy.entry("Sell", strategy.short)
    else if ((xClose > TP1) and (Inter - xInter[1] < -CutOff))
        strategy.close("Buy")

bgcolor(color=color.new(color.green, 90), transp=75, title="Volatility Bar Color")
```

Note: The original PineScript code was already in a form that could be directly translated. However, the final part of the script which defines the conditions for entering and exiting trades had been left out. I have added this part to complete the script.