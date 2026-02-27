``` pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=3
// RSI Alligator Trend Strategy

strategy("RSI Alligator Trend Strategy", overlay=true)

v_input_1 = input(70, title="Over bought")
v_input_2 = input(30, title="Over sold")
v_input_3 = input(5, title="Jaw Periods")
v_input_4 = input(false, title="Jaw Offset")
v_input_5 = input(13, title="Teeth Periods")
v_input_6 = input(false, title="Teeth Offset")
v_input_7 = input(34, title="Lips Periods")
v_input_8 = input(false, title="Lips Offset")
strategyType = input("Long Only", title="strategyType: Long Only|Long & Short|Short Only")
v_input_9 = input("Long Only", title=strategyType)
v_input_10 = input(7, title="From Month")
v_input_11 = input(true, title="From Day")
v_input_12 = input(2018, title="From Year")
v_input_13 = input(12, title="To Month")
v_input_14 = input(true, title="To Day")
v_input_15 = input(2020, title="To Year")
v_input_16 = input(10, title="Stop Loss %")
v_input_17 = input(90, title="Take Profit %")

// Calculate RSI
jaw_rsi = rsi(close, v_input_3)
teeth_rsi = rsi(close, v_input_5)
lips_rsi = rsi(close, v_input_7)

// Long entry condition
long_condition = teeth_rsi > lips_rsi and jaw_rsi > teeth_rsi

// Short entry condition
short_condition = teeth_rsi < lips_rsi and jaw_rsi < teeth_rsi

if (strategyType == "Long Only" or strategyType == "Long & Short")
    if long_condition
        strategy.entry("Long", strategy.long)
if (strategyType == "Short Only" or strategyType == "Long & Short")
    if short_condition
        strategy.entry("Short", strategy.short)

// Stop loss and take profit levels
stop_loss = v_input_16 / 100 * close
take_profit = v_input_17 / 100 * close

if (strategy.position_size > 0)
    strategy.exit("Profit Target", from_entry="Long", limit=close + take_profit, stop=close - stop_loss)
if (strategy.position_size < 0)
    strategy.exit("Profit Target", from_entry="Short", limit=close - take_profit, stop=close + stop_loss)

// Plot RSI lines
plot(jaw_rsi, title="Jaw Line", color=color.blue)
plot(teeth_rsi, title="Teeth Line", color=color.orange)
plot(lips_rsi, title="Lip Line", color=color.red)
```

This Pine Script implementation reflects the strategy described in the Chinese document. The code is kept exactly as specified, with all numbers and formatting preserved.