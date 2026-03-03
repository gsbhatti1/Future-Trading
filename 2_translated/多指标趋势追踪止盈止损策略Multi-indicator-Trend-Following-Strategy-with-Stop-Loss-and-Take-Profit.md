> Name

Multi-indicator Trend Following Strategy with Stop Loss and Take Profit

> Author

ChaoZhang

> Strategy Description

### Strategy Overview

The multi-indicator trend following strategy with stop loss and take profit incorporates indicators like EMA, MACD, OBV, and PSAR to determine the trend direction, and sets stop loss and take profit after entering trades to control risks. It synthesizes multiple factors to confirm trading signals, while strictly managing the reward and risk of each trade when following trends.

### Strategy Logic

1. Determine trend direction: when EMA, MACD, OBV, and PSAR align to give bullish or bearish signals.
2. Entry rules: go long on bull signals, go short on bear signals.
3. Stop loss/take profit: set stop loss and take profit for each trade based on PSAR levels after entry.
4. Exit rules: close positions when stop loss or take profit is triggered.

The advantage of this strategy is using multiple indicators for high-probability signal generation, while the stop loss/take profit rules actively control risks while locking in profits. Indicator mix and parameter settings can be optimized based on market conditions.

### Advantages of the Strategy

- Multiple indicators combine for high-probability signals
- Stop loss/take profit actively controls risks
- Take profit/stop loss based on PSAR levels
- Flexible indicator and parameter optimization
- Sustained profits in trends

### Risk Warnings

- Complex multi-indicator combination
- Potential signal lag risks
- Watch out for reversals and ranges
- Constant parameter testing and optimization needed

### Conclusion

The multi-indicator trend following strategy with stop loss and take profit comprehensively improves trend trading by enhancing accuracy and actively managing risks. Through repetitive testing on different markets and parameters, it can be optimized into a robust and reliable quantitative system.

||

### Strategy Arguments

|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Short Length OBV|
|v_input_2|8|Long Length OBV|
|v_input_3|0.1|PSAR START|
|v_input_4|0.05|PSAR INC|
|v_input_5|0.3|PSAR MAX|
|v_input_6|200|Length EMA|
|v_input_7_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_8|12|Fast Length MACD|
|v_input_9|25|Slow Length MACD|
|v_input_10_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_11|9|Signal Smoothing MACD|
|v_input_12|true|Simple MA (Oscillator)|
|v_input_13|true|Simple MA (Signal Line)|
|v_input_14|true|longEntry|
|v_input_15|true|shortEntry|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-08-15 00:00:00
end: 2023-09-14 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © exlux99

//@version=4

strategy("Scalping Forex full strategy with risk management", overlay=true, initial_capital=10000, default_qty_type=strategy.percent_of_equity, default_qty_value=100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.cash_per_contract, commission_value=0.00005)

// VOLUME
shortlen = input(1, minval=1, title="Short Length OBV")
longlen = input(8, minval=1, title="Long Length OBV")
upColor = #2196F3 // input(#2196F3, "Color Up")
dnColor = #6B1599 // input(#6B1599, "Color Down")
f_normGradientColor(_series, _crossesZero, _colorNormLen, _dnColor, _upColor) =>
    _dnValue = _crossesZero ? -100 : 0
    _mult = 0.0
    _lowest = lowest(_colorNormLen)
    _highest = highest(_colorNormLen)
    _diff1 = close - _lowest
    _diff2 = _highest - _lowest
    if _diff2 > 0
        _mult := _diff1 / _diff2 * 100
    color.from_gradient(sign(_series) * _mult, _dnValue, 100, _dnColor, _upColor)
shorta = ema(volume, shortlen)
longa = ema(volume, longlen)
osc = 100 * (shorta - longa) / longa

start = input(0.1, title="PSAR START")
increment = input(0.05, title="PSAR INC")
maximum = input(0.3, title="PSAR MAX")
// multitp = input(1)
// multisl = input(1)
var bool uptrend = na
var float EP = na
var float SAR = na
var float AF = start
var float nextBarSAR = na
if bar_index > 0
    firstTrendBar = false
    SAR := nextBarSAR
    if bar_index == 1
        float prevSAR = na
        float prevEP = na
        lowPrev = low[1]
        highPrev = high[1]
        closeCur = close
        closePrev = close[1]
        if closeCur > closePrev
            uptrend := true
            EP := high
            prevSAR := lowPrev
            prevEP := high
        else
            uptrend := false
            EP := low
            prevSAR := highPrev
            prevEP := low
        firstTrendBar := true
        SAR := prevSAR + start * (prevEP - prevSAR)
    if uptrend
        if SAR > low
            firstTrendBar := true
            uptrend := false
            SAR := max(EP, high)
            EP := low
            AF := start
    else
        if SAR < high
            firstTrendBar := true
            uptrend := true
            SAR := min(EP, low)
            EP := high
            AF := start
    if not firstTrendBar
        if uptrend
            if high > EP
                EP := high
                AF := min(AF + increment, maximum)
```