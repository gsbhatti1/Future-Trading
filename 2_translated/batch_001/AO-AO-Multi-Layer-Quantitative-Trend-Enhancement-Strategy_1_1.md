> Source (PineScript)

``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-12-04 00:00:00
period: 1d
basePeriod: 1d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This Pine Script™ code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © Skyrexio

//@version=6
//_______ <licence>
strategy(title = "MultiLayer Awesome Oscillator Saucer Strategy [Skyrexio]", 
         shorttitle = "AO Saucer", 
         overlay = true, 
         format = format.inherit, 
         pyramiding = 5, 
         calc_on_order_fills = false, 
         calc_on_every_tick = false, 
         default_qty_type = strategy.percent_of_equity, 
         default_qty_value = 10, 
         initial_capital = 10000, 
         currency = currency.NONE,  
         commission_type = strategy.commission.percent, 
         commission_value = 0.1,
         slippage = 5,
         use_bar_magnifier = true)


//_______ <constant_declarations>
var const color skyrexGreen               = color.new(#2ECD99, 0)
var const color skyrexGray                = color.new(#F2F2F2, 0)
var const color skyrexWhite               = color.new(#FFFFFF, 0)


//________<variables declarations>
var int trend                             = 0
var float upFractalLevel                  = na
var float upFractalActivationLevel        = na
var float downFractalLevel                = na
var float downFractalActivationLevel      = na
var float saucerActivationLevel           = na
bool highCrossesUpfractalLevel            = ta.crossover(high, upFractalActivationLevel)
bool lowCrossesDownFractalLevel           = ta.crossunder(low, downFractalActivationLevel)
var int signalsQtyInRow                   = 0


//_______ <inputs>
// Trading bot settings
strategy.entry("Long", direction = strategy.long, when = highCrossesUpfractalLevel and trend > 0)
strategy.exit("Exit Long", "Long", stop = lowCrossesDownFractalLevel or saucerActivationLevel >= upFractalActivationLevel, profit = saucerActivationLevel - upFractalActivationLevel)
```

This Pine Script defines a strategy for trading using the Awesome Oscillator (AO) and fractal levels to identify long opportunities. The script includes setup for backtesting and trading bot parameters, along with conditions for entering and exiting trades based on specific technical indicators.