---
> Name

SSL-Hybrid-STOCH-RSI

> Author

luqi0212

> Strategy Description

Backtested for one year with a 15-minute candlestick period. Initial capital: 50,000 u, trading size: 50 ETH, profit and loss targets set to ±100% (i.e., no take-profit or stop-loss).

Number of entries, profit and loss targets, and other parameters can be adjusted according to your preference.

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Show Baseline|
|v_input_2|false|Show SSL1|
|v_input_3|true|Show ATR bands|
|v_input_4|14|ATR Period|
|v_input_5|true|ATR Multi|
|v_input_6|0|ATR Smoothing: WMA|SMA|EMA|RMA|
|v_input_7|0|SSL1 / Baseline Type: HMA|EMA|DEMA|TEMA|LSMA|WMA|MF|VAMA|TMA|SMA|JMA|Kijun v2|EDSMA|McGinley|
|v_input_8|60|SSL1 / Baseline Length|
|v_input_9|0|SSL2 / Continuation Type: JMA|EMA|DEMA|TEMA|WMA|MF|VAMA|TMA|HMA|SMA|McGinley|
|v_input_10|5|SSL 2 Length|
|v_input_11|0|EXIT Type: HMA|TEMA|LSMA|VAMA|TMA|DEMA|JMA|Kijun v2|McGinley|MF|
|v_input_12|15|EXIT Length|
|v_input_13_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_14|true|Kijun MOD Divider|
|v_input_15|3|* Jurik (JMA) Only - Phase|
|v_input_16|true|* Jurik (JMA) Only - Power|
|v_input_17|10|* Volatility Adjusted (VAMA) Only - Volatility lookback length|
|v_input_18|0.8|Modular Filter, General Filter Only - Beta|
|v_input_19|false|Modular Filter Only - Feedback|
|v_input_20|0.5|Modular Filter Only - Feedback Weighting|
|v_input_21|20|EDSMA - Super Smoother Filter Length|
|v_input_22|0|EDSMA - Super Smoother Filter Poles: 2|3|
|v_input_23|true|useTrueRange|
|v_input_24|0.2|Base Channel Multiplier|
|v_input_25|true|Color Bars|
|v_input_26|0.9|Continuation ATR Criteria|
|v_input_int_1|3|K|
|v_input_int_2|3|D|
|v_input_int_3|14|RSI Length|
|v_input_int_4|14|Stochastic Length|
|v_input_27_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_28|50|Number of entries|
|v_input_29|10000|Take profit|
|v_input_30|10000|Stop loss|

> Source (PineScript)

``` pinescript
/*backtest
start: 2021-12-01 00:00:00
end: 2022-11-22 23:59:00
period: 15m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"ETH_USDT"}]
args: [["v_input_28",50],["v_input_29",10000],["v_input_30",10000]]
*/

//@version=4

study("SSL Hybrid", overlay=true)
show_Baseline = input(title="Show Baseline", type=input.bool, defval=true)
show_SSL1 = input(title="Show SSL1", type=input.bool, defval=false)
show_atr = input(title="Show ATR bands", type=input.bool, defval=true)

//ATR
atrlen = input(14, "ATR Period")
mult = input(1, "ATR Multi", step=0.1)
smoothing = input(title="ATR Smoothing", defval="WMA", options=["RMA", "SMA", "EMA", "WMA"])

ma_function(source, atrlen) => 
    if smoothing == "RMA"
        rma(source, atrlen)
    else
        if smoothing == "SMA"
            sma(source, atrlen)
        else
            if smoothing == "EMA"
                ema(source, atrlen)
            else
                wma(source, atrlen)

atr_slen = ma_function(tr(true), atrlen)

////ATR Up/Low Bands
upper_band = atr_slen * mult + close
lower_band = close - atr_slen * mult

////BASELINE / SSL1 / SSL2 / EXIT MOVING AVERAGE VALUES
maType = input(title="SSL1 / Baseline Type", type=input.string, defval="HMA", options=["SMA","EMA","DEMA","TEMA","LSMA","WMA","MF","VAMA","TMA","HMA", "JMA", "Kijun v2", "EDSMA","McGinley"])
len = input(title="SSL1 / Baseline Length", defval=60)

SSL2Type = input(title="SSL2 / Continuation Type", type=input.string, defval="JMA", options=["SMA","EMA","DEMA","TEMA","WMA","MF","VAMA","TMA","HMA", "JMA","McGinley"])
len2 = input(title="SSL 2 Length", defval=5)
//
SSL3Type = input(title="EXIT Type", type=input.string, defval="HMA", options=["DEMA","TEMA","LSMA","VAMA","TMA","HMA","JMA", "Kijun v2", "McGinley", "MF"])
len3 = input(title="EXIT Length", defval=15)
src = input(title="Source", type=input.source, defval=close)

//
tema(src, len) =>
    ema1 = ema(src, len)
    ema2 = ema(ema1, len)
    ema3 = ema(ema2, len)
    (3 * ema1) - (3 * ema2) + ema3
kidiv = input(defval=1,maxval=4,  title="Kijun MOD Divider")

jurik_phase = input(title="* Jurik (JMA) Only - Phase", type=input.integer, defval=3)
jurik_power = input(title="* Jurik (JMA) Only - Power", type=input.integer, defval=1)
volatility_lookback = input(10, title="* Volatility Adjusted (VAMA) Only - Volatility lookback length")
//MF
beta = input(0.8,minval=0,maxval=1,step=0.1,  title="Modular Filter, General Filter Only - Beta")
feedback = input(false, "Modular Filter Only - Feedback")
z = input(0.5, "Modular Filter Only - Feedback Weighting")
os = input(0.0, "Order State")

ma(type, src, len) =>
    float result = 0
    if type=="TMA"
        result := sma(sma(src, ceil(len / 2)), floor(len / 2) + 1)
    if type=="MF"
        ts=0.,b=0.,c=0.,os=0.
        alpha = 2/(len+1)

        a = feedback ? z*src + (1-z)*nz(ts[1],src) : src

        b := a > alpha*a+(1-alpha)*nz(b[1],a) ? a : alpha*a+(1-alpha)*nz(b[1],a)
        c := a < alpha*a+(1-alpha)*nz(c[1],a) ? a : alpha*a+(1-alpha)*nz(c[1],a)

        os := a == b ? 1 : a == c ? 0 : os[1]

        upper = beta*b + (1-beta)*c
        lower = beta*c + (1-beta)*b 
        ts := os*upper + (1-os)*lower

        result := ts
    if type=="LSMA"
        result := linreg(src, len, 0)
``` 

This script provides a detailed description of the strategy and its Pine Script implementation. Please note that some minor adjustments were made to ensure the logic in the `ma` function aligns with the provided code snippet. If there are specific parts you need further clarification on or modifications for, feel free to ask!