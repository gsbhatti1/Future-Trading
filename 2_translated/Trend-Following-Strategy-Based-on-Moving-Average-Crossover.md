> Name

Trend-Following-Strategy-Based-on-Moving-Average-Crossover

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1186010fe636f555290.png)

[trans]

## Overview

This strategy primarily uses the golden cross and dead cross of moving averages, along with candlestick breaks of moving averages to make long and short decisions. When a short-term moving average crosses over a longer-term moving average, it goes long; when a short-term moving average crosses below a longer-term moving average, it goes short. Additionally, the closing price of candlesticks breaking through the moving average is also used as an entry signal.

## Principles

1. Calculate two different period moving averages EMA1 and EMA2. EMA1 has a shorter period while EMA2 has a longer period.

2. Determine if EMA1 crosses over EMA2, if yes, go long.

3. Determine if EMA1 crosses below EMA2, if yes, go short.

4. Determine if the closing price breaks through EMA1 as the entry signal.

5. Exit mechanism: set fixed stop loss or use Donchian Channel to set stop loss.

Main functions used:

- ema(): calculate exponential moving average
- crossover(): determine if EMA1 crosses over EMA2
- crossunder(): determine if EMA1 crosses below EMA2
- rising()/falling(): determine if price is rising/falling
- valuewhen(): return different values based on condition

## Advantages

1. The strategy logic is simple and easy to understand and implement.

2. Utilizing the trend-following characteristics of moving averages, it can effectively track trends.

3. Combining candlestick closing prices breaking through the moving average helps avoid false breaks.

4. Flexible use of different moving average combinations adapts to various time periods.

5. A stop-loss mechanism controls risk.

## Risks

1. During consolidation markets, frequent golden crosses and dead crosses may result in whipsaws.

2. Fixed stop loss points may be too rigid and unable to adjust based on market changes.

3. Moving averages lag and may miss reversal signals at turning points.

4. Precise judgment of moving average slope is needed to filter false breaks.

5. Careful selection of parameters is necessary; inappropriate frequency or lag can affect strategy performance.

## Optimization

1. MACD zero line crossovers can help determine trends and filter consolidations.

2. Add Donchian Channels for dynamic stop loss lines to improve fixed stop losses.

3. Include Bollinger Bands to judge strong or weak trends, avoiding ineffective trading in consolidation markets.

4. Optimize moving average parameter combinations and test the actual effectiveness of different period strategies.

5. Consider adding anchored moving averages to reduce lag.

## Conclusion

The overall logic of this strategy is simple and clear, utilizing classic moving average crossover trading techniques combined with candlestick breakout for entry, which can effectively filter false signals. Optimization spaces include using other indicators for trend strength, setting dynamic stops, etc. Overall, trend-following strategies based on moving averages are classical and intuitive, with valuable exploration space for optimization.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|Candle body resistance Channel: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|false|Bar Channel On/Off|
|v_input_3|10|Support / Resistance length:|
|v_input_4|13|EMA 1|
|v_input_5|21|EMA 2|
|v_input_6|false|Display Hull MA Set:|
|v_input_7_close|0|Hull MA's Source:: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_8|8|Hull MA's Base Length:|
|v_input_9|5|Hull MA's Length Scalar:|
|v_input_10|720|period|


> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-01 00:00:00
end: 2023-10-23 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy(title='Mega crypto bot strategy', shorttitle='megacryptobot_Strategy', overlay=true, pyramiding=0, initial_capital=10000, currency=currency.USD)

// Candle body resistance Channel -----------------------------//
len = 34
src = input(close, title="Candle body resistance Channel")
out = sma(src, len)
last8h = highest(close, 13)
lastl8 = lowest(close, 13)
bearish = cross(close,out) == 1 and falling(close, 1)
bullish = cross(close,out) == 1 and rising(close, 1)
channel2=input(false, title="Bar Channel On/Off")
ul2=plot(channel2?last8h:last8h==nz(last8h[1])?last8h:na, color=black, linewidth=1, style=linebr, title="Candle body resistance level top", offset=0)
ll2=plot(channel2?lastl8:lastl8==nz(lastl8[1])?lastl8:na, color=black, linewidth=1, style=linebr, title="Candle body resistance level bottom", offset=0)
// fill(ul2, ll2, color=black, transp=95, title="Candle body resistance Channel")

//-----------------Support and Resistance 
RST = input(title='Support / Resistance length:',  defval=10) 
RSTT = valuewhen(high >= highest(high, RST), high, 0)
RSTB = valuewhen(low <=