> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|120|Timeframe|
|v_input_2|25|Long Length|
|v_input_3|13|Short Length|
|v_input_4|13|Signal Length|
|v_input_5|300|Period|
|v_input_6|true|From Month|
|v_input_7|true|From Day|
|v_input_8|2017|From Year|
|v_input_9|true|To Month|
|v_input_10|true|To Day|
|v_input_11|9999|To Year|


> Source (PineScript)

```pinescript
// Define the strategy name and description
strategy("Momentum Dual Moving Window TSI Indicator Strategy", shorttitle="MDMW-TSI")

// Input parameters
timeframe = input(120, title="Timeframe")
long_length = input(25, title="Long Length")
short_length = input(13, title="Short Length")
signal_length = input(13, title="Signal Length")
period = input(300, title="Period")
from_month = input(true, title="From Month")
from_day = input(true, title="From Day")
from_year = input(2017, title="From Year")
to_month = input(true, title="To Month")
to_day = input(true, title="To Day")
to_year = input(9999, title="To Year")

// Function to calculate double smoothed price change
double_smooth(pc, long_period, short_period) =>
    ewa1 = ema(close - close[long_period], long_period)
    ewa2 = ema(ewa1, short_period)
    ewa2

// Calculate TSI value
tsi_value = 100 * (double_smooth(change(close), long_length, short_length) / double_smooth(abs(change(close)), long_length, short_length))

// Plot TSI value on the chart
plot(tsi_value, title="TSI Value", color=color.blue)

// Generate buy and sell signals based on TSI crossing its moving average
if crossover(tsi_value, sma(tsi_value, signal_length))
    strategy.entry("Buy", strategy.long)
if crossunder(tsi_value, sma(tsi_value, signal_length))
    strategy.exit("Sell", "Buy")
```
```