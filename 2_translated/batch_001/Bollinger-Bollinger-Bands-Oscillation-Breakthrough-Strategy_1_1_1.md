> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Month|
|v_input_2|true|From Day|
|v_input_3|2020|From Year|
|v_input_4|true|Thru Month|
|v_input_5|true|Thru Day|
|v_input_6|2112|Thru Year|
|v_input_7|true|Show Date Range|
|v_input_8|20|lengthBB|
|v_input_9_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_10|2|StdDev|
|v_input_11|false|Offset|
|v_input_12|288|lengthAr|
|v_input_13|90|Aroon Confirmation|
|v_input_14|70|Aroon Stop|


> Source (PineScript)

```pinescript
//@version=5
indicator("Bollinger-Bands-Oscillation-Breakthrough-Strategy", overlay=true)
from_month = input(true, title="From Month")
from_day = input(true, title="From Day")
from_year = input(2020, title="From Year")
thru_month = input(true, title="Thru Month")
thru_day = input(true, title="Thru Day")
thru_year = input(2112, title="Thru Year")
show_date_range = input(true, title="Show Date Range")
lengthBB = input(20, title="lengthBB")
source_close = input(close, title="Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4")
std_dev = input(2, title="StdDev")
offset = input(false, title="Offset")
lengthAr = input(288, title="lengthAr")
aroon_confirmation = input(90, title="Aroon Confirmation")
aroon_stop = input(70, title="Aroon Stop")

// Bollinger Bands
bb = ta.bbands(source_close, lengthBB, std_dev)
middle_band = bb[1]
upper_band = bb[2]
lower_band = bb[3]

// Aroon Indicator
aroondown, aroonup = ta.aroon(lengthAr)

// Strategy Logic
long_condition = lower_band > middle_band and (aroonup > aroon_confirmation or offset == false)
short_condition = upper_band < middle_band and (aroonup < aroon_stop or offset == false)

strategy.entry("Long", strategy.long, when=long_condition)
strategy.exit("Close Long", "Long", stop=lower_band, limit=upper_band, trail_offset=aroon_stop)
```

This Pine Script implements the Bollinger-Bands-Oscillation-Breakthrough-Strategy as described. The script uses input parameters to customize the strategy according to user preferences and includes logic for both entering long positions based on breakouts from the lower Bollinger Band and exiting those positions using Aroon indicators.