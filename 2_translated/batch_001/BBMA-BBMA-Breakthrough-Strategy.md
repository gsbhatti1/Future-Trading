<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

BBMA Breakthrough Strategy

> Author

ChaoZhang

> Strategy Description


![IMG](https://www.fmz.com/upload/asset/773df181c666570e12.png)

[trans]
[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|BBMA Length|
|v_input_2|2|Deviation|
|v_input_3|50|EMA Period|
|v_input_4|10|Fast EMA Period|
|v_input_float_1|true|Stop Loss Percentage|
|v_input_float_2|2|Take Profit Percentage|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-12-17 00:00:00
end: 2023-12-24 00:00:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("BBMA Strategy", shorttitle="BBMA", overlay=true)

// Input parameters
length = input(20, title="BBMA Length")
deviation = input(2, title="Deviation")
ema_period = input(50, title="EMA Period")
fast_ema_period = input(10, title="Fast EMA Period")
stop_loss_percentage = input.float(1, title="Stop Loss Percentage") / 100
take_profit_percentage = input.float(2, title="Take Profit Percentage") / 100

// Calculate Bollinger Bands and MTF MA
basis = ta.sma(close, length)
dev = deviation * ta.stdev(close, length)
upper_bb = basis + dev
lower_bb = basis - dev
ema = ta.ema(close, ema_period)
fast_ema = ta.ema(close, fast_ema_period)

// Entry conditions
long_condition = ta.crossover(close, upper_bb) and ta.crossover(close, fast_ema) and close > ema
short_condition = ta.crossunder(close, lower_bb) and ta.crossunder(close, fast_ema) and close < ema

// Signals for entry and exit with stop loss and take profit
if (long_condition)
    strategy.entry("Buy", strategy.long)
    strategy.exit("Take Profit/Stop Loss", from_entry="Buy", stop=close * (1 + stop_loss_percentage), limit=close * (1 + take_profit_percentage))

if (short_condition)
    strategy.entry("Sell", strategy.short)
    strategy.exit("Take Profit/Stop Loss", from_entry="Sell", stop=close * (1 - stop_loss_percentage), limit=close * (1 - take_profit_percentage))
```

> Detail

https://www.fmz.com/strategy/436483

> Last Modified

2023-12-25 11:33:50