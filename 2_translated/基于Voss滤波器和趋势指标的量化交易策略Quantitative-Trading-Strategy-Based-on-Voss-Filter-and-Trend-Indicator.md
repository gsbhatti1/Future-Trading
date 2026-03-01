```pinescript
/*backtest
start: 2023-08-19 00:00:00
end: 2023-09-18 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"FutuOpenD","currency":"BTCUSD"}]
*/

//@version=5
indicator("Quantitative-Trading-Strategy-Based-on-Voss-Filter-and-Trend-Indicator", overlay=true)

// Strategy Arguments
v_input_1_close = input(close, title="Source")
v_input_2 = input(20, title="Period")
v_input_3 = input(4, title="Predict")
v_input_4 = input(0.25, title="Bandwidth")
v_input_5_hl2 = input(false, title="IT Source: hl2")
v_input_6 = input(0.07, title="Alpha")
v_input_7 = input(false, title="Fill Trend Region")
v_input_8 = input(false, title="Enable barcolors")
v_input_9 = input(false, title="Hide Ribbon")
v_input_10 = input(true, title="Custom Backtesting Dates")
v_input_11 = input(2019, title="Backtest Start Year")
v_input_12 = input(true, title="Backtest Start Month")
v_input_13 = input(true, title="Backtest Start Day")
v_input_14 = input(false, title="Backtest Start Hour")
v_input_15 = input(2020, title="Backtest Stop Year")
v_input_16 = input(2, title="Backtest Stop Month")
v_input_17 = input(29, title="Backtest Stop Day")
v_input_18 = input(false, title="Backtest Stop Hour")

// Voss Filter
_s1 = 0.5
_s2 = 0.4
_s3 = 0.6
_f1 = v_input_2
_x1 = close - open[1]
_x2 = v_input_4
_sumC = v_input_18 ? (v_input_17 + 1) * _x1 / 2 : 0

_filt = 0.5 * _s3 * _x1 + _f1 * _s2 * _filt[1] - _s1 * _filt[2]
_voss = _x2 * _filt - _sumC

// Instantaneous Trendline Indicator
_a = v_input_6
_src = close

_it = (_a-((_a*_a)/4.0))*_src+0.5*_a*_a*_src[1]-(_a-0.75*_a*_a)*_src[2]+2*(1-_a)*nz(_it[1])+-(1-_a)*(1-_a)*nz(_it[2])

// Strategy Logic
buySignal = _voss > 0 and crossover(_voss, _filt)
sellSignal = _voss < 0 and crossunder(_voss, _filt)

if (buySignal)
    strategy.entry("Buy", strategy.long)

if (sellSignal)
    strategy.close("Buy")

// Plotting
plot(_voss, title="Voss Filter", color=color.blue)
plot(_it, title="Instantaneous Trendline", color=color.red)
```