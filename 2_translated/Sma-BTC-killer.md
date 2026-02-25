> Name

Sma-BTC-killer

> Author

ChaoZhang

> Strategy Description

Hello !!


I made a nice strategy with insane profit using only LONG and SHORT orders. 
Well, this strategy is for ------->>> BINANCE:BTCUSDT.

The strategy logic is quite simple:

This strategy uses 3 different SMAs (7, 21, 55) to find the correct trend.
To avoid a lot of wrong signals, I added two indicators like:

- ADX - One of the most powerful and accurate trend indicators. ADX measures how strong a trend is, and can give valuable information on whether there is a potential trading opportunity.
- CLOUD - This is one of the newest indicators I'm using. This indicator helps in identifying the correct market trend. By applying the length of this indicator, I am able to notice a change in the trend a little later but more accurately.

Additionally, I added trailing stop-loss for maximum security.

To be honest, this strategy looks really good. It has many trades, high profit, and a small amount of indicators. The future profits could be similar.

Using these combinations of SMAs gives me amazing quick changes while the trend is also changing fast like here:

![Snapshot](https://www.fmz.com/upload/asset/b9533260444f2dfb3e.png)

Unfortunately, I was not able to 100% eliminate wrong signals on a flat chart like here:

![Snapshot](https://www.fmz.com/upload/asset/b9533260444f2dfb3e.png)


I hope this strategy will be useful for anyone ;)



As always



ENJOY !!


**Backtest**

![](https://www.fmz.com/upload/asset/b9533260444f2dfb3e.png)

> Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 14 |  1-SMA Length |
| v_input_2 | 28 |  2-SMA Length |
| v_input_3 | 55 |  3-SMA Length |
| v_input_4 | 0 | (Average Directional Index) ADX Type: MASANAKAMURA | CLASSIC |
| v_input_5 | 29 |  ADX Length |
| v_input_6 | 21 |  ADX Threshold |
| v_input_7 | 11 | (Cloud) Cloud Length |
| v_input_8 | 18 | (Average True Range) PP Period |
| v_input_9 | 5 |  ATR Factor |
| v_input_10 | 6 |  ATR Period |

> Source (PineScript)

```pinescript
/*backtest
start: 2022-01-01 00:00:00
end: 2022-02-11 23:59:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Bitfinex","currency":"BTC_USD"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © wielkieef


//@version=4

src = close

// strategy("Sma BTC killer [60MIN]", overlay = true, pyramiding=1,initial_capital = 10000, default_qty_type= strategy.percent_of_equity, default_qty_value = 100, calc_on_order_fills=false, slippage=0,commission_type=strategy.commission.percent,commission_value=0.04)

// SMAs -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Length1 = input(14, title="  1-SMA Length", minval=1)
Length2 = input(28, title="  2-SMA Length", minval=1)
Length3 = input(55, title="  3-SMA Length", minval=1)
xPrice = close
SMA1 = sma(xPrice, Length1)
SMA2 = sma(xPrice, Length2)
SMA3 = sma(xPrice, Length3)

// Indicators Inputs -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ADX_options         =                   input("MASANAKAMURA", title="  ADX Type", options = ["CLASSIC", "MASANAKAMURA"], group="Average Directional Index")
ADX_len             =                   input(29, type=input.integer, minval=1, title="  ADX Length", group="Average Directional Index")
th                  =                   input(21, type=input.integer, minval=0, title="  ADX Threshold", group="Average Directional Index")
len                 =                   input(11, title="Cloud Length", group="Cloud")

// ATR Inputs  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

prd                     =               input(18, title="  PP Period", group="Average True Range")
Factor                  =               input(5, title="  ATR Factor", group="Average True Range")
Pd                      =               input(6, title="  ATR Period", group="Average True Range")

// Indicators -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

calcADX(_len) =>
    up              =                                                                                                                       change(high)
	down            =                                                           
```