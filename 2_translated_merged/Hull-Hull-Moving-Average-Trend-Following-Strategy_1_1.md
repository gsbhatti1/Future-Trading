> Name

Hull-Moving-Average-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

[trans]

## Overview

The Hull moving average trend following strategy is a quantitative trading strategy that uses the Hull moving average to determine market trend direction and generate buy and sell signals. It can capture mid-to-long term trends, establish positions early in trend beginnings, and close out before trend reversals.

## Principles

This strategy utilizes both the Hull moving average and simple moving average (EMA) to identify trend direction. A buy signal is generated when the shorter period Hull MA crosses above the longer period Hull MA. Conversely, a sell signal is triggered when the shorter Hull MA crosses below the longer one.

The EMA determines real-time trend direction. An uptrend is indicated when the short-term EMA crosses above the long-term EMA; conversely, a downtrend occurs when the short-term EMA falls below the long-term EMA. Trades are executed only if both Hull MA and EMA signals agree on the bullish or bearish bias.

Additionally, this strategy uses K-line body channels to gauge market volatility and avoid trading in consolidation zones. Positions are considered only after prices break out of the channel range.

## Advantages

- The Hull moving average is more sensitive to price changes, allowing for early trend detection.
- Combining both Hull MA and EMA helps filter out false signals.
- K-line channels prevent excessive trading during sideways markets.
- Trend following enables sustained profit capture as trends persist.

## Risks

- Moving averages have lag, potentially missing optimal entry points in trend reversals.
- Inaccurate consolidation detection may result in bad trades.
- Low trade frequency increases the impact of single losing trades.
- Unable to fully capitalize on short-term oscillations.

## Risk Management

- Optimize moving average periods for timely trend signal generation.
- Utilize additional indicators like RSI and Bollinger Bands (BBANDS) to detect consolidation.
- Implement aggressive capital management techniques to limit per-trade loss percentages.
- Supplement with other strategies to capture short-term profits.

## Summary

The Hull moving average trend following strategy effectively tracks mid-to-long term trends by combining the use of Hull MA and EMA. It accumulates profits during profitable trends and exits early before reversals. This is a simple and practical quant trading strategy worth recommending.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|Candle body resistance Channel: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|false|Bar Channel On/Off|
|v_input_3|15|Support / Resistance length:|
|v_input_4|13|EMA 1|
|v_input_5|21|EMA 2|
|v_input_6|false|Display Hull MA Set:|
|v_input_7_close|0|Hull MA's Source:: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_8|16|Hull MA's Base Length:|
|v_input_9|10|Hull MA's Length Scalar:|
|v_input_10|720|Piriod|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-08-16 00:00:00
end: 2023-09-15 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2

// strategy(title='HULLMiguel 2019/ Strategy v3', shorttitle='HULLMiguel_2019_Strategy', overlay=true, pyramiding=0, default_qty_value=1000, initial_capital=1000, currency=currency.USD)

// Candle body resistance Channel-----------------------------//
len = 34
src = input(close, title="Candle body resistance Channel")
out = sma(src, len)
last8h = highest(close, 13)
lastl8 = lowest(close, 13)
bearish = cross(close,out) == 1 and falling(close, 1)
bullish = cross(close,out) == 1 and rising(close, 1)
channel2=input(false, title="Bar Channel On/Off")
ul2=plot(channel2?last8h:last8h==nz(last8h[1])?last8h:na, color=black, linewidth=1, style=linebr, title="Candle body resistance level top", offset=0)
ll2=plot(channel2?lastl8:lastl8==nz(lastl8[1])?lastl8:na, color=blue, linewidth=1, style=linebr, title="Candle body resistance level bottom", offset=0)
//fill(ul2, ll2, color=black, transp=95, title="Candle body resistance Channel")

//-----------------Support and Resistance 
RST = input(title='Support / Resistance length:',  defval=15) 
RSTT = valuewhen(high >= highest(high, RST), high, 0)
RSTB = valuewhen(low <= lowest(low, RST), low, 0)
RT2 = plot(RSTT, color=RSTT != RSTT[1] ? na : red, linewidth=1, offset=+0)
RB2 = plot(RSTB, color=RSTB != RSTB[1] ? na : green, linewidth=1, offset=0)

//--------------------Trend colour ema------------------------------------------------// 
src0 = close, len0 = input(13, minval=1, title="EMA 1")
ema0 = ema(src0, len0)
direction = rising(ema0, 2) ? +1 : falling(ema0, 2) ? -1 : 0
plot_color = direction > 0  ? lime: direction < 0 ? red : na
plot(ema0, title="EMA", style=line, linewidth=3, color = plot_color)

//-------------------- ema 2------------------------------------------------//
src02 = close, len02 = input(21, minval=1, title="EMA 2")
ema02 = ema(src02, len02)
direction2 = rising(ema02, 2) ? +1 : falling(ema02, 2) ? -1 : 0
plot_color2 = direction2 > 0  ? green: direction2 < 0 ? red : na
plot(ema02, title="EMA Signal 2", style=line, linewid