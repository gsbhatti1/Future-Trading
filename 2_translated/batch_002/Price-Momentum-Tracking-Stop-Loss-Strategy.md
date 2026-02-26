``` pinescript
/*backtest
start: 2023-01-01 00:00:00
end: 2023-02-03 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("Trailing Stop Snippet", overlay=true)

length = input(12)
price = close
momentum(seria, length) =>
	mom = seria - seria[length]
	mom
mom0 = momentum(price, length)
mom1 = momentum(mom0, 1)

tsact = input.float(0.0, "Trailing Stop Activation |", group="strategy", tooltip="Activates the Trailing Stop once this PnL is reached.") / 100
tsact := tsact ? tsact : na
ts = input.float(0.0, "Position Trailing Stop |", group="strategy", tooltip="Trails your position with a stop loss at this distance from the highest PnL") / 100
ts := ts ? ts : na

in_long = strategy.position_size > 0
in_short = strategy.position_size < 0

var ts_ = array.new_float()
ts_size = array.size(ts_)
ts_get = ts_size > 0 ? array.get(ts_, ts_size - 1) : 0

if in_long
    if tsact and high > strategy.position_avg_price + strategy.position_avg_price * tsact
        if ts_size > 0 and ts_get < high
            array.push(ts_, high)
        if ts_size < 1
            array.push(ts_, high)
    if not tsact
        if ts_size > 0 and ts_get < high
            array.push(ts_, high)
        if ts_size < 1
            array.push(ts_, high)
if in_short
    if tsact and low < strategy.position_avg_price - strategy.position_avg_price * tsact
        if ts_size > 0 and ts_get > low
            array.push(ts_, low)
        if ts_size < 1
            array.push(ts_, low)
    if not tsact
        if ts_size > 0 and ts_get > low
            array.push(ts_, low)
        if ts_size < 1
            array.push(ts_, low)
    
trail = in_
```