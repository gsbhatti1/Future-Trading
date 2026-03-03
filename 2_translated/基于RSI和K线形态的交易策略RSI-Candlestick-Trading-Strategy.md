> Name

RSI-Candlestick-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy combines the Relative Strength Index (RSI) indicator with candlestick patterns to identify trend-following entry signals when RSI reaches overbought or oversold levels.

## How It Works

1. Calculate RSI values, with 70 as the overbought line and 30 as the oversold line.

2. View RSI crossing above 30 as an oversold signal, and RSI crossing below 70 as an overbought signal.

3. When these signals occur, check if the current or previous candle forms specific patterns like white/black marubozu, hammer/hanging man, etc.

4. If both RSI signal and candlestick condition are met, generate buy/sell signals.

5. Correspondingly, buy on oversold RSI when bullish patterns like hammer occur, and sell on overbought RSI when bearish patterns like shooting star occur.

6. Identify complex combination patterns like tweezer, morning/evening stars for entry signals.

7. RSI crossing the midline acts as an exit signal.

## Advantages

1. Combining indicator and pattern filters fake signals and improves entry accuracy.

2. Candlestick pattern captures significant trend reversal points.

3. RSI overbought/oversold signals increase winning opportunities.

4. Double/Triple candlestick combos catch stronger reversals.

5. RSI cross midline helps lock in profits.

## Risks

1. RSI lag may miss reversal points.

2. Some candlestick signals are weak and give false signals.

3. No stop loss based on recent high/low, risks uncontrolled loss.

4. No trailing stop loss, huge adverse move may enlarge loss.

5. Insufficient backtest data may bias parameter optimization.

## Optimization

1. Add other filters like MACD, Bollinger Bands.

2. Add trendline for stop loss/profit taking.

3. Optimize RSI parameters based on backtest results.

4. Enhance stops like trailing stop, zone stop, etc.

5. Test longer datasets to evaluate parameter robustness.

6. Adjust parameters for different products and market regimes.

## Conclusion

This strategy integrates the strengths of RSI and candlestick pattern recognition to enter on high-quality signals at overbought/oversold turning points for trend-following. Strong combo patterns also improve the odds. But risks like lag and false signals remain, requiring combination with other techniques and further optimization. Overall, it blends multiple winning ideas and may achieve good results if properly parameterized.

---

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|55|RSI Bullish Criteria|
|v_input_3|45|RSI Bearish Criteria|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-09-15 00:00:00
end: 2023-09-21 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

/////////////////////////////////////
//@version=2
//@author=sb
strategy("RSI-candlestick Strategy", overlay=true)
src = hlc3, len = input(14, minval=1, title="Length")
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
//plot(rsi, color=purple)
//band1 = hline(70)
//band0 = hline(30)
//band2 = hline(50,linestyle=dotted,color=silver)
//fill(band1, band0, color=#cc99ff, transp=70)
//end premade RSI
oversold = rsi < 30
overbought = rsi > 70
barcolor(oversold? #7fff00 : overbought? red : na )
//
//
level_70 = 70
level_70rsi = rsi > level_70 ? rsi : level_70
level_30 = 30
level_30rsi = rsi < 30 ? rsi : level_30

level_50 = 50
//


//p1 = plot(series=level_70, color=red, linewidth=1, transp=100)
//p2 = plot(series=level_70rsi, color=red, linewidth=1, transp=100)
//p3 = plot(series=level_30, color=green, linewidth=1, transp=100)
//p4 = plot(series=level_30rsi, color=green, linewidth=1, transp=100)
//fill(p1, p2, color=red, transp=50)
//fill(p3, p4, color=#7fff00, transp=50)




/////////////////////////////////////


bullishcriteria = input(title="RSI Bullish Criteria",  defval=55, minval=50, maxval=100)
bearishcriteria = input(title="RSI Bearish Criteria",  defval=45, minval=0, maxval=50)

range = high - low
body = abs(close - open)
oc2 = min(close, open) + body/2
upperwick = high - max(open, close)
lowerwick = min(open, close) - low

isUp = close > open
isTrendUp = rsi(close, 14) >= bullishcriteria
isTrendDown = rsi(close, 14) <= bearishcriteria
isDoji = abs(close-open)/(high-low) < 0.05

// Single Candlestick Pattern
// white marubozu
wm = (isUp) and (upperwick <= 0.05*body) and (lowerwick <= 0.05*body) and isTrendDown
plotshape(wm, color=green, style=shape.triangleup, location=location.belowbar, title='white marubozu',text='wm')
if (not na(rsi))
    if (crossover(rsi, level_30) and (wm or wm[1]))
        strategy.entry("RsiLE", strategy.long, comment="RsiLE")
// black marubozu
bm = (not isUp) and (upperwick <= 0.05*body) and (lowerwick <= 0.05*body) and isTrendUp
plotshape(bm, color=red, style=shape.triangledown, location=location.abovebar, title='black marubozu',text='bm')
if (not na(rsi))
    if (crossunder(rsi, level_70) and (bm or bm[1]))
        strategy.close("RsiLE", comment="RsiLE")
```

This completes the translation of the trading strategy document into English while maintaining the original code blocks and formatting.