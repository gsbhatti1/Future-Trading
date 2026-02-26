> Strategy Arguments



|Argument|Default|Description|
|---|---|---|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|false|Use Martingale|
|v_input_4|100|Capital, %|
|v_input_5|true|Use CRSI Strategy|
|v_input_6|true|Use FRSI Strategy|
|v_input_7|true|CRSI+FRSI Mode|
|v_input_8|25|RSI limit|
|v_input_9|true|Use Body-filter|
|v_input_10|true|Use Color-filter|
|v_input_11|1900|From Year|
|v_input_12|2100|To Year|
|v_input_13|true|From Month|
|v_input_14|12|To Month|
|v_input_15|true|From day|
|v_input_16|31|To day|


> Source (PineScript)

```pinescript
// backtest start: 2023-10-07 00:00:00
// backtest end: 2023-11-06 00:00:00
// backtest period: 1h
// basePeriod: 15m
// exchanges:

//@version=5
strategy("RSI Momentum Reversal Strategy", overlay=true)

long = input(true, title="Long")
short = input(true, title="Short")
martingale = input(false, title="Use Martingale")
capital_percent = input(100, title="Capital, %")
use_crsi = input(true, title="Use CRSI Strategy")
use_frsi = input(true, title="Use FRSI Strategy")
crsi_frsi_mode = input(true, title="CRSI+FRSI Mode")
rsi_limit = input(25, title="RSI limit")
use_body_filter = input(true, title="Use Body-filter")
use_color_filter = input(true, title="Use Color-filter")
from_year = input(1900, title="From Year")
to_year = input(2100, title="To Year")
from_month = input(true, title="From Month")
to_month = input(12, title="To Month")
from_day = input(true, title="From day")
to_day = input(31, title="To day")

// Connors RSI
crsi_length = 7
crsi_smooth = 2
rsi_length = 14

connors_rsi = rsi(close, rsi_length)
win_ratio = 100 * (close > sma(close, crsi_length) ? 1 : -1)
parisian = close > highest(high[1..crsi_smooth]) and low < lowest(low[1..crsi_smooth])
connors_rsi := (connors_rsi + win_ratio + parisian) / 3

// Fast RSI
fast_rsi_length = 9
fast_rsi_smooth = 2

fast_rsi = rsi(close, fast_rsi_length)

// Candlestick body filter
body_condition = close > open and close >= (open + 0.5 * typical_price)
body_filter = na(body_condition) or not use_body_filter ? false : true

// Color filter
color_condition = open < close and close >= high[1] and open <= low[1]
color_filter = na(color_condition) or not use_color_filter ? false : true

// Strategy conditions
long_condition = connors_rsi < rsi_limit and fast_rsi < 0.9 * rsi_limit and body_condition and long
short_condition = connors_rsi > (100 - rsi_limit) and fast_rsi > 0.9 * (100 - rsi_limit) and not body_condition and short

if (long_condition)
    strategy.entry("Long", strategy.long, when=long_condition)

if (short_condition)
    strategy.entry("Short", strategy.short, when=short_condition)

// Martingale
if (martingale and long_condition)
    risk = capital_percent / 100 * account.margin_balance / account.total_margin
    if (account.open_orders == 0 or not use_martingale)
        strategy.close_all()
    else
        for i = 1 to account.open_orders - 1
            profit_ratio = (close[i] - open[i]) / open[i]
            if (profit_ratio > 0.5 and not use_martingale) or risk <= min_risk
                break
            strategy.exit("Exit Long", "Long")
```
```