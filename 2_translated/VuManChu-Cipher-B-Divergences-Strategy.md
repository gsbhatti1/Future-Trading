> Name

VuManChu-Cipher-B-Divergences-Strategy

> Author

ChaoZhang

> Strategy Description

A strategy using VuManChu Cipher B + Divergences for backtesting purposes.

**backtest**

 ![IMG](https://www.fmz.com/upload/asset/11eb4c027659ace3042.png) 

> Strategy Arguments


|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Show WaveTrend|
|v_input_2|true|Show Buy dots|
|v_input_3|true|Show Gold dots|
|v_input_4|true|Show Sell dots|
|v_input_5|true|Show Div. dots|
|v_input_6|true|Show Fast WT|
|v_input_7|9|WT Channel Length|
|v_input_8|12|WT Average Length|
|v_input_9_hlc3|0|WT MA Source: hlc3|high|low|open|hl2|close|hlcc4|ohlc4|
|v_input_10|3|WT MA Length|
|v_input_11|53|WT Overbought Level 1|
|v_input_12|60|WT Overbought Level 2|
|v_input_13|100|WT Overbought Level 3|
|v_input_14|-53|WT Oversold Level 1|
|v_input_15|-60|WT Oversold Level 2|
|v_input_16|-75|WT Oversold Level 3|
|v_input_17|true|Show WT Regular Divergences|
|v_input_18|false|Show WT Hidden Divergences|
|v_input_19|true|Do not apply OB/OS limits on hidden divergences|
|v_input_20|45|WT Bearish Divergence min|
|v_input_21|-65|WT Bullish Divergence min|
|v_input_22|true|Show 2nd WT Regular Divergences|
|v_input_23|15|WT 2nd Bearish Divergence|
|v_input_24|-40|WT 2nd Bullish Divergence 15 min|
|v_input_25|true|Show MFI|
|v_input_26|60|MFI Period|
|v_input_27|150|MFI Area multiplier|
|v_input_28|2.5|MFI Area Y Pos|
|v_input_29|false|Show RSI|
|v_input_30_close|0|RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_31|14|RSI Length|
|v_input_32|30|RSI Oversold|
|v_input_33|60|RSI Overbought|
|v_input_34|false|Show RSI Regular Divergences|
|v_input_35|false|Show RSI Hidden Divergences|
|v_input_36|60|RSI Bearish Divergence min|
|v_input_37|30|RSI Bullish Divergence min|
|v_input_38|true|Show Stochastic RSI|
|v_input_39|true| Use Log?|
|v_input_40|false|Use Average of both K & D|
|v_input_41_close|0|Stochastic RSI Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_42|14|Stochastic RSI Length|
|v_input_43|14|RSI Length |
|v_input_44|3|Stochastic RSI K Smooth|
|v_input_45|3|Stochastic RSI D Smooth|
|v_input_46|false|Show Stoch Regular Divergences|
|v_input_47|false|Show Stoch Hidden Divergences|
|v_input_48|false|Show Schaff TC line|
|v_input_49_close|0|Schaff TC Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_50|10|Schaff TC|
|v_input_51|23|Schaff TC Fast Lenght|
|v_input_52|50|Schaff TC Slow Length|
|v_input_53|0.5|Schaff TC Factor|
|v_input_54|false|Show Sommi flag|
|v_input_55|false|Show Sommi F. Wave|
|v_input_56|720|Sommi F. Wave timeframe|
|v_input_57|false|F. Wave Bear Level (less than)|
|v_input_58|false|F. Wave Bull Level (more than)|
|v_input_59|false|WT Bear Level (more than)|
|v_input_60|false|WT Bull Level (less than)|
|v_input_61|false|Money flow Bear Level (less than)|
|v_input_62|false|Money flow Bull Level (more than)|
|v_input_63|false|Show Sommi diamond|
|v_input_64|60|HTF Candle Res. 1|
|v_input_65|240|HTF Candle Res. 2|
|v_input_66|false|WT Bear Level (More than)|
|v_input_67|false|WT Bull Level (Less than)|
|v_input_68|false|Show MACD Colors|
|v_input_69|240|MACD Colors MACD TF|
|v_input_70|false|Dark mode|
|v_input_71|14|len|
|v_input_72|20|th|
|v_input_77|10|length|
|v_input_73|100|(?RSI Settings)RSI Length|
|v_input_74_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_75|25|RSI Length|
|v_input_76_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_78|5|(?Directional Energy Ratio)Average|
|v_input_79|3|Smoothing|
|v_input_80|0|(?Volume Parameters)Calculation: Relative|Full|None|
|v_input_81|20|Lookback (for Relative)|


> Source (PineScript)

``` pinescript
/* backtest
start: 2022-04-16 00:00:00
end: 2022-05-15 23:59:00
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © vumanchu

//@version=4


// Thanks to dynausmaux for the code
// Thanks to falconCoin for https://www.tradingview.com/script/KVfgBvDd-Market-Cipher-B-Free-version-with-Buy-and-sell/ inspired me to start this.
// Thanks to LazyBear for WaveTrend Oscillator https://www.tradingview.com/script/2KE8wTuF-Indicator-WaveTrend-Oscillator-WT/
// Thanks to RicardoSantos for https://www.tradingview.com/script/3oeDh0Yq-RS-Price-Divergence-Detector-V2/
// Thanks to LucemAnb for Plain Stochastic Divergence https://www.tradingview.com/script/FCUgF8ag-Plain-Stochastic-Divergence/
// Thanks to andreholanda73 for RSI and other indicators
// I am not an expert trader or know how to program pine script as such, in fact it is my first indicator only to study and all the code is copied and modified from other codes that are published in TradingView.
// I am very grateful to the entire TV community that publishes codes so that other newbies like me can learn and present their results. This is an attempt to imitate Market Cipher B.

// Settings by default are for 4h timeframe, divergences are more stronger and accurate. Haven't tested in all timeframes, only 2h and 4h.
```