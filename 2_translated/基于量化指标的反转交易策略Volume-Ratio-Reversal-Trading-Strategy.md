> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Length|
|v_input_2|3|Threshold|
|v_input_3|true|Direction picker # bars|
|v_input_4|2019|Start Year|
|v_input_5|true|Start Month|
|v_input_6|true|Start Day|
|v_input_7|9999|End Year|
|v_input_8|true|End Month|
|v_input_9|true|End Day|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

strategy(title="Volume Ratio_30min", shorttitle="VR_30min") //,initial_capital=1000)

// User Input ------------------------------------------------------------------
len = input(20, title="Length", minval=1)
threshold  = input(3, step=0.05, title="Threshold")

// Volume Calculation ---------------------------------------------------------
vol = volume
sma = sma(volume, len)
vrs = vol / sma

// Direction -------------------------------------------------------------------
dirtime = input(1, "Direction picker # bars")
dir = if close / close[dirtime] > 1
    1
else
    -1

// Plot ------------------------------------------------------------------------
plot(vrs, title="VRS", color=color.green, transp=0)
hline(1, title="baseline")
plot(threshold, color=color.white)

// Logic -----------------------------------------------------------------------
long = vrs > threshold and dir == 1
short = vrs > threshold and dir == -1

// Back Test Function ---------------------------------------------------------
```