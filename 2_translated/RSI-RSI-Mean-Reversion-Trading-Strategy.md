```pinescript
/*backtest
start: 2022-09-05 00:00:00
end: 2023-09-11 00:00:00
Period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © relevantLeader16058

//@version=4
strategy(shorttitle='RSI Bot Strategy', title='Quadency Mean Reversion Bot Strategy', overlay=true, initial_capital = 100, process_orders_on_close=true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100, commission_type=strategy.commission.percent, commission_value=0.08)

// Backtest dates
start = input(defval = timestamp("08 Mar 2021 00:00 -0600"), title = "Start Time", type = input.time)
finish = input(defval = timestamp("9 Mar 2021 23:59 -0600"), title = "End Time", type = input.time)
window() => true // create function "within window of time"

// Complete Control over RSI inputs and source price calculations
lengthRSI = input(14, minval=1)
source = input(title="Source", type=input.source, defval="close")
strat = input(title="Strategy", defval="Long/Short", options=["Long Only", "Long/Short", "Short Only"])
strat_val = strat == "Long Only" ? 1 : strat == "Long/Short" ? 0 : -1
stoploss = input(5.00, "Stop Loss %")
oversold= input(30)
overbought= input(60)

// Standard RSI Calculation
RSI = rsi(source, lengthRSI)
stLossLong=(1-(stoploss*.01))
stLossShort=(1+(stoploss*.01))

// Long and Short Strategy Logic
GoLong = crossunder(RSI, oversold) and window()
GoShort = crossover(RSI, overbought) and window()

// Strategy Entry and Exit
if (GoLong)
    if strat_val > -1
        strategy.entry("LONG", strategy.long)
    if strat_val < 1
        strategy.close("SHORT")


if(GoShort)
    if strat_val > -1
        strategy.close("LONG")
    if strat_val < 1
        strategy.entry("SHORT", strategy.short)


LongStopLoss = barssince(GoLong)<barssinc
```