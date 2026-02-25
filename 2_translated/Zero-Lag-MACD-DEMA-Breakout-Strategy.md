> Name

Zero-Lag-MACD-DEMA-Breakout-Strategy

> Author

ChaoZhang

> Strategy Description


[trans]
Zero-Lag MACD DEMA Breakout Strategy

This strategy builds trading signals based on Toff’s MACD DEMA indicator. The MACD DEMA indicator calculates the difference between the DEMA fast line and the DEMA slow line, with zero-lag processing, effectively eliminating the lagging issue of regular MACD.

The trading rules are: go long when the zero-lag MACD crosses above the 0 axis; go short when the zero-lag MACD crosses below the 0 axis. The long and short positions can be determined by the MACD's breakthrough on the 0 axis.

The advantage of this strategy based on zero-lag MACD is that it can capture trend changes more sensitively, and using DEMA instead of EMA can filter out false breakouts. However, the MACD indicator itself has limited ability to judge complex market conditions, and there is a risk of false signals. It needs to be combined with the trend filter indicator to improve stability.

In general, the zero-lag MACD DEMA breakout strategy works well for strong trending markets and can quickly seize opportunities. However, its performance is poor in consolidation markets and should be used with caution. Only by continuously optimizing parameters and strictly controlling risks can this strategy be applied in the long term.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|2000|Backtest Start Year|
|v_input_2|true|Backtest Start Month|
|v_input_3|true|Backtest Start Day|
|v_input_4|2100|Backtest Stop Year|
|v_input_5|12|Backtest Stop Month|
|v_input_6|31|Backtest Stop Day|
|v_input_7|12|DEMA Short Period|
|v_input_8|26|DEMA Long Period|
|v_input_9|9|Signal Period|
|v_input_10|true|Show Lines|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-09-10 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
// strategy(title="Patron04 MACD DEMA Strategy", default_qty_type = strategy.percent_of_equity, default_qty_value = 3500, overlay=true)

testStartYear = input(2000, "Backtest Start Year")
testStartMonth = input(1, "Backtest Start Month")
testStartDay = input(1, "Backtest Start Day")
testPeriodStart = timestamp(testStartYear,testStartMonth,testStartDay,0,0)

testStopYear = input(2100, "Backtest Stop Year")
testStopMonth = input(12, "Backtest Stop Month")
testStopDay = input(31, "Backtest Stop Day")
testPeriodStop = timestamp(testStopYear,testStopMonth,testStopDay,0,0)

testPeriod() =>
    time >= testPeriodStart and time <= testPeriodStop ? true : false

sma = input(12, title='DEMA Short Period')
lma = input(26, title='DEMA Long Period')
tsp = input(9, title='Signal Period')
dolignes = input(true, title="Show Lines")

MMEslowa = ema(close, lma)
MMEslowb = ema(MMEslowa, lma)
DEMAslow = ((2 * MMEslowa) - MMEslowb )

MMEfasta = ema(close, sma)
MMEfastb = ema(MMEfasta, sma)
DEMAfast = ((2 * MMEfasta) - MMEfastb)

LigneMACDZeroLag = (DEMAfast - DEMAslow)

MMEsignala = ema(LigneMACDZeroLag, tsp)
MMEsignalb = ema(MMEsignala, tsp)
Lignesignal = ((2 * MMEsignala) - MMEsignalb )

MACDZeroLag = (LigneMACDZeroLag - Lignesignal)

long = LigneMACDZeroLag > 0
short = LigneMACDZeroLag < 0

if testPeriod()
    strategy.entry("Long", strategy.long, when=long)
    strategy.entry("Short", strategy.short, when=short)
```


> Detail

https://www.fmz.com/strategy/426360

> Last Modified

2023-09-11 14:43:52