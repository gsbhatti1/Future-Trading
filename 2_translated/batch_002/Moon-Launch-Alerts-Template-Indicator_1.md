``` pinescript
/*backtest
start: 2022-05-04 00:00:00
end: 2022-05-10 23:59:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © zombie76

//@version=5
indicator("ML Alerts Template [indicator]", shorttitle = "ML Alerts Template [indicator]", overlay=false)


/////////////////////////////////////////////////////////////////////////
tradeshorts = input(title='- *Trade Shorts* - ', defval=true)
tradeexitsignals = input(title='- *Trade Exits* -', defval=true)
/////////////////////////////////////////////////////////////////////////

src = close
source = close

///////////////////// EMA's ////////////////////////
p10=input(title="EMA 1",defval=10)
p200=input(title="EMA 2",defval=200)

ema10=ta.ema(src,p10)
ema200=ta.ema(src,p200)
////////////////////////////////////////////////////


//************* ATR ***************//
lengthatr = input(12, title="ATR Length") 

atr = ta.rma(ta.tr(true), lengthatr)
ema = ta.ema(src, lengthatr)

emaPlus1Atr = ema + atr
emaMinus1Atr = ema - atr

//************ END ATR ***********//


////////////////////////////// HIST ///////////////////////////////////

fastLengthHist = input(title='Hist Fast Length',defval=12)
slowLengthHist=input(title='Hist Slow Length',defval=26)
signalLength=input(title='Hist Signal Length',defval=9)

fastMA = ta.ema(source, fastLengthHist)
slowMA = ta.ema(source, slowLengthHist)

macd = fastMA - slowMA
signal = ta.sma(macd, signalLength)
hist = macd - signal

///////////////////////////////////////////////////////////////////


//////////////////////////////////////////////////
//// INPUT YOUR BUY/SELL/EXIT SIGNALS HERE: ////
//////////////////////////////////////////////////

tradeups = ema10 > ema10[1] and src < emaMinus1Atr and hist > hist[1] // LONG
tradeexits = tradeexitsignals and (ema10 < ema10[1]) and not tradeups // Exit Long
tradedowns = ((ema10 < ema10[1] and hist < hist[1]) or (src > emaPlus1Atr and close < emaPlus1Atr and close < open and hist < hist[1])) and not tradeups // SHORT
exitshort = src < emaMinus1Atr and close > open and ema10 > ema10[1] and hist > hist[1] // Exit Short

//////////////////////////////////////////////////
//////////////////////////////////////////////////


///////////////////////////////// Buy Sell Line ///////////////////////////////////////////
////////////////////////// DO NOT EDIT ANYTHING BELOW /////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////


// Filters out signals if opposite signal is also on:
heikDownColor() => tradedowns
heikUpColor() => tradeups
heikExitColor() => tradeexitsignals and tradeexits

previnashort = 0
previnalong = 0
previnaexit = 0


// Heiki Down Filter //    
//short//
inashort_filt = heikDownColor() and tradeshorts and not heikUpColor()
previnashort := inashort_filt ? 1 : heikUpColor() ? -1 : previnashort[1]
inashort2 = previnashort[1] == 1

// Heiki Up Filter //
//long//
inalong_filt = heikUpColor() and not (heikDownColor() or tradeexits)
previnalong := inalong_filt ? 1 : heikDownColor() ? -1 : previnalong[1]
inalong2 = previnalong[1] == 1

// Heiki Exit Filter //
//exit//
inaexit_filt = heikExitColor() and not heikDownColor() and not (heikUpColor() or tradeups)
previnaexit := inaexit_filt ? 1 : heikDownColor() or heikUpColor() ? -1 : previnaexit[1]
inaexit2 = previnaexit[1] == 1

// Heiki Exit Filter 2 //
//exit short//
previnasexits = 0
inasexits_filt = exitshort and (inashort2 or tradedowns) and not tradeups //and not tradedowns[1]
previnasexits := inasexits_filt ? 1 : heikDownColor() or heikUpColor() ? -1 : previnasexits[1]
inasexit2 = previnasexits[1] == 1 //and not exitshort[1]

/////////////////////////////////////////////////////// 

heikDownColor_filt = (heikDownColor() and not heikUpColor()) or (heikDownColor() and not heikExitColor())
heikUpColor_filt = tradeups or ((heikUpColor() or inalong2) and
```