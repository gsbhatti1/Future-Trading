> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|40|channel length|
|v_input_2|60|average length|
|v_input_3|40|over bought level 1|
|v_input_4|50|over bought level 1|
|v_input_5|70|over bought level 1|
|v_input_6|80|over bought level 1|
|v_input_7|100|over bought level 2|
|v_input_8|-40|over sold level 1|
|v_input_9|-45|over sold level 1|
|v_input_10|-50|over sold level 1|
|v_input_11|-55|over sold level 1|
|v_input_12|-65|over sold level 1|
|v_input_13|-75|over sold level 1|
|v_input_14|-85|over sold level 1|
|v_input_15|-100|over sold level 2|
|v_input_16_hlc3|0|source: hlc3|high|low|open|hl2|close|hlcc4|ohlc4|


> Source (PineScript)

```pinescript
//@version=5
// © And Isaac, all rights reserved. If there is any piracy, please call the police immediately.
strategy("Wavetrend Large Amplitude Oversold Rebound Grid Trading Strategy", overlay=true)

v_input_1 = input.int(40, title="Channel Length")
v_input_2 = input.int(60, title="Average Length")
v_input_3 = input.int(40, title="Overbought Level 1")
v_input_4 = input.int(50, title="Overbought Level 1")
v_input_5 = input.int(70, title="Overbought Level 1")
v_input_6 = input.int(80, title="Overbought Level 1")
v_input_7 = input.int(100, title="Overbought Level 2")
v_input_8 = input.float(-40, title="Oversold Level 1")
v_input_9 = input.float(-45, title="Oversold Level 1")
v_input_10 = input.float(-50, title="Oversold Level 1")
v_input_11 = input.float(-55, title="Oversold Level 1")
v_input_12 = input.float(-65, title="Oversold Level 1")
v_input_13 = input.float(-75, title="Oversold Level 1")
v_input_14 = input.float(-85, title="Oversold Level 1")
v_input_15 = input.float(-100, title="Oversold Level 2")
v_input_16_hlc3 = input.int(0, title="Source", options=["hlc3", "high", "low", "open", "hl2", "close", "hlcc4", "ohlc4"])

// Calculate Wavetrend indicator
wt1 = ta.wavelet(hl2, v_input_1)
wt2 = sma(wt1, v_input_2)

// Define overbought and oversold levels
overbought_levels = [v_input_3, v_input_4, v_input_5, v_input_6, v_input_7]
oversold_levels = [v_input_8, v_input_9, v_input_10, v_input_11, v_input_12, v_input_13, v_input_14, v_input_15]

// Open positions when the price is below oversold levels and above wt2
for i = 0 to array.size(oversold_levels) - 1
    if wt1 <= oversold_levels[i] and wt1 > wt2
        strategy.entry("Long Entry", strategy.long)

// Close 70% of long positions when the price is above overbought level 1
if wt1 >= v_input_3 and wt1 < wt2
    strategy.close(id="Long Entry", percentage=0.7)

// Repeat the process to build a grid trading system
```