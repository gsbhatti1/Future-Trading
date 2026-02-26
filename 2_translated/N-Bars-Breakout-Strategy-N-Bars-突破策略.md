```pinescript
/*backtest
start: 2023-04-06 00:00:00
end: 2024-04-11 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("N Bars Breakout Strategy", overlay=true, precision=6, pyramiding=0, initial_capital=1000, default_qty_type=strategy.percent_of_equity, default_qty_value=25.0, commission_value=0.05)

n = input.int(5, "N Bars", minval=1)
src_input = input.string("Close", "Source", ["Close", "High/Low"])

bull_src = switch src_input
    "Close" => close
    "High/Low" => high
    => 
        runtime.error("Invalid source input")
        na

bear_src = switch src_input
    "Close" => close
    "High/Low" => low
    => 
        runtime.error("Invalid source input")
        na

highest = ta.highest(bull_src[1], n)
lowest = ta.lowest(bear_src[1], n)

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------
// Plots
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------

bool long = ta.crossover(bull_src, highest)
bool short = ta.crossunder(bear_src, lowest)

//Plots
lowest_plot  = plot(lowest,  color=color.red, title="Lowest")
highest_plot  = plot(highest,  color=color.green, title="Highest")
bull_src_plot = plot(bull_src, color=color.blue, title="Bull")
bear_src_plot = plot(bear_src, color=color.orange, title="Bear")

// this message is an alert that can be sent to a webhook, which allows for simple automation if you have a server that listens to alerts and trades programmatically.
enter_long_alert = '{"side": "Long", "order": "Enter", "price": ' + str.tostr(strategy.opentrades.avg_price("Long")) + '}'
```