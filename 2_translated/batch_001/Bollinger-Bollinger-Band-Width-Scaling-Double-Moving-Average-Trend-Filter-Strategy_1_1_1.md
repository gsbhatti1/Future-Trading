<!-- AUTO-TRANSLATION FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->

> Name

Bollinger Band Width Scaling Double Moving Average Trend Filter Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/181af817922384577aa.png)

[trans]

This strategy generates trading signals based on Bollinger Bands and double moving averages, combined with trend filtering to achieve a high win rate and favorable risk-reward ratio.

### Strategy Logic

1. Uses the upper, middle, and lower bands of Bollinger Bands to determine long and short signals. A short signal is generated when the price touches the upper band, and a long signal when it touches the lower band.

2. Employs a 20-period medium-short term moving average and a 60-period long-term moving average to judge the trend. An uptrend is indicated when the short-term MA crosses above the long-term MA, and a downtrend when it crosses below.

3. Dynamically adjusts the stop-loss level based on the width of the Bollinger Bands. When the band width exceeds 0.5%, the stop-loss is set at the lower band; when it's less than 0.5%, the stop-loss is reduced to half the lower band range.

4. Entry Conditions: Breakout below the lower band serves as a long signal during an uptrend, and breakout above the upper band serves as a short signal during a downtrend.

5. Exit Conditions: For long positions, take profit when the price touches the upper Bollinger Band or the short-term MA. For short positions, take profit when touching the lower Bollinger Band or the short-term MA.

6. Stop-Loss Conditions: For long positions, stop out if the price drops below the dynamically adjusted lower band range. For short positions, stop out if the price rises above the dynamically adjusted upper band range.

### Strategy Advantages

1. The dual moving average system filters out market noise from non-trending or consolidating markets effectively.

2. The middle Bollinger Band acts as support/resistance, while the upper and lower bands serve as dynamic stop-loss levels, helping manage risk.

3. Adjusting the stop-loss magnitude according to Bollinger Band width lowers the probability of premature stop-outs and ensures logical stop placement.

4. Following the trend direction generally results in a higher win rate.

### Strategy Risks

1. Dual moving averages may produce frequent false breakouts, potentially missing trend reversal points. This can be mitigated by reducing the MA periods.

2. Bollinger Bands are susceptible to whipsaws in ranging markets. Reducing trade frequency can help avoid such situations.

3. Stop-losses placed too close to support/resistance levels are easily triggered. Widening the stop-loss range slightly can address this issue.

4. The strategy struggles to capture short-term retracements effectively. Shortening the holding period could help.

### Optimization Directions

1. Optimize the moving average periods to better suit specific market conditions.

2. Fine-tune the Bollinger Band multiplier to balance the likelihood of stop-loss triggers.

3. Integrate additional indicators for multi-factor validation to enhance signal accuracy.

4. Incorporate trading volume or momentum to confirm trends and prevent divergence-related losses.

5. Improve money management strategies, such as fixed fractional position sizing or fixed stop-loss amounts, to control per-trade risk.

6. Implement mechanisms to handle price shocks, such as large overnight gaps.

### Conclusion

Overall, this strategy is relatively stable, using dual moving averages for trend identification and Bollinger Bands for dynamic support/resistance and stop-loss placement. However, limitations include potential trend misjudgments and overly tight stop-losses. Future improvements could focus on optimizing the moving average system, stop-loss methodology, and capital management to make the strategy more robust across varying market environments. In summary, with its high win rate and attractive risk-reward profile, this strategy offers a straightforward and effective approach ideal for novice traders.

[/trans]

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Length|
|v_input_2|4|multiplier|
|v_input_3|60|Trend Time Frame|
|v_input_4|true|Use Trend Filter|
|v_input_5_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|

> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-18 00:00:00
end: 2023-10-24 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy(title="yuthavithi BB Scalper 2 strategy", overlay=true)

len = input(20, minval=1, title="Length")
multiplier = input(4, minval=1, title="multiplier")
trendTimeFrame = input(60, minval=1, title="Trend Time Frame")
useTrendFilter = input(true, type=bool, title = "Use Trend Filter")

src = input(close, title="Source")
out = sma(src, len)
//plot(out, title="SMA", color=blue)

stdOut = stdev(close, len)
bbUpper = out + stdOut * multiplier
bbLower = out - stdOut * multiplier
bbUpper2 = out + stdOut * (multiplier / 2)
bbLower2 = out - stdOut * (multiplier / 2)
bbUpperX2 = out + stdOut * multiplier * 2
bbLowerX2 = out - stdOut * multiplier * 2
bbWidth = (bbUpper - bbLower) / out


closeLongTerm = request.security(syminfo.tickerid, tostring(trendTimeFrame), close)
smaLongTerm = request.security(syminfo.tickerid, tostring(trendTimeFrame), sma(close,20))

//plot(smaLongTerm, color=red)

trendUp = useTrendFilter ? (closeLongTerm > smaLongTerm) : true
trendDown = useTrendFilter? (closeLongTerm < smaLongTerm) : true

bearish = ((cross(close,bbUpper2) == 1) or (cross(close,out) == 1)) and (close[1] > close) and trendDown
bullish = ((cross(close,bbLower2) == 1) or (cross(close,out) == 1)) and (close[1] < close) and trendUp


closeBuy = (high[1] > bbUpper[1]) and (close < bbUpper) and (close < open) and trendUp 
closeSell = (((low[1] < bbLower[1]) and (close > bbLower)) or ((low[2] < bbLower[2]) and (close[1] > bbLower[1]))) and (close > open) and trendDown


cutLossBuy = iff(bbWidth > 0.005, (low < bbLower) and (low[1] > bbLower[1]) and trendUp, (low < bbLowerX2) and (low[1] > bbLowerX2[1]) and trendUp)
cutLossSell = iff(bbWidth > 0.005, (high > bbUpper) and (high[1] < bbUpper[1]) and trendDown, (high > bbUpperX2) and (high[1] < bbUpperX2[1]) and trendDown)


if (bullish)
    strategy.entry("Buy", strategy.long, comment="Buy")

if (bearish)
    strategy.entry("Sell", strategy.short, comment="Sell")
    

strategy.close("Buy", closeBuy or cutLossBuy)
   
strategy.close("Sell", closeSell or cutLossSell)

```

> Detail

https://www.fmz.com/strategy/430149

> Last Modified

2023-10-25 15:00:20