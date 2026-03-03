``` pinescript
/*backtest
start: 2023-09-09 00:00:00
end: 2023-09-12 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © mohanee

//@version=4
strategy(title="Aroon Oscillator Strategy", overlay=false, pyramiding=2, initial_capital=10000, currency=currency.USD)  //default_qty_value=10, default_qty_type=strategy.fixed,

//variables BEGIN
aroonLength=input(169,title="Aroon Length")   //square root of 13
rsiLength=input(13, title="RSI Length")
stopLoss = input(title="Stop Loss%", defval=5, minval=1)
//variables  END

//RSI 
rsi13=rsi(close, rsiLength)

// Drawings

//Aroon oscillator
arronUpper = 100 * (highestbars(high, aroonLength+1) + aroonLength)/aroonLength
aroonLower = 100 * (lowestbars(low, aroonLength+1) + aroonLength)/aroonLength

aroonOsc  = arronUpper - aroonLower

aroonMidpoint = 0
oscPlot = plot(aroonOsc, color=color.green)
midLine= plot(aroonMidpoint, color=color.green)
topLine = plot(90,style=plot.style_circles, color=color.green)
bottomLine = plot(-90,style=plot.style_circles, color=color.red)

fill(oscPlot, midLine, color=aroonOsc>0?color.green:color.red, transp=50)
fill(topLine,bottomLine, color=color.blue)


// RSI 
//plot(rsi13, title="RSI", linewidth=2, color=color.purple)
//hline(50, title="Middle Line", linestyle=hline.style_dotted)
//obLevel = hline(80, title="Overbought", linestyle=hline.style_dotted)
//osLevel = hline(30, title="Oversold", linestyle=hline.style_dotted)
//fill(obLevel, osLevel, title="Background", color=rsi13 >=30 ? color.green:color.purple, transp=65)  // longTermRSI >=50


//Entry--
strategy.entry(id="Long Entry", comment="LE", long=true, when=crossover(aroonOsc,0))

//Add
if(strategy.position_size>=1 and close < strategy.position_avg_price and crossover(rsi13,30))
    strategy.order(id="Long Entry", comment="Add") 

stopLossVal= abs(strategy.position_size)>1 ? strategy.position_avg_price*(1-0.5) : 0.00 

//close partial
strategy.close(id="Long Entry", comment="Partial X", qty=strategy.position_size/3, when=abs(strategy.position_size)>=1 and crossunder(aroonOsc, 90))

//close All
strategy.close(id="Long Entry", comment="Exit All", when=abs(strategy.position_size)>stopLossVal)
```

This Pine Script code implements the dual-trend-tracking strategy described in the Chinese document. The script sets up entry conditions based on Aroon oscillator crossovers, adds positions during oversold conditions as indicated by RSI, and includes a stop-loss mechanism.