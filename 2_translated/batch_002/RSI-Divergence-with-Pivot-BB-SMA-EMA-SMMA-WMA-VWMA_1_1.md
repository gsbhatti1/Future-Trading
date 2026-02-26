``` pinescript
/*backtest
start: 2022-04-11 00:00:00
end: 2022-05-10 23:59:00
period: 10m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

////////////////////////////////////////////////////////////////////////////////
//                                                                            //
//                      ====== My Crypto Succubus ======                      //
//   ====== RSI Divergence with Pivot, BB, SMA, EMA, SMMA, WMA, VWMA ======   //
//                                                                            //
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
//                                                                            //
// My Crypto Succubus is a project based on the community and participatory  //
// aspect, knowledge sharing is the core of the project, the act of sharing   //
// is destined to get richer, either on the intellectual or the wealth        //
// side, the ultimate goal of MCS is that every single one of our members     //
// can reach the financial freedom we all deserve.                            //
//                                                                            //
//   ====== Join us on our Discord : https://discord.gg/TmW6RQeyXp  ======    //
//                                                                            //
////////////////////////////////////////////////////////////////////////////////
//@version=5
indicator(title="RSI Divergences with Pivots, BB, MA [My Crypto Succubus]", shorttitle="RSI Div, Pivot, BB, MA [My Crypto Succubus]", format=format.price, precision=2)

ma(source, length, type) =>
    switch type
        "SMA" => ta.sma(source, length)
        "Bollinger Bands" => ta.sma(source, length)
        "EMA" => ta.ema(source, length)
        "SMMA (RMA)" => ta.rma(source, length)
        "WMA" => ta.wma(source, length)
        "VWMA" => ta.vwma(source, length)

rsiLengthInput = input.int(14, minval=1, title="RSI Length", group="RSI Settings")
rsiSourceInput = input.source(close, "Source", group="RSI Settings")
maTypeInput = input.string("SMA", title="MA Type", options=["SMA", "Bollinger Bands", "EMA", "SMMA (RMA)", "WMA", "VWMA"], group="MA Settings")
maLengthInput = input.int(14, title="MA Length", group="MA Settings")
bbMultInput = input.float(2.0, minval=0.001, maxval=50, title="BB StdDev", group="MA Settings")

up = ta.rma(math.max(ta.change(rsiSourceInput), 0), rsiLengthInput)
down = ta.rma(-math.min(ta.change(rsiSourceInput), 0), rsiLengthInput)
rsi = down == 0 ? 100 : up == 0 ? 0 : 100 - (100 / (1 + up / down))
rsiMA = ma(rsi, maLengthInput, maTypeInput)
isBB = maTypeInput == "Bollinger Bands"

plot(rsi, "RSI", color=#ffffff, linewidth=1)
plot(rsiMA, "RSI-based MA", color=color.yellow)
rsiUpperBand = hline(70, "RSI Upper Band", color=#787B86)
hline(50, "RSI Middle Band", color=color.new(#787B86, 50))
rsiLowerBand = hline(30, "RSI Lower Band", color=#787B86)
fill(rsiUpperBand, rsiLowerBand, color=color.rgb(178, 8, 120, 90), title="RSI Background Fill")
bbUpperBand = plot(isBB ? rsiMA + ta.stdev(rsi, maLengthInput) * bbMultInput : na, title = "Upper Bollinger Band", color=color.green)
bbLowerBand = plot(isBB ? rsiMA - ta.stdev(rsi, maLengthInput) * bbMultInput : na, title = "Lower Bollinger Band", color=color.green)
fill(bbUpperBand, bbLowerBand, color= isBB ? color.new(color.green, 90) : na, title="Bollinger Bands Background Fill")

///////////////////////////////////////////////////////////////////////////////////////////////////////

len = input.int(14, minval=1, title='RSI Length', group="RSI Settings")
ob = input.int(defval=70, title='Overbought', minval=0, maxval=100, group="RSI Settings")
os = input.int(defval=30, title='Oversold', minval=0, maxval=100, group="RSI Settings")

// RSI code
band1 = hline(ob)
band0 = hline(os)
plot(rsi, color=rsi > ob or rsi < os ? color.rgb(255, 0, 0, 0) : color.new(color.black, 100), linewidth=1)
fill(band1, band0, color=color.new(color.purple, 97))

// DIVS code
piv = input(false, 'Hide pivots?')
shrt = input(false, 'Shorter labels?')
hidel = input(true, 'Hide labels and color background')
xbars = input.int(defval=90, title='Div lookback period (bars)?', minval=1)
hb = math.abs(ta.highestbars(rsi, xbars))  // Finds bar with highest value in last X bars
lb = math.abs(ta.lowestbars(rsi, xbars))  // Finds bar with lowest value in last X bars

// Defining variable values, mandatory in Pine 3
max = float(na)
max_rsi = float(na)
min = float(na)
min_rsi = float(na)
pivoth = bool(na)
pivotl = bool(na)
divbear = bool(na)
divbull = bool(na)

// If bar with lowest / highest is current bar, use it's value
max := hb == 0 ? close : na(max[1]) ? close : max[1]
max_rsi := hb == 0 ? rsi : na(max_rsi[1]) ? rsi : max_rsi[1]
min := lb == 0 ? close : na(min[1]
```