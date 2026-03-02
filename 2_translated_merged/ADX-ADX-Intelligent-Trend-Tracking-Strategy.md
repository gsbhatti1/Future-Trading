> Name

ADX Intelligent Trend Tracking Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1045022a6c7c839ea8c.png)
[trans]

## Overview

The ADX Intelligent Trend Tracking Strategy uses the Average Directional Index (ADX) to judge the strength of trends, capturing trends when they are weak and following strong trends for profit. This strategy combines trend strength assessment with price breakouts to generate trading signals, making it a type of trend-following strategy.

## Strategy Logic

This strategy primarily relies on the Average Directional Index (ADX) to assess current trend strength. ADX calculates the average value of the DIRECTIONAL INDICATOR over a specific period to indicate trend strength. When the ADX value falls below a set threshold, we consider the market to be consolidating. At this point, a box range is established; if the price breaks out of the upper or lower boundary of this box, a trading signal is generated.

Specifically, the strategy first calculates the 14-period ADX value. If it's below 18, the trend is considered weak. Then, it determines the box range formed by the highest high and lowest low over the past 20 candles. When the price breaks through this box, buy and sell signals are triggered. The stop-loss distance is set at 50% of the box size, while the take-profit distance is 100% of the box size.

By combining trend strength judgment with breakout signals, this strategy captures trends during consolidation phases and avoids frequent trades in choppy markets. During strong trends, the larger take-profit range allows for greater profits.

## Strategy Advantages

1. Incorporating trend strength judgment helps avoid excessive trading in non-trending markets.
2. The box breakout adds filtering to prevent being caught in sideways movements.
3. Provides greater profit-taking opportunities during trending periods.
4. Customizable ADX parameters, box settings, and stop-loss/take-profit multipliers allow adaptation to various instruments.

## Strategy Risks

1. Incorrect ADX parameter settings may result in missed trends or false signals.
2. Box range that is too wide or narrow can negatively impact performance.
3. Poorly configured stop-loss and take-profit multipliers might lead to premature exits or insufficient protection.

Optimization can be achieved by adjusting ADX parameters, box lookback periods, and stop-loss/take-profit coefficients to better suit different assets and market conditions. Strict risk management is crucial—controlling per-trade loss percentages prevents significant drawdowns.

## Optimization Directions

1. Test different ADX calculation periods for improved sensitivity.
2. Experiment with varying box lookback windows to find optimal range sizes.
3. Fine-tune stop-loss and take-profit multipliers to enhance risk-reward ratios.
4. Evaluate unidirectional trading (long-only or short-only) effectiveness.
5. Integrate additional indicators such as volume metrics for confirmation.

## Conclusion

Overall, the ADX Intelligent Trend Tracking Strategy offers a relatively stable approach to trend following. By integrating both trend strength analysis and price breakout signals, it mitigates common pitfalls like buying highs and selling lows often seen in traditional trend followers. With proper parameter tuning and disciplined capital management, this strategy can deliver consistent returns.

[/trans]

> Strategy Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| v_input_1 | 14 | (?ADX Settings) ADX Smoothing Period |
| v_input_2 | 14 | ADX Period |
| v_input_3 | 18 | ADX Lower Level |
| v_input_4 | 20 | (?BreakoutBox) BreakoutBox Lookback Period |
| v_input_5 | true | (?Take Profit and Stop Loss) Profit Target Box Width Multiple |
| v_input_6 | 0.5 | Stop Loss Box Width Multiple |
| v_input_7 | false | (?Trade Direction) Both(0), Long(1), Short(-1) |

> Source (PineScript)

```pinescript
/*backtest
start: 2023-11-20 00:00:00
end: 2023-11-27 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//Developer: Andrew Palladino. 
//Creator: Rob Booker.
//Date: 9/29/2017
//@version=5
//Date: 08/10/2022
//Updated to V5 from V1, default cash settings added and indicators made more easily visible by:
// @ Powerscooter

strategy("Rob Booker - ADX Breakout", shorttitle="ADX Breakout V5", overlay=true, default_qty_type = strategy.cash, default_qty_value = 100000, initial_capital = 100000)

adxSmoothPeriod = input(14, title="ADX Smoothing Period", group = "ADX Settings")
adxPeriod = input(14, title="ADX Period", group = "ADX Settings")
adxLowerLevel = input(18, title="ADX Lower Level", group = "ADX Settings")
boxLookBack = input(20, title="BreakoutBox Lookback Period", group = "BreakoutBox")
profitTargetMultiple = input(1.0, title="Profit Target Box Width Multiple", group = "Take Profit and Stop Loss")
stopLossMultiple = input(0.5, title="Stop Loss Box Width Multiple", group = "Take Profit and Stop Loss")
enableDirection = input(0, title="Both(0), Long(1), Short(-1)", group = "Trade Direction")


// When the ADX drops below threshold limit, then we consider the pair in consolidation. 
// Set Box around highs and lows of the last 20 candles. with upper and lower boundaries. 
// When price breaks outside of box, a trade is taken. (on close or on touch?)
// Stop is placed, default 50%, of the size of the box. So if box is 200 pips, stop is at 100 pips. 
// Profit target is 100% of the size of the box. Default. User can set a profit target of 0.5, 1 full size, 2 or 3. 


dirmov(len) =>
	up = ta.change(high)
	down = -ta.change(low)
	truerange = ta.rma(ta.tr, len)
	plus = fixnan(100 * ta.rma(up > down and up > 0 ? up : 0, len) / truerange)
	minus = fixnan(100 * ta.rma(down > up and down > 0 ? down : 0, len) / truerange)
	[plus, minus]

adx(dilen, adxlen) => 
	[plus, minus] = dirmov(dilen)
	sum = plus + minus
	adx = 100 * ta.rma(math.abs(plus - minus) / (sum == 0 ? 1 : sum), adxlen)

adxHigh(dilen, adxlen) => 
	[plus, minus] = dirmov(dilen)
	plus
	
adxLow(dilen, adxlen) => 
	[plus, minus] = dirmov(dilen)
	minus
	
sig = adx(adxSmoothPeriod, adxPeriod)
//sigHigh = adxHigh(dilen, adxlen)
//sigLow = adxLow(dilen, adxlen)

isADXLow = sig < adxLowerLevel

//boxUpperLevel = ta.highest(high, boxLookBack)[1]
//boxLowerLevel = ta.lowest(low, boxLookBack)[1]

var float boxUpperLevelCarry = 0
var float boxLowerLevelCarry = 0

boxUpperLevel = strategy.position_size == 0 ? ta.highest(high, boxLookBack)[1] : boxUpperLevelCarry
boxUpperLevelCarry := boxUpperLevel
boxLowerLevel = strategy.position_size == 0 ? ta.lowest(low, boxLookBack)[1] : boxLowerLevelCarry
boxLowerLevelCarry := boxLowerLevel

boxWidth = boxUpperLevel - boxLowerLevel

profitTarget = strategy.position_size > 0  ? strategy.position_avg_price + profitTargetMultiple*boxWidth : strategy.position_size < 0 ?  strategy.position_avg_price - profitTargetMultiple*boxWidth : na
stopLoss = strategy.position_size > 0 ? strategy.position_avg_price - stopLossMultiple*boxWidth : strategy.position_size < 0 ? strategy.position_avg_price + stopLossMultiple*boxWidth : na

plot(strategy.position_size == 0 ? boxUpperLevel : na, color=color.white, style = plot.style_linebr)
plot(strategy.position_size == 0 ? boxLowerLevel : na, color=color.white, style = plot.style_linebr)


bgcolor(isADXLow ? color.purple : na, transp=72, title = "ADX limit")
plot(stopLoss, color=color.red, linewidth=2, style = plot.style_linebr, title="StopLossLine")
plot(profitTarget, color=color.blue, linewidth=2, style = plot.style_linebr, title="ProfitTargetLine")

isBuyValid = strategy.position_size == 0 and ta.cross(close, boxUpperLevel) and isADXLow

//Long Entry Condition
strategy.exit("close_long", from_entry="open_long", limit = profitTarget, stop = stopLoss)
if isBuyValid and strategy.opentrades == 0 and (enableDirection == -1 or enableDirection == 0)
    strategy.entry("open_long", strategy.long)

isSellValid = strategy.position_size == 0 and ta.cross(close, boxLowerLevel) and isADXLow

//Short Entry condition
strategy.exit(id="close_short", from_entry="open_short", limit = profitTarget, stop = stopLoss)
if isSellValid and strategy.opentrades == 0 and (enableDirection == 1 or enableDirection == 0)
    strategy.entry("open_short", strategy.short)
```

> Detail

https://www.fmz.com/strategy/433545

> Last Modified

2023-11-28 14:04:00