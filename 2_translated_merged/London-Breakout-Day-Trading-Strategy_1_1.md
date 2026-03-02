> Name

London Breakout Day Trading Strategy London-Breakout-Day-Trading-Strategy

> Author

ChaoZhang

> Strategy Description


[trans]

### Strategy Overview

The London breakout day trading strategy is designed for intraday forex trading, utilizing the price action during the London session with simple breakout logic. It combines specific trading hours and price behavior patterns to generate trade signals for short-term profits.

### Strategy Logic

1. Trade only during London session hours on weekdays, e.g., GMT 0400-0500.
2. Determine short-term trend: go long if there are three consecutive up candles; go short if there are three consecutive down candles.
3. Long signal: Enter a long position when seeing three consecutive up candles.
4. Short signal: Enter a short position when seeing three consecutive down candles.
5. Stop loss/take profit: Set stop loss and take profit at a certain percentage from the entry price.
6. Exit rules: Exit at stop loss/take profit triggers or at the end of the London session.

The strategy solely uses simple breakout signals to capture short-term trends, coupled with strict risk management to control risk/reward per trade.

### Advantages of the Strategy

- Trades only during highly active London hours
- Simple price breakout logic for signals
- Strict stop loss/take profit controls risks
- Avoids low liquidity night and holiday sessions
- Clear entry and exit rules

### Risk Warnings

- Potential issues with premature or delayed entries
- Risks of being trapped in trades
- Opportunities may emerge during nights/holidays 
- Attention needed for key support/resistance levels

### Conclusion

The London breakout day trading strategy is well-suited for short-term intraday trading, avoiding chaotic periods and exiting with profits during high liquidity. With parameter tuning, it can adapt to more assets and serve as an effective short-term trading strategy.

[/trans]

> Strategy Arguments


|Argument        |Default    |Description|
|---------------|-----------|-----------|
|v_input_1       |true       |From Day   |
|v_input_2       |true       |From Month |
|v_input_3       |2000       |From Year  |
|v_input_4       |31         |To Day     |
|v_input_5       |12         |To Month   |
|v_input_6       |2020       |To Year    |
|v_input_7       |0400-0500  |Session    |
|v_input_8       |0300-0900  |eXOT       |
|v_input_9       |false      |Use Heikin Ashi Candles in Algo Calculations|
|v_input_10      |true       |LONG only  |
|v_input_11      |true       |SHORT only |
|v_input_12      |0.005      |Stop Loss  |
|v_input_13      |0.005      |Target Price|
|v_input_14      |true       |Risk % of equity |
|v_input_15      |true       |Monday     |
|v_input_16      |true       |Tuesday    |
|v_input_17      |true       |Wednesday  |
|v_input_18      |true       |Thursday   |
|v_input_19      |true       |Friday     |

> Source (PineScript)

```pinescript
/*backtest
start: 2023-09-07 00:00:00
end: 2023-09-08 09:00:00
period: 30m
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("time zone", overlay=true, initial_capital=1000)
fromDay = input(defval = 1, title="From Day", minval = 1, maxval = 31)
fromMonth = input(defval = 1, title="From Month", minval = 1, maxval = 12)
fromYear = input(defval = 2000, title="From Year", minval = 1970)

// Monday and session
// To Date Inputs
toDay = input(defval = 31, title="To Day", minval = 1, maxval = 31)
toMonth = input(defval = 12, title="To Month", minval = 1, maxval = 12)
toYear = input(defval = 2020, title="To Year", minval = 1970)

startDate = timestamp(fromYear, fromMonth, fromDay, 00, 00)
finishDate = timestamp(toYear, toMonth, toDay, 00, 00)
time_cond = true

s = input(title="Session", type=input.session, defval="0400-0500")
s2 = input(title="eXOT", type=input.session, defval="0300-0900")
t1 = time(timeframe.period, s)
t2 = time(timeframe.period, s2)
c2 = #0000FF
//bgcolor(t1 ? c2 : na, transp=85)

UseHAcandles    = input(false, title="Use Heikin Ashi Candles in Algo Calculations")
//
// === /INPUTS ===

// === BASE FUNCTIONS ===

haClose = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, close) : close
haOpen  = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, open) : open
haHigh  = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, high) : high
haLow   = UseHAcandles ? security(heikinashi(syminfo.tickerid), timeframe.period, low) : low

isMon() => dayofweek(time('D')) == dayofweek.monday
isTue() => dayofweek(time('D')) == dayofweek.tuesday
isWed() => dayofweek(time('D')) == dayofweek.wednesday
isThu() => dayofweek(time('D')) == dayofweek.thursday
isFri() => dayofweek(time('D')) == dayofweek.friday
isSat() => dayofweek(time('D')) == dayofweek.saturday
isSun() => dayofweek(time('D')) == dayofweek.sunday

longe = input(true, title="LONG only")
shorte = input(true, title="SHORT only")
//sl=input(0.001, title="sl % price movement")
//accbalance = strategy.initial_capital + strategy.netprofit


entry = close

sl = input(0.005, title = "Stop Loss")
tp = input(0.005, title="Target Price")

// sldist = entry - sl
// tgdist = tp - entry 
// slper = sldist / entry * 100
// tgper = tgdist / entry * 100

// rr = tgper / slper
// size = accbalance * riskper / slper

balance = strategy.netprofit + 50000 //current balance
floating = strategy.openprofit          //floating profit/loss
risk = input(1,type=input.float,title="Risk % of equity ")           //risk % per trade


temp01 = (balance * risk)/100     //Risk in USD
temp02 = temp01/close*sl      //Risk in lots
temp03 = temp02*100000      //Convert to contracts
size = temp03 - temp03%1000 //Normalize to 1000s (Trade size)
if(size < 1000)
    size := 1000           //Set minimum
```