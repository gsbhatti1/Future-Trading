<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

RSI Range Breakout Strategy

> Author

ChaoZhang

> Strategy Description

[trans]

## Overview

The RSI range breakout strategy is a typical trend-following strategy. It uses the Relative Strength Index (RSI) as the primary technical indicator to identify opportunities for entering positions when RSI is in overbought or oversold conditions, aiming to track trending movements.

## Strategy Logic  

This strategy primarily relies on the RSI indicator to judge overbought and oversold market states. The RSI calculation formula is: RSI = (Average Gain / (Average Gain + Average Loss)) × 100. Here, Average Gain represents the simple moving average of upward price changes over the past N days, while Average Loss is the simple moving average of downward price changes during that period.

When RSI exceeds the predefined overbought level (default 80), it suggests an overbought market condition; when RSI falls below the defined oversold threshold (default 35), it indicates an oversold market. The strategy seeks shorting opportunities when RSI breaks below the overbought line and looks for long entries when RSI moves above the oversold zone.

Specifically, the strategy employs two SMA lines to assess the trend direction of the RSI indicator. A buy signal occurs when the fast SMA crosses above the slow SMA simultaneously with RSI breaking out from the oversold region. Conversely, a sell signal arises when the fast SMA crosses below the slow SMA along with RSI breaching the overbought level. Additionally, stop-loss and take-profit levels are established to manage risk effectively.

## Advantages

- Uses RSI to detect overbought/oversold conditions, offering some trend identification capability
- Combines dual SMA filtering to reduce false breakouts caused by RSI oscillations
- Incorporates stop-loss and take-profit mechanisms to limit individual trade losses
- Entry via breakout avoids excessive whipsaw trading

## Risks and Mitigation Strategies

- RSI lag may cause missing key turning points in trends
  - Fine-tune RSI parameters to improve responsiveness
- Improperly set thresholds can hinder profitability
  - Adjust parameters based on specific market characteristics
- Tight stop-losses might get triggered prematurely due to overnight volatility
  - Increase stop-loss distances slightly to prevent premature exits
- Small profit targets fail to capture full trend potential
  - Dynamically adjust take-profit levels according to prevailing market volatility

## Optimization Directions

- Integrate additional indicators like KDJ or MACD to refine entry timing and counteract RSI's inherent lag
- Implement higher time-frame trend analysis to avoid counter-trend trades
- Enhance exit strategies using dynamic stops such as trailing stops or adaptive profit-taking methods
- Customize parameter configurations per asset class to suit distinct market behaviors
- Develop robust position sizing models incorporating pyramiding or scaling techniques

## Conclusion

Overall, the RSI range breakout strategy serves as a classic example of trend-following methodology. By leveraging RSI for signal generation, applying SMA crossovers for noise reduction, and employing disciplined risk controls, this approach aims to capitalize on sustained directional moves. However, its effectiveness hinges upon appropriate parameter calibration and addressing RSI’s known limitations through strategic enhancements.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|3|RSI Length|
|v_input_2|35|Threshold Low|
|v_input_3|80|Threshold High|
|v_input_4|3|RSI Smoothing 1|
|v_input_5|5|RSI Smoothing 2|
|v_input_6|0.026|Stop loss %|
|v_input_7|300|Take Profit Points|
|v_input_8|true|Long only?|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-10 00:00:00
end: 2023-10-10 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

//strategy("Strategy RSI | Fadior", shorttitle="Strategy RSI", pyramiding=10, calc_on_order_fills=false, initial_capital=10000, default_qty_type=strategy.percent_of_equity, currency="USD", default_qty_value=100, overlay=false)
 
len = input(3, minval=1, title="RSI Length") 
threshLow = input(title="Threshold Low", defval=35)
threshHigh = input(title="Threshold High", defval=80)
rsiLength1 = input(title="RSI Smoothing 1", defval=3)
rsiLength2 = input(title="RSI Smoothing 2", defval=5)
SL = input(title="Stop loss %", type=float, defval=.026, step=.001)
TP = input( defval=300)

// 3 40 70 2
// 14 40 70 2 16 0.05 50

src = close
  
up = rma(max(change(src), 0), len)
down = rma(-min(change(src), 0), len)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))

plot(sma(rsi,rsiLength2), color=orange)
plot(sma(rsi,rsiLength1), color=green)

band1 = hline(threshHigh)
band0 = hline(threshLow)
fill(band1, band0, color=purple, transp=90)

strategy = input(type=bool, title="Long only ?", defval=true)
strategy.risk.allow_entry_in(strategy ? strategy.direction.long : strategy.direction.all)

longCondition = sma(rsi,rsiLength1) < threshLow and sma(rsi,rsiLength2) > sma(rsi,rsiLength2)[1] 

if (longCondition)
    strategy.entry("Long", strategy.long) //, qty=10)
    strategy.exit("Close Long", "Long", stop=src-close*SL, profit=TP)
    
shortCondition = sma(rsi,rsiLength1) > threshHigh and sma(rsi,rsiLength2) < sma(rsi,rsiLength2)[1]
if (shortCondition)
    strategy.entry("Short", strategy.short) //, qty=10)
    strategy.exit("Close Short", "Short") //, stop=src-close*SL, profit=TP)

```

> Detail

https://www.fmz.com/strategy/428981

> Last Modified

2023-10-11 15:54:11