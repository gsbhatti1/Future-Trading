``` pinescript
/*backtest
start: 2023-01-11 00:00:00
end: 2024-01-17 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/


//@version=2
strategy("Noro's Bands Strategy v1.5", shorttitle = "NoroBands str 1.5", overlay=true)

//Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
len = input(20, defval = 20, minval = 2, maxval = 200, title = "Period")
color = input(true, defval = true, title = "Use ColorBar")
usecb = input(true, defval = true, title = "Use CryptoBottom")
usersi = input(true, defval = true, title = "Use RSI")
usemm = input(true, defval = true, title = "Use min/max")
usepyr = input(true, defval = true, title = "Use pyramiding")
needbb = input(false, defval = false, title = "Show Bands")
needbg = input(false, defval = false, title = "Show Background")
needlo = input(false, defval = false, title = "Show Locomotive")
needpy = input(false, defval = false, title = "Show Avg.price line")
src = close

//Fast RSI
fastup = rma(max(change(src), 0), 2)
fastdown = rma(-min(change(src), 0), 2)
fastrsi = fastdown == 0 ? 100 : fastup == 0 ? 0 : 100 - (100 / (1 + fastup / fastdown))

//CryptoBottom
mac = sma(close, 10)
lencb = abs(close - mac)
sma = sma(lencb, 100)
max = max(open, close)
min = min(open, close)

//PriceChannel
lasthigh = highest(src, len)
lastlow = lowest(src, len)
center = (lasthigh + lastlow) / 2

//dist
dist = abs(src - center)
distsma = sma(dist, len)
hd = center + distsma
ld = center - distsma
hd2 = center + distsma * 2
ld2 = center - distsma * 2

//Trend
trend = close < ld and high < hd ? -1 : close > hd and low > ld ? 1 : trend[1]

//Lines
colo = needbb == false ? na : black
plot(hd2, color = colo, linewidth = 1, transp = 0, title = "High band 2")
plot(hd, color = colo, linewidth = 1, transp = 0, title = "High band")
plot(center, color = colo, linewidth = 1, transp = 0, title = "center")
plot(ld, color = colo, linewidth = 1, transp = 0, title = "Low band")
plot(ld2, color = colo, linewidth = 1, transp = 0, title = "Low band 2")

//Background
col = needbg == false ? na : trend == 1 ? lime : red
bgcolor(col, transp = 80)

//Signals
up = trend == 1 and ((close < open or color == false) or close < hd) and (min < min[1] or usemm == false) and (close < strategy.position_avg_price or usepyr == false or strategy.position_size <= 0) ? 1 : 0
dn = trend == -1 and ((close > open or color == false) or close > ld) and (max > max[1] or usemm == false) and (close > strategy.position_avg_price or usepyr == true) and not na(strategy.position_size) ? 1 : 0

```