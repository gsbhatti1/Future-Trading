> Name

Dual-Trend-Filtering-Optimization-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1e1d7482bf8258a29e2.png)
[trans]
## Overview
This strategy uses average line double filtering and multi-level trend direction confirmation mechanisms to design a relatively stable tracking system. It consists of three main parts:

1. An optimized trend tracking system based on improved double peak oscillators to determine the major trend direction.
  
2. A sub-trend filtering system based on a combination of multiple cycle moving averages to further filter out some noise.

3. The Alpha Index provides final confirmation to ensure reliability of trading signals.

With the triple protection described above, the strategy can judge major trends more accurately and filter short-term market noise very effectively.

## Principle 
### Main Trend Tracking
It uses an improved double peak oscillator TOTT and a Close Series double trend filter to calculate the main trend direction. TOTT itself has very strong filtering capabilities against noise. The Close Series provides an additional level of confirmation. The combination of the two can determine major trends very accurately.

### Subtrend Filtering  
In addition to the main trend judging system, the strategy also sets up a sub-trend filtering system based on EMA combinations of multiple cycles. According to the Golden Cross and Dead Cross confirmation levels of the EMA lines, the reliability of judgments on the main trend direction is further improved and more noise is filtered out.

### Alpha Confirmation
When entering and exiting positions, the strategy also checks the value of the Alpha Index to ensure reliability of final trading signals. Alpha reflects the buying and selling power in the market and is a good confirmation indicator.

## Advantages
- Multi-level protection design for more accurate major trend judgments  
- Powerful noise filtering capability
- Stable and reliable trading signals
- Large parameter optimization space

## Risks
- Signal frequency may be low
- The tracking system uses moving averages, which can be broken in drastic market changes

To mitigate the risks, parameters can be adjusted to optimize tracker sensitivity, or more reversal indicators can be added as final filters.  

## Optimization Directions
- Adjust double peak oscillator parameters to find better parameter combinations
- Try parameter optimization of different moving average types  
- Optimize EMA line cycle periods in the combination
- Enhance Alpha filtering mechanism
- Add stop loss mechanism  

## Conclusion
The overall design of this strategy is robust, with proper measures and multiple protections. The powerful noise filtering gives it stable performance. There is room for further improvement through continuous parameter optimization and mechanism enhancements.  
[/trans]

> Strategy Arguments

|Argument|Default|Description|
|---|---|---|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_1|18|OTT Period|
|v_input_float_1|true|Optimization Constant|
|v_input_float_2|0.001|Twin OTT Coefficient|
|v_input_2|true|Show Support Line?|
|v_input_3|true|Show Signals?|
|v_input_string_1|0|Moving Average Type: EMA|SMA|WMA|TMA|VAR|WWMA|ZLEMA|TSF|
|v_input_4|true|Highlighter On/Off ?|
|v_input_5_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_int_2|69|OTT Period|
|v_input_float_3|true|Optimization Constant|
|v_input_float_4|0.001|Twin OTT Coefficient|
|v_input_6|true|Show Support Line?|
|v_input_7|true|Show Signals?|
|v_input_string_2|0|Moving Average Type: VAR2|EMA|WMA|TMA|SMA|WWMA|ZLEMA2|TSF2|
|v_input_8|true|Highlighter On/Off ?|
|v_input_9_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_10|true|Use Alternate Resolution?|
|v_input_11|3|Multiplier for Alernate Resolution|
|v_input_string_3|0|MA Type: : SMMA|EMA|DEMA|TEMA|WMA|VWMA|SMA|HullMA|LSMA|ALMA|SSMA|TMA|
|v_input_int_3|8|MA Period|
|v_input_int_4|6|Offset for LSMA / Sigma for ALMA|
|v_input_float_5|0.85|Offset for ALMA|
|v_input_12|false|Show coloured Bars to indicate Trend?|
|v_input_int_5|false|Delay Open/Close MA (Forces Non-Repainting)|
|v_input_string_4|0|What trades should be taken : : BOTH|SHORT|LONG|NONE|
|v_input_int_6|false|Initial Stop Loss Points (zero to disable)|
|v_input_int_7|false|Initial Target Profit Points (zero for disable)|
|v_input_int_8|10000|Number of Bars for Back Testing|
|v_input_13|false|- SET to ZERO for Daily or Longer Timeframes|
|v_input_float_6|true|Multiplier|
|v_input_14|14|Common Period|
|v_input_15_close|0|src5: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_16|true|Show Signals?|
|v_input_17|false|Change calculation (no volume data)?|

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-02-20 00:00:00
end: 2024-02-26 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
```