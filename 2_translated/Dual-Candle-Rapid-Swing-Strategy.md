```plaintext
Name

Dual-Candle-Rapid-Swing-Strategy

Author

ChaoZhang

Strategy Description


This strategy calculates the combination of daily trading volume changes and NVI indicators to determine market swings within the very short term for trading.

Specifically, it counts the number of days when daily trading volume decreases from the previous day, and uses the change in the NVI value to form an oscillator. Long positions are generated when the indicator flips from negative to positive and remains positive on the second candle. Short positions occur when the indicator flips from positive to negative and remains negative on the second candle.

The advantage of this strategy is that it captures very short-term gaps and only requires two candles to form a trading signal and achieve profits. However, this high-frequency trading method has the risk of over-optimization, and its performance may vary greatly across different market time periods.

Additionally, such short-term transactions also depend on transaction fees, and parameters need to be adjusted for specific instruments. At the same time, errors in trading decisions within a very small period of time could lead to losses. Only by strictly controlling the capital size of each trade can this dual-candle strategy be applied over the long run.

||

This strategy combines calculations of daily volume changes and the NVI indicator to trade short-term market swings.

Specifically, it counts the number of days when volume is lower than that of the previous day, and uses the change in the NVI value to form an oscillator. Long signals are generated when the oscillator flips from negative to positive and remains positive on the second candle. Short signals occur when the oscillator flips from positive to negative and remains negative on the second candle.

The advantage of this strategy is that it capitalizes on short-term gaps within just two candles. However, such high-frequency trading methods risk over-optimization, with performance varying greatly across different market time periods.

Also, transaction fees can be a concern for such short-term trades, requiring parameter tuning per instrument. And slight errors in decisions within small timeframes could lead to losses. Only by strictly controlling the position size of each trade can this dual-candle strategy be applied successfully over the long run.

[/trans]

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|═════════ DESDE ════════|
|v_input_2|true|Mes|
|v_input_3|true|Dia|
|v_input_4|2018|Año|
|v_input_5|true|═════════ HASTA ════════|
|v_input_6|31|Mes|
|v_input_7|12|Dia|
|v_input_8|9999|Año|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-09-04 00:00:00
end: 2023-09-10 00:00:00
Period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
//
//▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒