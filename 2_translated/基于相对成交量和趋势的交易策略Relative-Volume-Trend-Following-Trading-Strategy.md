``` pinescript
LEN_RELATIVE_VOL = input(5, title="SMA(volume) length (for relative comparison)"), 
relative_vol = sma(volume, LEN_RELATIVE_VOL),
plot(relative_vol, "Relative Volume", color=color.blue, offset = 0)
// }

// Entry Conditions {
long_condition = not opened_position and is_low_volat and relative_vol > close[1]
if long_condition
    strategy.entry("Long", strategy.long)
    opened_position := true
// }

// Exit Conditions {
long_stop_loss = not opened_position or (strategy.position_size > 0 and TSL_source < stop_loss_price)
if long_stop_loss
    strategy.exit("Long Exit", "Long")
    opened_position := false
// }

// Bearish Engulfing Pattern Detection {
bearish_engulfing = na
for i = 0 to barssince(closed > open and close[1] < open[1] and close < open[1])
    bearish_engulfing := i == 0 ? 1 : bearish_engulfing + 1
long_exit_condition = not opened_position or (strategy.position_size > 0 and bearish_engulfing > 0)
if long_exit_condition
    strategy.exit("Long Exit", "Long")
    opened_position := false
// }

```