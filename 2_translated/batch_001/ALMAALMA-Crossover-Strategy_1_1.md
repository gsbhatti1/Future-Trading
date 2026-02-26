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
ALMA1 = input(100, "ALMA Lenghth 1", group= "ALMA Fast Length Settings")
alma_offset = input.float(defval=0.85, title='Arnaud Legoux (ALMA) - Offset Value', minval=0, step=0.01)
alma_sigma = input.int(defval=6, title='Arnaud Legoux (ALMA) - Sigma Value', minval=0)
Alma1 = ta.alma(src, ALMA1, alma_offset, alma_sigma)

//Slow Settings
ALMA2 = input(120, "ALMA Length 2", group="ALMA Slow Length Settings")
alma_offset2 = input.float(defval=0.85, title='Arnaud Legoux (ALMA) - Offset Value', minval=0, step=0.01)
alma_sigma2 = input.int(defval=6, title='Arnaud Legoux (ALMA) - Sigma Value', minval=0)
Alma2 = ta.alma(src, ALMA2, alma_offset2, alma_sigma2)

//Volume Filter
short_volume_length = input.int(5, "Short Length", group="Volume Settings")
volume_filter = sma(volume, short_volume_length) > 0

//Buy and Sell Conditions
long_condition = crossabove(Alma1, Alma2) and volume_filter
short_condition = crossbelow(Alma1, Alma2)

//Take Profit and Stop Loss
take_profit_long = input.float(2, "Long Take Profit", group="Take Profit Percentage")
stop_loss_short = input.float(2.5, "Short Stop Percentage", group="Stop Percentage")

//Trade Logic
if (long_condition)
    strategy.entry("Buy", strategy.long)

if (short_condition)
    strategy.entry("Sell", strategy.short)

// Position Sizing
position_size_long = input.int(100, "Long Length")
strategy.exit("Cover Long", from_entry="Buy", limit=Alma2 * (1 + take_profit_long), stop=Alma2 * (1 - stop_loss_short))

```