``` pinescript
/*backtest
start: 2023-08-17 00:00:00
end: 2023-09-16 00:00:00
period: 3h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © mohanee

//@version=4
strategy(title="RSI W Pattern strategy", pyramiding=2, shorttitle="RSI W Pattern", overlay = false)

//Strategy Rules
//ema20 is above ema50
//RSI5 making W pattern in oversold area  or just below 70 level  , you can define the value for parameter buyRsiEntry --- dont go beyond 70
//Exit when RSI reaches 75 

len = input(title="RSI Period", minval=1, defval=5)
buyRsiEntry = input(title="look for W pattern bottom edges well below RSI level (BUY) ", minval=10, defval=65, maxval=70)
//numberOfBars = input(title="Number of Bars in W pattern ", minval=4, defval=4, maxval=6)

emaL = input(title="Long Term EMA", minval=1, defval=50, maxval=200)
emaS = input(title="Short Term EMA", minval=1, defval=20, maxval=200)

stopLoss = input(title="Stop Loss %", minval=1, defval=8, maxval=10)

//rsiWp1=false

myRsi = rsi(close,len)

//longEmaVal=ema(close,emaL)
//shortEmaVal=ema(close,emaS)

entryEma=ema(close,5)  // This is used as filetr for BUY


isEma20AboveEma50=ema(close,emaS)>ema(close,emaL) ? true : false 

//W Pattern
//rsiWp1 =  myRsi>myRsi[1] and myRsi>=30 and myRsi[1]<myRsi[2] and myRsi[2]>myRsi[3]  and myRsi[3]<myRsi[4] //This is published one
rsiWp1 =    myRsi>myRsi[1] and myRsi>=30 and myRsi[1]<myRsi[2] and myRsi[2]>myRsi[3]  and myRsi[3]<myRsi[4] and (low[1]<=low[4] or low[3]<=low[4] ) // looking for recent low

//rsiWp1 =  myRsi>myRsi[1] and myRsi>=30 and myRsi[1]<myRsi[2] and myRsi[2]>myRsi[3]  and myRsi[3]<myRsi[4]  //Ths one has 92% win rate and 4.593 prfit factor

//long condition filters
//1. ema20 > ema50
//2. Rsi5 has W pattern
//3. current RSI <= 65 (parameter buyRsiEntry)  (dont go beyond 70 , becuase that is already overbought area)
//4. current price low/close is below 5 ema --- looking for pullback  -- Optional
longCondition =  isEma20AboveEma50 and rsiWp1   and (myRsi<=buyRsiEntry  and myRsi>=30)  
//and (low<entryEma or close<entryEma)  --- if this optional required , add it to above condition

patternText=" W "

barcolor(longCondition?color.yellow:na)

//initial entry
strategy.entry("RSI_W_LE", comment="Buy" , long=true, when=longCondition  )

//legging in to existing 
strategy.entry("RSI_W_LE",comment="Add", long=true, when=strategy.position_size>0 and crossover(myRsi,10 ))

//calculate stoploss value
stopLossValue=strategy.position_avg_price -  (strategy.position_avg_price*stopLoss/100) 

rsiPlotColor=longCondition ?color.yellow:color.purple

```