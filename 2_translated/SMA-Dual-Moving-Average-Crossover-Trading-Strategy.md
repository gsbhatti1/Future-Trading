> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|14|(?Indicator Settings)Short SMA Length|
|v_input_int_2|28|Long SMA Length|
|v_input_bool_1|true|(?Compounding)Compounding|
|v_input_bool_2|true|(?Take Profit and Stop Loss)Use Take Profit|
|v_input_float_1|0.1|Take Profit %|
|v_input_bool_3|true|Use Stop Loss|
|v_input_float_2|0.5|Stop Loss %|
|v_input_1|timestamp(1 Jan 2023 00:00:00)|(?TRADING WINDOW)Start Date|
|v_input_2|timestamp(1 Jan 2030 00:00:00)|End Date|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-10-21 00:00:00
end: 2023-11-20 00:00:00
period: 4h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © BigJasTrades https://linktr.ee/bigjastrades 

// READ THIS BEFORE USE:
// This code is provided as an example strategy for educational purposes only.  It comes with NO warranty or claims of performance.
// It should be used as a basis for your own learning and development and to create your own strategies.
// It is NOT provided to enable you to profitably trade. 
// If you use this code or any part of it you agree that you have thoroughly tested it and determined that it is suitable for your own purposes prior to use.
// If you use this code or any part of it you agree that you accept all risk and you are responsible for the results.

//@version=5
strategy(title = "Strategy Template", shorttitle = "ST v1.0", overlay = true, pyramiding = 1, initial_capital = 1000, commission_type = strategy.commission.percent, commission_value = 0.1, max_labels_count = 500)

// INPUTS
// Indicator values
shortSMAlength              = input.int(defval = 14, title = "Short SMA Length", tooltip = "Set the length of the short simple moving average here.", minval = 1, step = 1, group = "Indicator Settings")
longSMAlength               = input.int(defval = 28, title = "Long SMA Length", tooltip = "Set the length of the long simple moving average here.", minval = 1, step = 1, group = "Indicator Settings")

// Compounding
compoundingSelected         = input.bool(defval = true, title = "Compounding", tooltip = "Select this option if you want to compound your net profits.", group = "Compounding")

// Take profit and stop loss
takeProfitSelected          = input.bool(defval = true, title = "Use Take Profit", tooltip = "Select this to enable take profits.", group = "Take Profit and Stop Loss")
takeProfitPercent           = input.float(defval = 0.1, title = "Take Profit %", tooltip = "Set the value of take profits here.", minval = 0.1, step = 0.1, group = "Take Profit and Stop Loss")
stopLossSelected            = input.bool(defval = true, title = "Use Stop Loss", tooltip = "Select this to enable stop losses.", group = "Take Profit and Stop Loss")
stopLossPercent             = input.float(defval = 0.5, title = "Stop Loss %", tooltip = "Set the value of stop losses here.", minval = 0.1, step = 0.1, group = "Take Profit and Stop Loss")

// Trading window
startDate                   = input.time(title = "Start Date", defval = timestamp("2023-01-01"), group = "TRADING WINDOW")
endDate                     = input.time(title = "End Date", defval = timestamp("2030-01-01"), group = "TRADING WINDOW")

// SMA calculation
shortSMA                    = sma(close, shortSMAlength)
longSMA                     = sma(close, longSMAlength)

// Entry rules
if (crossabove(shortSMA, longSMA))
    strategy.entry("Long", strategy.long)

if (crossbelow(shortSMA, longSMA))
    strategy.entry("Short", strategy.short)

// Exit rules with take profit and stop loss
if (takeProfitSelected)
    takeprofitLevel = strategy.position_avg_price * (1 + takeProfitPercent)
    strategy.exit("Take Profit", from_entry="Long", limit=takeprofitLevel)
    
if (stopLossSelected)
    stoplossLevel = strategy.position_avg_price * (1 - stopLossPercent)
    strategy.exit("Stop Loss", from_entry="Long", stop=stoplossLevel)

// Money management
positionSize                = fixed_size(strategy.initial_capital, close, commission_type, commission_value)
```