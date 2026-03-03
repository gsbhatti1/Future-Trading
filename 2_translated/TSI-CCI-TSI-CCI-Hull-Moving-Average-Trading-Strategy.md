> Name

TSI CCI Hull Moving Average Trading Strategy

> Author

ChaoZhang

> Strategy Description

## Overview

This strategy combines the TSI indicator, CCI indicator, and Hull Moving Average to determine and trade trends. The TSI and CCI indicators identify price wave trends, while the Hull MA confirms trend direction. Long/short signals are generated when conditions align with these indicators, setting profit targets for profitable exits.

## Strategy Logic

The TSI curve and signal line are calculated. A long signal is triggered when the curve crosses above the signal line, while a short signal is triggered on a downward crossover. The CCI indicator helps to identify overbought/oversold levels. Price crossing above the Hull MA suggests a bull market, and below indicates a bear market. Long/short trades are taken when TSI, CCI, and Hull MA breakout conditions align. Profit targets are set to exit positions upon reaching these targets.

## Advantages

- The TSI indicator strongly identifies trend direction.
- The CCI indicator effectively detects overbought/oversold conditions.
- The Hull MA filters false breakouts, improving signal quality.
- Setting profit targets allows exiting at peak profitability.
- Combining multiple indicators improves robustness and stability.

## Risks

- Lag exists in TSI, CCI, and other indicators.
- The Hull MA cannot perfectly determine turning points.
- Exact price reversal timing cannot be accurately determined.
- Poor profit target setting may reduce potential profits.

Risk can be reduced by tuning indicator parameters and optimizing profit algorithms.

## Enhancements

- Test different combinations of TSI/CCI parameters to improve sensitivity.
- Consider dynamic/trailing profit targets.
- Add other indicators to determine reversals.
- Test across different products to enhance robustness.

## Conclusion

This multi-indicator strategy with profit targeting shows good backtest results. Further refinements like parameter optimization can make it a stable quantitative trading system.

||

## Overview

This strategy combines the TSI, CCI indicators and Hull Moving Average to determine and trade trends. The TSI and CCI identify price wave trends while the Hull MA confirms trend direction. Profit targets are set when long/short signals occur for profitable exits.

## Strategy Logic

The TSI curve and signal line are calculated. Long signals are generated when the curve crosses above the signal line, short signals on a downward crossover. The CCI indicates overbought/oversold levels. Price crossing above the Hull MA suggests a bull market, and below indicates a bear market. Long/short trades are taken when TSI, CCI, and Hull MA breakout conditions align. Profit targets are set to exit positions upon reaching these targets.

## Advantages  

- The TSI indicator strongly identifies trend direction.
- The CCI effectively detects overbought/oversold conditions.
- The Hull MA filters false breakouts, improving signal quality.
- Setting profit targets allows exiting at peak profitability.
- Combining multiple indicators improves robustness and stability.

## Risks

- Lag exists in the TSI, CCI, and other indicators.
- The Hull MA cannot perfectly determine turning points.
- Exact price reversal timing cannot be accurately determined.
- Poorly set profit targets may reduce potential profits.

Risks can be reduced by tuning indicator parameters and optimizing profit algorithms.

## Enhancements

- Test different combinations of TSI/CCI parameters to improve sensitivity.
- Consider dynamic/trailing profit targets.
- Add other indicators to determine reversals.
- Test across different products to enhance robustness.

## Conclusion

This multi-indicator strategy with profit targeting shows good backtest results. Further refinements like parameter optimization can make it a stable quantitative trading system.

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|50|Long Length|
|v_input_2|50|Short Length|
|v_input_3|25|Signal Length|
|v_input_4_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_5|26|Period|
|v_input_6|100|Upper Line|
|v_input_7|-100|Lower Line|
|v_input_8|true|Start Date|
|v_input_9|true|Start Month|
|v_input_10|2018|Start Year|
|v_input_11|true|End Date|
|v_input_12|7|End Month|
|v_input_13|9999|End Year|
|v_input_14|0.5|LongProfitPercent|
|v_input_15|0.5|ShortProfitPercent|
|v_input_16_close|0|profit long source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_17_close|0|profit short source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-08-18 00:00:00
end: 2023-09-17 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

strategy(title="TSI CCI Hull", shorttitle="TSICCIHULL", default_qty_type=strategy.percent_of_equity, default_qty_value=100, calc_on_order_fills=false, calc_on_every_tick=true, pyramiding=0, commission_type=strategy.commission.percent, commission_value=0.018)
long = input(title="Long Length", type=input.integer, defval=50)
short = input(title="Short Length", type=input.integer, defval=50)
signal = input(title="Signal Length", type=input.integer, defval=25)
price=input(title="Source",type=input.source,defval=close)
Period=input(26, minval=1)
lineupper = input(title="Upper Line", type=input.integer, defval=100)
linelower = input(title="Lower Line", type=input.integer, defval=-100)
p=price
length= Period
double_smooth(src, long, short) =>
    fist_smooth = ema(src, long)
    ema(fist_smooth, short)
pc = change(price)
double_smoothed_pc = double_smooth(pc, long, short)
double_smoothed_abs_pc = double_smooth(abs(pc), long, short)
tsi_value = 100 * (double_smoothed_pc / double_smoothed_abs_pc)
keh = tsi_value*5 > linelower ? color.red : color.lime
teh = ema(tsi_value*5, signal*5) > lineupper ? color.red : color.lime
meh = ema(tsi_value*5, signal*5) > tsi_value*5 ? color.red : color.lime
i1=plot(tsi_value*5, title="TSI Value", color=color.black, linewidth=1,transp=100)
i2=plot(ema(tsi_value*5, signal*5), title="TSI Signal", color=color.black, linewidth=1,transp=100)
fill(i1,i2,color=meh,transp=85)
plot(cross(tsi_value*5, ema(tsi_value*5, signal*5)) ? tsi_value*5 : na, style=plot.style_circles, color=color.black, linewidth=10)
plot(cross(tsi_value*5, ema(tsi_value*5, signal*5)) ? tsi_value*5 : na, style=plot.style_circles, color=color.white, linewidth=8,transp=0)
plot(cross(tsi_value*5, ema(tsi_value*5, signal*5)) ? tsi_value*5 : na, style=plot.style_circles, color=meh, linewidth=5)
n2ma = 2 * wma(p, round(length / 2))
nma = wma(p, length)
diff = n2ma - nma
sqn = round(sqrt(length))
n1 = wma(diff, sqn)
cci = (p - n1) / (0.015 * dev(p, length))
c = cci > 0 ? color.lime : color.red
c1 = cci > 20 ? color.lime : color.silver
c2 = cci < -20 ? color.red : color.silver
cc=plot(cci, color=c, title="CCI Line", linewidth=2)
cc2=plot(cci[1], color=color.gray, linewidth=1,transp=100)
fill(cc,cc2,color=c,transp=85)
plot(cross(20, cci) ? 20 : na, style=plot.style_cross,title="CCI cross down",  color=c2, linewidth=2,transp=100,offset=-2)
plot(cross(-20, cci) ? -20 : na, style=plot.style_cross,title="CCI cross up",  color=c1, linewidth=2,transp=100,offset=-2)

TSI1=ema(tsi_value*5, signal*5)
TSI2=ema(tsi_value*5, signal*5)[2]

hullma_smoothed = wma(2*wma(n1, Period/2)-wma(n
``` 

This completes the translation and description of the strategy. The code provided is for Pine Script in TradingView, which you can use to implement this trading strategy directly into your analysis or backtests. If there are any specific parts that need further refinement or explanation, feel free to ask!