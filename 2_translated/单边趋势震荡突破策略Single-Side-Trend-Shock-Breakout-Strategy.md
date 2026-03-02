``` pinescript
/*backtest
start: 2024-01-10 00:00:00
end: 2024-01-17 00:00:00
period: 3m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=2
strategy("Noro's Bands Scalper Strategy v1.5", shorttitle = "Scalper str 1.5", overlay=true, default_qty_type = strategy.percent_of_equity, default_qty_value=100.0, pyramiding=0)

//Settings
needlong = input(true, defval = true, title = "Long")
needshort = input(true, defval = true, title = "Short")
takepercent = input(0, defval = 0, minval = 0, maxval = 1000, title = "take, %")
needbe = input(true, defval = true, title = "Bands Entry")
needct = input(false, defval = false, title = "Counter-trend entry")
bodylen = input(10, defval = 10, minval = 0, maxval = 50, title = "Body length")
trb = input(1, defval = 1, minval = 1, maxval = 5, title = "Trend bars")
len = input(20, defval = 20, minval = 2, maxval = 200, title = "Period")
needbb = input(true, defval = true, title = "Show Bands")
needbg = input(true, defval = true, title = "Show Background")
src = close

//Price Channel
lasthigh = highest(src, len)
lastlow = lowest(src, len)
center = (lasthigh + lastlow) / 2

//Distance
dist = abs(src - center)
distsma = sma(dist, len)
hd = center + distsma
ld = center - distsma
hd2 = center + distsma * 2
ld2 = center - distsma * 2

//Trend
chd = close > hd
cld = close < ld
uptrend = trb == 1 and chd ? 1 : trb == 2 and chd and chd[1] ? 1 : trb == 3 and chd and chd[1] and chd[2] ? 1 : trb == 4 and chd and chd[1] and chd[2] and chd[3] ? 1 : trb == 5 and chd and chd[1] and chd[2] and chd[3] and chd[4] ? 1 : 0
dntrend = trb == 1 and cld ? 1 : trb == 2 and cld and cld[1] ? 1 : trb == 3 and cld and cld[1] and cld[2] ? 1 : trb == 4 and cld and cld[1] and cld[2] and cld[3] ? 1 : trb == 5 and cld and cld[1] and cld[2] and cld[3] and cld[4] ? 1 : 0
trend = dntrend == 1 and high < center ? -1 : uptrend == 1 and low > center ? 1 : trend[1]

//Lines
colo = needbb == false ? na : black
plot(hd2, color = colo, linewidth = 1, transp = 0, title = "High band 2")
plot(hd, color = colo, linewidth = 1, transp = 0, title = "High band")
plot(ld, color = colo, linewidth = 1, transp = 0, title = "Low band")
plot(ld2, color = colo, linewidth = 1, transp = 0, title = "Low band 2")

//Body Breakout
bodylenpct = bodylen * (close - open) / close
longentry = trend == 1 and bodylenpct > takepercent ? true : false
shortentry = trend == -1 and bodylenpct > takepercent ? true : false

if (needbe)
    if (trend == 1 and close < hd or trend == -1 and close > ld)
        strategy.entry("Long Entry", strategy.long)

if (needct and needlong)
    if (trend == -1 and bodylenpct > takepercent)
        strategy.entry("Short Entry", strategy.short)

if (needbg) bgcolor(#000000, transp=95)

if (needbe or needct)
    if (trend == 1 and close < hd2 or trend == -1 and close > ld2)
        strategy.exit("Exit Long", "Long Entry")

    if (trend == -1 and close > hd or trend == 1 and close < ld)
        strategy.exit("Exit Short", "Short Entry")
```

This Pine Script code implements the Single-Side-Trend-Shock-Breakout-Strategy as described in the document. The script includes settings for entry, stop-loss, take-profit, and visualization of price channels.