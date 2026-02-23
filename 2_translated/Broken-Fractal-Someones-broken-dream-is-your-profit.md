> Name

Broken-Fractal-Someones-broken-dream-is-your-profit

> Author

ChaoZhang

> Strategy Description

Idea  
The idea is simple: when the market turns around, it catches many traders off guard. We trade alongside them, in the same direction as their exits!

Method  
We allow the market to first form a fractal.  
Then we let the market create an opposite fractal.  
Next, we let the market break through the initial fractal, trapping numerous trades during this move.  
Finally, we patiently wait until the market offers these trapped traders a chance to exit—and we enter in that same direction.

How to Use?  
Green boxes indicate long entries; red boxes signal short entries.  
When a box appears, that defines your risk parameters—place limit orders accordingly and follow the trend!  
This strategy works across all timeframes.

If you find this script useful, feel free to share how you're applying it.  
Personally, I combine it with higher timeframe bias for better results.

P.S.1 Some traders refer to this pattern as "Break of Market Structure" or simply "Breaker." I prefer calling it "Broken Fractal."  
P.S.2 A break of a previously broken fractal can also be extremely powerful—stay alert for such setups!

**Backtest**

![IMG](https://www.fmz.com/upload/asset/13522764fc0126952eb.png)

> Strategy Arguments

| Argument            | Default | Description                   |
|---------------------|---------|-------------------------------|
| v_input_1           | 2       | n==1 or 2                     |
| v_input_2           | false   | bgColor                       |
| v_input_3           | true    | drawBoxes                     |
| v_input_4           | true    | showBullishSignal             |
| v_input_5           | true    | showBearishSignal             |

> Source (PineScript)

``` pinescript
/*backtest
start: 2022-02-24 00:00:00
end: 2022-05-24 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © makuchaku

//@version=4
study("Broken Fractal", overlay=true)
n = input(title="n==1 or 2", defval=2, type=input.integer)
bgColor = input(title="bgColor", type=input.bool, defval=false)
drawBoxes = input(title="drawBoxes", type=input.bool, defval=true)
showBullishSignal = input(title="showBullishSignal", type=input.bool, defval=true)
showBearishSignal = input(title="showBearishSignal", type=input.bool, defval=true)

var fractalCounter = 0
var highAtDownFractal = 0.0
var lowAtUpFractal = 0.0

downFractal = (n == 2 ? (high[n-2] < high[n]) and (high[n-1] < high[n]) and (high[n+1] < high[n]) and (high[n+2] < high[n]) : (high[1] > high[0]) and (high[1] > high[2]))
// plotchar(downFractal, char='⮝', location=location.abovebar, offset=-1*n, color=color.red, transp=0, title="Down Fractal") 
if downFractal
    //line.new(x1=bar_index-1, y1=high[n], x2=bar_index, y2=high[n], extend=extend.none, color=color.silver, style=line.style_solid, width=1)
    if fractalCounter > 0
        fractalCounter := 0
    highAtDownFractal := high[n]
    fractalCounter := fractalCounter - 1

upFractal = (n == 2 ? (low[n-2] > low[n]) and (low[n-1] > low[n]) and (low[n+1] > low[n]) and (low[n+2] > low[n]) : (low[1] < low[0]) and (low[1] < low[2]))
// plotchar(upFractal, char='⮟', location=location.belowbar, offset=-1*n, color=color.green, transp=0, title="Up Fractal")
if upFractal
    //line.new(x1=bar_index-1, y1=low[n], x2=bar_index, y2=low[n], extend=extend.none, color=color.silver, style=line.style_solid, width=1)
    if fractalCounter < 0
        fractalCounter := 0
    lowAtUpFractal := low[n]
    fractalCounter := fractalCounter + 1

sellSignal = (fractalCounter < 0) and (open > lowAtUpFractal) and (close < lowAtUpFractal)
//bgcolor(color=(sellSignal and bgColor and showBearishSignal ? color.red : na), transp=80)
//                      if sellSignal and drawBoxes and showBearishSignal
    //box.new(left=bar_index, top=lowAtUpFractal, right=bar_index+10, bottom=highAtDownFractal, bgcolor=color.new(color.red, 90), border_color=color.new(color.red, 10))


buySignal = (fractalCounter >= 1) and crossover(close, highAtDownFractal)
//bgcolor(color=(buySignal and bgColor and showBullishSignal ? color.green : na), transp=80)
//if buySignal and drawBoxes and showBullishSignal
    //box.new(left=bar_index, top=highAtDownFractal, right=bar_index+10, bottom=lowAtUpFractal, bgcolor=color.new(color.green, 90), border_color=color.new(color.green, 10))




if buySignal
    strategy.entry("Enter Long", strategy.long)
else if sellSignal
    strategy.entry("Enter Short", strategy.short)
```

> Detail

https://www.fmz.com/strategy/365695

> Last Modified

2022-05-25 17:21:02