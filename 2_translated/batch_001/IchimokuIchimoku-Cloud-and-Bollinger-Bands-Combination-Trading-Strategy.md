``` pinescript
/*backtest
start: 2023-12-19 00:00:00
end: 2023-12-26 00:00:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Coinrule

//@version=5
strategy("Ichimoku Cloud and Bollinger Bands",
         overlay=true,
         initial_capital=1000,
         process_orders_on_close=true,
         default_qty_type=strategy.percent_of_equity,
         default_qty_value=30,
         commission_type=strategy.commission.percent,
         commission_value=0.1)

showDate = input(defval=true, title='Show Date Range')
timePeriod = true
notInTrade = strategy.position_size <= 0


//Ichimoku Cloud
//Inputs
ts_bars = input.int(9, minval=1, title="Tenkan-Sen Bars")
ks_bars = input.int(26, minval=1, title="Kijun-Sen Bars")
ssb_bars = input.int(52, minval=1, title="Senkou-Span B Bars")
cs_offset = input.int(26, minval=1, title="Chikou-Span Offset")
ss_offset = input.int(26, minval=1, title="Senkou-Span Offset")
long_entry = input(true, title="Long Entry")
short_entry = input(true, title="Short Entry")

middle(len) => math.avg(ta.lowest(len), ta.highest(len))

// Components of Ichimoku Cloud
tenkan = middle(ts_bars)
kijun = middle(ks_bars)
senkouA = math.avg(tenkan, kijun)
senkouB = middle(ssb_bars)

```