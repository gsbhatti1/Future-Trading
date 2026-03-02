```pinescript
/*backtest
start: 2022-10-19 00:00:00
end: 2023-10-25 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy( "MACD-Controlled-Risk-Trading-Strategy", shorttitle="Risk Controlled Trading", initial_capital=10000, default_qty_type=strategy.cash, currency=currency.USD )

capital_risk    = input( 1.0, "% capital risk per trade" ) / 100
r_exit          = input( 4.0, "Take Profit in 'R'" )
wma_length      = input( 150, 'WMA Bias Length' )

[macd_line, signal_line, hist ] = macd(close, 12, 26, 9)

w_line = wma( close, wma_length )

golong = barssince(crossover(macd_line, signal_line)) <= 5 and ( macd_line < 0 and signal_line < 0 ) and ( close > w_line ) and strategy.opentrades == 0

float stop = na
float tp = na

// For a stop, use a recent low 
stop := golong ? lowest(low, 3)[1] : stop[1]
range = abs(close - stop)
tp := golong ? close + (r_exit * range) : tp[1]


// This is the bit that calculates how much size to use so we only lose 1% of the `strategy.equity`
how_much_willing_to_lose = strategy.equity * capital_risk
// Spread the risk across the stop range 
position_size_in_usd = how_much_willing_to_lose / (range / close)
// Sized specified in base contract
position_size_in_contracts = position_size_in_usd / close

// Enter the position
if golong
    strategy.entry("long", strategy.long, qty=position_size_in_contracts)
    strategy.exit("long exit","long", stop=stop, limit=tp)

// experimental exit strategy
// hist_strength = hist >= 0 ? ( hist[1] < hist ? 'strong' : 'weak') : ( hist[1] < hist ? 'weak' : 'strong' )
// if hist < 0 and hist_strength == '