> Name

RedK-Volume-Accelerated-Directional-Energy-Ratio

> Author

ChaoZhang

> Strategy Description

The Volume-Accelerated Directional Energy Ratio (VADER) utilizes price movements and the associated volume to estimate the positive (buying) and negative (selling) "energy" behind market action, enabling traders to gain more detailed insights into market behavior and adjust their trading decisions accordingly.

How does VADER work?
------------------------------------
I have always been a fan of technical analysis concepts that are simple and integrate both price action and volume together. The concept behind VADER is really quite straightforward.

Let's walk through it without getting too technical:
- Large price moves accompanied by large volume indicate serious buyers (if the move is up) or sellers (if the move is down), who are "in control" of the market.
- Small price moves with large volume suggest a fight or balance of energy between buying and selling forces.
- Large price moves with limited volume imply a lack of "energy" from either buyers or sellers, and such moves are usually short-lived.

The analogy with VADER is that we look at price changes (difference in closing prices over two bars) as the displacement (or action result), and the associated volume as the "effort" behind this action. Combining these two values gives us a representation or proxy of the underlying energy (in a specific direction). When both values are high, the resulting energy is high; if one of them is low, the resulting energy is low.

We then calculate an average of that relative energy in each direction (positive = buying and negative = selling) to determine the net energy. Note that we approach this analogy from a trading perspective rather than a physics perspective—any differences in how energy is calculated in physics are understandable.


**Backtest**

![IMG](https://www.fmz.com/upload/asset/130a0f8baab4c18b768.jpg)

> Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_int_1 | 9 | Length |
| v_input_int_2 | 5 | (Directional Energy Ratio) Average |
| v_input_string_1 | 0 | DER MA type: WMA, EMA, SMA |
| v_input_int_3 | 3 | Smooth |
| v_input_bool_1 | false | Sentiment |
| v_input_int_4 | 20 | Length |
| v_input_string_2 | 0 | (Volume Parameters) Calculation: Relative, Full, None |
| v_input_int_5 | 10 | Lookback (for Relative) |

> Source (PineScript)

```pinescript
/* backtest
start: 2022-04-17 00:00:00
end: 2022-05-16 23:59:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © RedKTrader

//@version=5
indicator('RedK Volume-Accelerated Directional Energy Ratio', 'RedK VADER v3.0', precision=0, timeframe='', timeframe_gaps=false)

// ***********************************************************************************************************
// Choose volume calculation method.. Relative vs full.
// Relative magnifies effect of recent volume spikes (up or down)
f_RelVol(_value, _length) =>
    min_value = ta.lowest(_value, _length)
    max_value = ta.highest(_value, _length)
    ta.stoch(_value, max_value, min_value, _length) / 100
// ***********************************************************************************************************

// ***********************************************************************************************************
// Choose MA type for the base DER calculation..
// WMA is my preference and is default .. SMA is really slow and lags a lot - but added for comparison
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
length  = input.int(9, minval=1)
DER_avg = input.int(5, 'Average', minval=1, inline='DER', group='Directional Energy Ratio')
MA_Type = input.string('WMA', 'DER MA type', options=['WMA', 'EMA', 'SMA'], inline='DER', group='Directional Energy Ratio') 
smooth  = input.int(3, 'Smooth', minval=1,  inline='DER_1', group='Directional Energy Ratio')

show_senti = input.bool(false, 'Sentiment',  inline='DER_s', group='Directional Energy Ratio')
senti   = input.int(20, 'Length', minval=1, inline='DER_s', group='Directional Energy Ratio')

v_calc  = input.string('Relative', 'Calculation', options=['Relative', 'Full', 'None'], group='Volume Parameters')
vlookbk = input.int(10, 'Lookback (for Relative)', minval=1,                            group='Volume Parameters')

// ===========================================================================================================
//          Calculations
// ===========================================================================================================

// Volume Calculation Option -- will revert to no volume acceleration for instruments with no volume data
vola    = 
  v_calc == 'None' or na(volume) ? 1 : 
  v_calc == 'Relative' ? f_RelVol(volume, vlookbk) : 
  volume

R       = (ta.highest(2) - ta.lowest(2)) / 2                    // R is the 2-bar average bar range - this method accommodates bar gaps
sr      = ta.change(price) / R                                  // calc ratio of change to R
rsr     = math.max(math.min(sr, 1), -1)                         // ensure ratio is restricted to +1/-1 in case of big moves
c       = fixnan(rsr * vola)                                    // add volume
```