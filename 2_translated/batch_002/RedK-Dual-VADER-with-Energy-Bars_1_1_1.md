> Name

RedK-Dual-VADER-with-Energy-Bars

> Author

ChaoZhang

> Strategy Description

The visual improvements I added in VADER-DEB help bring more insight into market action by:
1) exposing the dual/long VADER plot by default (which we use as a proxy for sentiment) - and it now shows as an area instead of a histogram. You can still hide the sentiment plot in indicator settings.
2) using directional "energy bars" (instead of energy lines in v3.0). Optional Red/Green DER Lines are available in study settings and are hidden by default.

So this is Dual VADER with Energy Bars, or VADER-DEB for short.

These changes may be considered small by some, but I found them to be more visually appealing and better for "driving action" - This works better for me as a visual person - so I thought to share with others who may be like me. That's why I decided to publish this as a separate version and not as an update to the existing indicator - so you can make the choice which one you prefer to use.

There is no change in the core calculation within the code. As shown by the chart above where we compare both VADER versions side-by-side.

If you're happy with VADER v3.0, please feel free to continue using it.

Good luck!

**backtest**
 ![IMG](https://www.fmz.com/upload/asset/18a93e656d65507c1cf.png) 

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_int_1|10|length|
|v_input_int_2|5|(?Directional Energy Ratio)Average|
|v_input_string_1|0|DER MA type: WMA|EMA|SMA|
|v_input_int_3|3|Smooth|
|v_input_bool_1|true|Sentiment|
|v_input_int_4|20|Length|
|v_input_string_2|0|(?Volume Parameters)Calculation: Relative|Full|None|
|v_input_int_5|20|Lookback (for Relative)|


> Source (PineScript)

```pinescript
/*backtest
start: 2022-04-23 00:00:00
end: 2022-05-22 23:59:00
period: 45m
basePeriod: 5m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © RedKTrader

//@version=5
indicator('RedK Dual VADER with Energy Bars [VADER-DEB]', 'RedK VADER-DEB v4.0', precision=0, timeframe='', timeframe_gaps=false)

// This version is the same as VADER v3.0 with enhanced visuals, using Energy Bars instead of positive/energy lines.
// The sentiment plot has been changed from a histogram to an area and is exposed by default (hence Dual w/ Energy Bars -- DEB).
// There are no changes in the core calculations from VADER v3.0 -- that's why I'll just call it VADER v4.0.

// ***********************************************************************************************************
// Choose volume calculation method.. Relative vs full.
// Relative magnifies the effect of recent volume spikes (up or down).
f_RelVol(_value, _length) =>
    min_value = ta.lowest(_value, _length)
    max_value = ta.highest(_value, _length)
    ta.stoch(_value, max_value, min_value, _length) / 100
// ***********************************************************************************************************

// ***********************************************************************************************************
// Choose MA type for the base DER calculation..
// WMA is my preference and is default.. SMA is really slow and lags a lot - but added for comparison.
f_derma(_data, _len, MAOption) =>
    value = 
      MAOption == 'SMA' ? ta.sma(_data, _len) :
      MAOption == 'EMA' ? ta.ema(_data, _len) :
      ta.wma(_data, _len)
// ***********************************************************************************************************

// ===========================================================================================================
//      Inputs
// ===========================================================================================================

price   = close
length  = input.int(10, minval=1)
DER_avg = input.int(5, 'Average', minval=1, inline='DER', group='Directional Energy Ratio')
MA_Type = input.string('WMA', 'DER MA type', options=['WMA', 'EMA', 'SMA'], inline='DER', group='Directional Energy Ratio') 
smooth  = input.int(3, 'Smooth', minval=1,  inline='DER_1', group='Directional Energy Ratio')

show_senti = input.bool(true, 'Sentiment',  inline='DER_s', group='Directional Energy Ratio')
senti   = input.int(20, 'Length', minval=1, inline='DER_s', group='Directional Energy Ratio')

v_calc  = input.string('Relative', 'Calculation', options=['Relative', 'Full', 'None'], group='Volume Parameters')
vlookbk = input.int(20, 'Lookback (for Relative)', minval=1,                            group='Volume Parameters')

// ===========================================================================================================
//          Calculations
// ===========================================================================================================

// Volume Calculation Option -- will revert to no volume acceleration for instruments with no volume data.
vola    = 
  v_calc == 'None' or na(volume) ? 1 : 
  v_calc == 'Relative' ? f_RelVol(volume, vlookbk) : 
  volume

R       = (ta.highest(2) - ta.lowest(2)) / 2                    // R is the 2-bar average bar range -- this method accommodates bar gaps
sr      = ta.change(price) / R                                  // calc ratio of change to R
rsr     = math.max(math.min(sr, 1), -1)                         // ensure ratio is restricted to +1/-1 in case of big moves
c       = fixnan(rsr * vola)                                    // add volume accel -- fixnan addresses cases where no price change between bars

c_plus  = math.max(c, 0)                                        // calc directional vol-accel energy
c_minus = -math.min(c, 0)

// plot(c_plus)
// plot(c_minus)


avg_vola    = f_derma(vola, length, MA_Type)
dem         = f_derma(c_plus, length, MA_Type)  / avg_vola          // directional energy ratio
sup         = f_derma(c_minus, length, MA_Type) / avg_vola

adp         = 100 * ta.wma(dem, DER_avg)
```