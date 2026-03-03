```pinescript
"Std 18 52 104 26"], defval="Std 18 52 104 26")
drop_first_n = input(title="Drop first N candles", type=bool, defval=true)
show_clouds = input(title="Show Clouds", type=bool, defval=false)
stop_loss = input(title="Stop Loss", type=bool, defval=true)
from_month = input(title="From Month", type=int, minval=1, maxval=12, defval=6)
from_day = input(title="From Day", type=int, minval=1, maxval=31, defval=15)
from_year = input(title="From Year", type=int, minval=1900, defval=2023)
to_month = input(title="To Month", type=bool, defval=true)
to_day = input(title="To Day", type=bool, defval=true)
to_year = input(title="To Year", type=int, minval=1900, defval=2023)

// Ichimoku Cloud Parameters
ichimoku_conversion_period = ichiConversionPeriods(presets)
ichimoku_base_period = ichiBasePeriods(presets)
ichimoku_lagging_span2_period = ichiLaggingSpan2Periods(presets)
ichimoku_displacement = ichiDisplacement(presets)

// Calculate Ichimoku Cloud
highs = high[ichimoku_conversion_period]
lows = low[ichimoku_conversion_period]
conversion_line = xhighest(highs, 1) + xlowest(lows, 1)
base_line = xlowest_(highs + lows, ichimoku_base_period / 2)
lagging_span1 = (highs + lows) / 2
lagging_span2 = xhighest(highs, ichimoku_lagging_span2_period) - xlowest(low, ichimoku_lagging_span2_period)

// Plot Ichimoku Cloud and lines
plot(lagging_span1, title="Conversion Line", color=color.blue)
plot(base_line, title="Base Line", color=color.red)
fill(area(hline(0), lagging_span1, base_line), color=color.new(color.gray, 95))

// Buy/Sell Signals
buy_signal = crossover(conversion_line, base_line)
sell_signal = crossunder(conversion_line, base_line)

if buy_signal and (from_month <= month and from_day <= day and from_year == year) and not to_month or to_year > year or (to_month and to_day <= day):
    strategy.entry("Buy", strategy.long)

if sell_signal and (from_month <= month and from_day <= day and from_year == year) and not to_month or to_year > year or (to_month and to_day <= day):
    strategy.exit("Sell", "Buy")

// Stop Loss
if stop_loss and position_size != 0:
    strategy.exit("Stop Loss", "Buy", loss=v_input_6)

```
[/trans]