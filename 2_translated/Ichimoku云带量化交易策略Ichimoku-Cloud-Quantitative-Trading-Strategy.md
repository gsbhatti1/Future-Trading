> Name

Ichimoku Cloud Quantitative Trading Strategy Ichimoku-Cloud-Quantitative-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/6a418e09b8e25a3301.png)
[trans]

### Overview

This strategy integrates multiple indicators such as Ichimoku cloud, K-line, Hull Moving Average, and MACD to build a long-short decision mechanism for automated trading.

### Strategy Logic  

It uses the conversion line and lagging line of Ichimoku cloud to generate trading signals. The trend direction is determined by the Hull Moving Average. The MACD indicator differentiates between longer and shorter cycles. Intraday K-line breakout provides entry signals.

The conversion line averages the mid-price of the last 9 days. The lagging line averages the mid-price of the last 26 days. Long positions are initiated when the conversion line crosses above the lagging line, and short positions are taken when it crosses below.

The Hull Moving Average uses a double averaging line crossover to define trends. An uptrend is determined when the fast line crosses above the slow line, and a downtrend in reverse.

MACD takes the difference between 12- and 26-period exponential moving averages (EMAs). Crosses on the zero line and signal line indicate long/short signals. 

Intraday K-line penetration of the lagging line provides entry timing.

### Advantages  

1. Accurate trend detection with multiple indicators.
2. Precise entry avoiding unnecessary trades.
3. Solid risk control with stop loss/take profit mechanisms.

### Risks

1. Aggressive entry with improper parameter tuning.
2. Increased complexity with multi-indicator usage.
3. Drawdowns inevitable for short-term trades.

### Enhancement Opportunities 

1. Optimize parameters for more products and timeframes.
2. Add machine learning for adaptive tuning.
3. Improve entry momentum for higher win rate.

### Summary  

This strategy combines Ichimoku cloud and other indicator signals into a complete quantitative system. Strict stop loss/take profit mechanisms control risks. With parameter adjustment and model optimization, it can be applied to more trading instruments with broad prospects.

||

### Overview

This strategy integrates multiple indicators such as Ichimoku cloud, K-line, Hull Moving Average, and MACD to build a long-short decision mechanism for automated trading.

### Strategy Logic  

It uses the conversion line and lagging line of Ichimoku cloud to generate trading signals. The trend direction is determined by the Hull Moving Average. The MACD indicator differentiates between longer and shorter cycles. Intraday K-line breakout provides entry signals.

The conversion line averages the mid-price of the last 9 days. The lagging line averages the mid-price of the last 26 days. Long positions are initiated when the conversion line crosses above the lagging line, and short positions are taken when it crosses below.

The Hull Moving Average uses a double averaging line crossover to define trends. An uptrend is determined when the fast line crosses above the slow line, and a downtrend in reverse.

MACD takes the difference between 12- and 26-period exponential moving averages (EMAs). Crosses on the zero line and signal line indicate long/short signals.

Intraday K-line penetration of the lagging line provides entry timing.

### Advantages  

1. Accurate trend detection with multiple indicators.
2. Precise entry avoiding unnecessary trades.
3. Solid risk control with stop loss/take profit mechanisms.

### Risks

1. Aggressive entry with improper parameter tuning.
2. Increased complexity with multi-indicator usage.
3. Drawdowns inevitable for short-term trades.

### Enhancement Opportunities 

1. Optimize parameters for more products and timeframes.
2. Add machine learning for adaptive tuning.
3. Improve entry momentum for higher win rate.

### Summary  

This strategy combines Ichimoku cloud and other indicator signals into a complete quantitative system. Strict stop loss/take profit mechanisms control risks. With parameter adjustment and model optimization, it can be applied to more trading instruments with broad prospects.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Double HullMA|
|v_input_2|0.001|Decision Threshold (0.001)|
|v_input_3|-500|Stop Loss in $|
|v_input_4|25000|Target Point in $|
|v_input_5|9|Conversion Line Periods|
|v_input_6|26|Base Line Periods|
|v_input_7|52|Lagging Span 2 Periods|
|v_input_8|26|Displacement|
|v_input_9|9|MACD_Length|
|v_input_10|12|MACD_fastLength|
|v_input_11|26|MACD_slowLength|


> Source (PineScript)

```pinescript
//@version=2
// Any timeFrame ok but good on 15 minute & 60 minute, Ichimoku + Daily-Candle_cross(DT) + HULL-MA_cross + MacD combination 420 special blend
strategy("Ichimoku + Daily-Candle_X + HULL-MA_X + MacD", shorttitle="٩(̾●̮̮̃̾•̃̾)۶", overlay=true, default_qty_type=strategy.percent_of_equity, max_bars_back=720, default_qty_value=100, calc_on_order_fills=true, calc_on_every_tick=true, pyramiding=0)
keh=input(title="Double HullMA",defval=14, minval=1)
dt = input(defval=0.0010, title="Decision Threshold (0.001)", type=float, step=0.0001)
SL = input(defval=-500.00, title="Stop Loss in $", type=float, step=1)
TP = input(defval=25000.00, title="Target Point in $", type=float, step=1)
ot=1
n2ma=2*wma(close,round(keh/2))
nma=wma(close,keh)
diff=n2ma-nma
sqn=round(sqrt(keh))
n2ma1=2*wma(close[1],round(keh/2))
nma1=wma(close[1],keh)
diff1=n2ma1-nma1
sqn1=round(sqrt(keh))
n1=wma(diff,sqn)
n2=wma(diff1,sqn)
b=n1>n2?lime:red
c=n1>n2?green:red
d=n1>n2?red:green
confidence=(request.security(syminfo.tickerid, 'D', close)-request.security(syminfo.tickerid, 'D', close[1]))/request.security(syminfo.tickerid, 'D', close[1])
conversionPeriods = input(9, minval=1, title="Conversion Line Periods")
basePeriods = input(26, minval=1, title="Base Line Periods")
laggingSpan2Periods = input(52, minval=1, title="Lagging Span 2 Periods")
displacement = input(26, minval=1, title="Displacement")
donchian(len) => avg(lowest(len), highest(len))
conversionLine = donchian(conversionPeriods)
baseLine = donchian(basePeriods)
leadLine1 = avg(conversionLine, baseLine)
leadLine2 = donchian(laggingSpan2Periods)
LS=close, offset = -displacement
MACD_Length = input(9)
MACD_fastLength = input(12)
MACD_slowLength = input(26)
MACD = ema(close, MACD_fastLength) - ema(close, MACD_slowLength)
aMACD = ema(MACD, MACD_Length)
closelong = n1<n2 and close<n2 and confidence<dt or strategy.openprofit<SL or strategy.openprofit>TP
if (closelong)
    strategy.close("Long")
closeshort = n1>n2 and close>n2 and confidence>dt or strategy.openprofit<SL or strategy.openprofit>TP
if (closeshort)
    strategy.close("Short")
longCondition = n1>n2 and strategy.opentrades<ot and confidence>dt and close>n2 and leadLine1>leadLine2 and open<LS and MACD>aMACD
if (longCondition)
    strategy.entry("Long",strategy.long)
shortCondition = n1<n2 and strategy.opentrades<ot and confidence<dt and close<n2 and leadLine1<leadLine2 and open>LS and MACD<aMACD
if (shortCondition)
    strategy.entry("Short")
```