``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-12-09 08:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// @version=5
// Draw corresponding horizontal lines on each chart, do it manually for now
// Allow up to 200 additional positions in the same direction, recalculate after order execution and at every tick. Variables are saved for 1000 bars, orders processed at bar close, draw plots based on code sequence
strategy("Price Level Breakout Strategy", overlay=true, pyramiding=200, calc_on_order_fills=true, calc_on_every_tick=true, max_bars_back=1000, process_orders_on_close=true, explicit_plot_zorder=true)
// var creates persistent variables, := updates the variable without redeclaring
// This is a global variable
// a = array.new<string>(200)
// array.push(a, "a")
// plot(close, color = array.get(a, close > open ? 1 : 0))
string ticker = syminfo.ticker
var float step_size = 1.5 * close / 100 // Set the step size as 1.5% of the current price
// label.new(x=bar_index, y
```