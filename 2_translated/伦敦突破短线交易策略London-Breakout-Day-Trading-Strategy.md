> Name

London Breakout Day Trading Strategy

> Author

ChaoZhang

> Strategy Description


### Strategy Overview

The London breakout day trading strategy is designed for forex intraday trading, leveraging the price action during the London session with simple breakout logic. It combines specific trading hours and price behavior patterns to generate trade signals and seek short-term profits.

### Strategy Logic

1. Trade only during London session hours on weekdays, e.g., GMT 0400-0500.
2. Determine short-term trend: go long on 3 consecutive up candles; go short on 3 consecutive down candles.
3. Long signal: enter a long position when seeing 3 consecutive up candles.
4. Short signal: enter a short position when seeing 3 consecutive down candles.
5. Stop loss/take profit: set stop loss and take profit at a certain percentage from the entry price.
6. Exit rules: exit on stop loss or take profit triggers, or at the end of the London session.

The strategy purely uses simple breakout signals to capture short-term trends with strict risk management to control risks per trade.

### Advantages of the Strategy

- Trades only during highly active London hours
- Simple price breakout logic for signals
- Strict stop loss/take profit controls risks
- Avoids low liquidity night and holiday sessions
- Clear entry and exit rules

### Risk Warnings

- Potential premature or delayed entry issues
- Risks of being trapped
- Opportunities may emerge during nights/holidays 
- Key support/resistance levels need attention

### Conclusion

The London breakout day trading strategy is well-suited for short-term intraday trading, avoiding chaotic periods and exiting with profits during high liquidity. With parameter tuning, it can adapt to more assets as an effective short-term trading strategy.

||

### Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|From Day|
|v_input_2|true|From Month|
|v_input_3|2000|From Year|
|v_input_4|31|To Day|
|v_input_5|12|To Month|
|v_input_6|2020|To Year|
|v_input_7|0400-0500|Session|
|v_input_8|0300-0900|eXOT|
|v_input_9|false|Use Heikin Ashi Candles in Algo Calculations|
|v_input_10|true|LONG only|
|v_input_11|true|SHORT only|
|v_input_12|0.005|Stop Loss|
|v_input_13|0.005|Target Price|
|v_input_14|true|Risk % of equity |
|v_input_15|true|Monday|
|v_input_16|true|Tuesday|
|v_input_17|true|Wednesday|
|v_input_18|true|Thursday|
|v_input_19|true|Friday|


> Source (PineScript)

```pinescript
//@version=4
strategy("time zone", overlay=true, initial_capital=1000)
fromDay = input(defval = 1, title = "From Day", minval = 1, maxval = 31)
fromMonth = input(defval = 1, title = "From Month", minval = 1, maxval = 12)
fromYear = input(defval = 2000, title = "From Year", minval = 1970)

toDay = input(defval = 31, title = "To Day", minval = 1, maxval = 31)
toMonth = input(defval = 12, title = "To Month", minval = 1, maxval = 12)
toYear = input(defval = 2020, title = "To Year", minval = 1970)

startDate = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finishDate = timestamp(toYear, toMonth, toDay, 00, 00)
time_cond = true

s = input(title="Session", type=input.session, defval="0400-0500")
s2 = input(title="eXOT", type=input.session, defval="0300-0900")
t1 = time(timeframe.period, s)
t2 = time(timeframe.period, s2)

haClose = iff(UseHAcandles, security(heikinashi(syminfo.tickerid), timeframe.period, close), close)
haOpen  = iff(UseHAcandles, security(heikinashi(syminfo.tickerid), timeframe.period, open), open)
haHigh  = iff(UseHAcandles, security(heikinashi(syminfo.tickerid), timeframe.period, high), high)
haLow   = iff(UseHAcandles, security(heikinashi(syminfo.tickerid), timeframe.period, low), low)

isMon() => dayofweek(time('D')) == dayofweek.monday
isTue() => dayofweek(time('D')) == dayofweek.tuesday
isWed() => dayofweek(time('D')) == dayofweek.wednesday
isThu() => dayofweek(time('D')) == dayofweek.thursday
isFri() => dayofweek(time('D')) == dayofweek.friday
isSat() => dayofweek(time('D')) == dayofweek.saturday
isSun() => dayofweek(time('D')) == dayofweek.sunday

longe = input(true, title="LONG only")
shorte = input(true, title="SHORT only")

entry = close

sl = input(0.005, title = "Stop Loss")
tp = input(0.005, title="Target Price")

balance = strategy.netprofit + 50000 //current balance
floating = strategy.openprofit          //floating profit/loss
risk = input(1,type=input.float,title="Risk % of equity ")           //risk % per trade

temp01 = (balance * risk)/100     //Risk in USD
temp02 = temp01/close*sl      //Risk in lots
temp03 = temp02*100000      //Convert to contracts
size = temp03 - temp03%1000 //Normalize to 1000s (Trade size)
if(size < 1000)
    size := 1000           //Set minimum size

// trading logic
if(t1 and isMon() and longe)
    strategy.entry("Long", strategy.long, when=haClose[1] > haOpen[2] and haClose[2] > haOpen[1])
    strategy.exit("SL/TP Long", "Long", stop=haLow[1]*sl, limit=haHigh[1]*(1+tp))

if(t2 and isMon() and shorte)
    strategy.entry("Short", strategy.short, when=haClose[1] < haOpen[2] and haClose[2] < haOpen[1])
    strategy.exit("SL/TP Short", "Short", stop=haHigh[1]*(1-sl), limit=haLow[1]*tp)
```

This Pine Script implementation captures the logic described in the original document, ensuring all code blocks remain as-is.