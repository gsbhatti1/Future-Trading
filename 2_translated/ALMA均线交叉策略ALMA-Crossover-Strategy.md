``` pinescript
/*backtest
start: 2022-09-16 00:00:00
end: 2023-09-22 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Sarahann999
// Calculations for TP/SL based off: https://kodify.net/tradingview/orders/percentage-profit/
//@version=5
strategy("ALMA Cross", overlay=true)

//User Inputs
src = close
long_entry = input(true, title='Long Entry')
short_entry = input(true, title='Short Entry')

//Fast Settings
ALMA1 = input(100, "ALMA Length 1", group="ALMA Fast Length Settings")
alma_offset_1 = input.float(defval=0.85, title='Arnaud Legoux (ALMA) - Offset Value', minval=0, step=0.01)
alma_sigma_1 = input.int(defval=6, title='Arnaud Legoux (ALMA) - Sigma Value', minval=0)
Alma1 = ta.alma(src, ALMA1, alma_offset_1, alma_sigma_1)

//Slow Settings
ALMA2 = input(120, "ALMA Length 2", group="ALMA Slow Length Settings")
alma_offset_2 = input.float(defval=0.85, title='Arnaud Legoux (ALMA) - Offset Value', minval=0, step=0.01)
alma_sigma_2 = input.int(defval=6, title='Arnaud Legoux (ALMA) - Sigma Value', minval=0)
Alma2 = ta.alma(src, ALMA2, alma_offset_2, alma_sigma_2)

//Long and Short Length
long_length = input.int(10, title="Long Length")
short_length = input.int(defval=3, title="Short Length")

//Take Profit and Stop Loss
short_take_profit = input.float(2, title="Short Take Profit", minval=0)
short_stop_loss = input.float(2.5, title="Short Stop Loss", minval=0)
long_take_profit_percent = input.float(2, title="Long Take Profit %")
long_stop_loss_percent = input.float(2.5, title="Long Stop Loss %")

// Buy and Sell Conditions
long_condition = ta.crossover(Alma1, Alma2) and long_entry
short_condition = ta.crossunder(Alma1, Alma2) and short_entry

// Volume Filter
vol_short = ta.volume > ta.sma(src.vol, short_length)

// Order Management
if (long_condition and vol_short)
    strategy.entry("Long", strategy.long)
    
if (short_condition)
    strategy.entry("Short", strategy.short)
    
strategy.exit("Long Exit", "Long", profit=long_take_profit_percent/100 * close, loss=long_stop_loss_percent/100 * close)

strategy.exit("Short Exit", "Short", profit=short_take_profit, loss=short_stop_loss)
```

This translation preserves the original code structure and comments while providing an English version of the strategy description.