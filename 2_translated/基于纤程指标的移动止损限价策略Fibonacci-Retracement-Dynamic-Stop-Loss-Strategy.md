``` pinescript
/*backtest
start: 2024-01-06 00:00:00
end: 2024-02-05 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © CryptoRox

//@version=4
//Paste the line below in your alerts to run the built-in commands.
//{{strategy.order.alert_message}}
strategy(title="Fibs limit only", shorttitle="Strategy", overlay=true, precision=8, pyramiding=1000, commission_type=strategy.commission.percent, commission_value=0.04)

//Settings 
testing = input(false, "Live")
//Use epochconverter or something similar to get the current timestamp.
starttime = input(1600976975, "Start Timestamp") * 1000
//Wait XX seconds from that timestamp before the strategy starts looking for an entry.
seconds = input(60, "Start Delay") * 1000
testPeriod = true


leverage = input(1, "Leverage")
tp = input(1.0, "Take Profit %") / leverage
dca = input(-1.0, "DCA when < %") / leverage *-1
fibEntry = input("1", "Entry Level", options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])

//Strategy Calls
equity = strategy.equity
avg = strategy.position_avg_price
symbol = syminfo.tickerid
openTrades = strategy.opentrades
closedTrades = strategy.closedtrades
size = strategy.position_size

//Fibs
lentt = input(60, "Pivot Length")
h = highest(lentt)
h1 = dev(h, lentt) ? na : h
hpivot = fixnan(h1)
l = lowest(lentt)
l1 = dev(l, lentt) ? na : l
lpivot = fixnan(l1)
z = 400
p_offset= 2
transp = 60
a=(low
```