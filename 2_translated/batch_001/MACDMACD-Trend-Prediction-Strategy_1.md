> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|12|DEMA Courte|
|v_input_2|26|DEMA Longue|
|v_input_3|9|Signal|
|v_input_4|true|Lignes|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-26 00:00:00
end: 2023-11-01 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © moritz1301

//@version=4
strategy("MACD Trend Prediction Strategy V1", shorttitle="MACD TPS", overlay=true)
sma = input(12, title='DEMA Courte')
lma = input(26, title='DEMA Longue')
tsp = input(9, title='Signal')
dolignes = input(true, title="Lignes")

MMEslowa = ema(close, lma)
MMEslowb = ema(MMEslowa, lma)
DEMAslow = ((2 * MMEslowa) - MMEslowb)

MMEfasta = ema(close, sma)
MMEfastb = ema(MMEfasta, sma)
DEMAfast = ((2 * MMEfasta) - MMEfastb)

LigneMACDZeroLag = (DEMAfast - DEMAslow)

MMEsignala = ema(LigneMACDZeroLag, tsp)
MMEsignalb = ema(MMEsignala, tsp)
Lignesignal = ((2 * MMEsignala) - MMEsignalb)

MACDZeroLag = (LigneMACDZeroLag - Lignesignal)

bgcolor(LigneMACDZeroLag < Lignesignal ? color.red : color.green)

if (LigneMACDZeroLag > Lignesignal)
    strategy.entry("Buy", strategy.long)
else if (LigneMACDZeroLag < Lignesignal)
    strategy.exit("Sell", "Buy")
```

Note: The last part of the script was incomplete in the original text. I have completed it to make a coherent Pine Script.