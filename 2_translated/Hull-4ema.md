``` pinescript
/*backtest
start: 2022-05-02 00:00:00
end: 2022-05-08 23:59:00
period: 5m
basePeriod: 1m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4

                                            
//                                           


study("Hull-4ema", overlay=true)

// ————— Inputs
price = input(hl2, title="Source")

//for charting the indicator on higher aggregation periods eg. hourly hull on 15 min chart
//comment out the price variable above, and uncomment code below
//note: syminfo.tickerid doesn't work when you are charting a ratio of different tickers eg. ETH/BTC*100

//res = input(title="Resolution",type=input.resolution,defval="60")
//src = input(hl2, title="Source")
//price = security(syminfo.tickerid,res,src)

HMA_Length = input(21, "HMA Length", type=input.integer)
lookback = input(2, "Lookback", type=input.integer)
ShowHullSupResLines = input(false, "Show Hull Support/Resistance Lines", type=input.bool)
ShowBuySellArrows = input(false, "Show Buy/Sell Arrows", type=input.bool)
ShowDivergenceLabel = input(false, "Show Divergence Label", type=input.bool)
ExtendSupResLines = input(false, "Extend Local Support/Resistance Lines", type=input.bool)

// ————— Calculations
HMA = hma(price, HMA_Length)

delta = HMA[1] - HMA[lookback + 1]
delta_per_bar = delta / lookback

next_bar = HMA[1] + delta_per_bar

concavity = if HMA > next_bar then 1 else -1

O_R = if HMA > HMA[1] then '#ff7f00' else '#ff0000'
DG_G = if HMA < HMA[1] then '#025f02' else '#00fa03'

// ————— Plots
plot(HMA, "HMA", color=if concavity != -1 then DG_G else O_R, linewidth=3)

//MA_Min and MA_Max Points only
MA_Min = if HMA > HMA[1] and HMA[1] < HMA[2] then HMA[1] else na
MA_Max = if HMA < HMA[1] and HMA[1] > HMA[2] then HMA[1] else na

//MA_Min and MA_Max Series
saveMA_Min = valuewhen(HMA > HMA[1] and HMA[1] < HMA[2], HMA[1], 0)
saveMA_Max = valuewhen(HMA < HMA[1] and HMA[1] > HMA[2], HMA[1], 0)

//Draw MA_Min/MA_Max as lines from series or just points
plot(extend ? saveMA_Min : MA_Min, "Hull Support", style=shape.circle, color=color.green, linewidth=1, offset=-1)
plot(extend ? saveMA_Max : MA_Max, "Hull Resistance", style=shape.circle, color=color.red, linewidth=1, offset=-1)

//Draw Arrows at MA_Min/MA_Max
plotshape(BuySellArrows ? MA_Min : na, "Buy Signal", shape.triangleup, location.belowbar, color=color.green, text="Buy", offset=-1)
plotshape(BuySellArrows ? MA_Max : na, "Sell Signal", shape.triangledown, location.abovebar, color=color.red, text="Sell", offset=-1)

//Divergence Label
divergence = round(HMA - next_bar, 4)
divergenceColor = if concavity < 0 and divergence > divergence[1]
    color.red
else if concavity < 0 and divergence < divergence[1]
    color.fuchsia
else if concavity > 0 and divergence < divergence[1]
    color.green
else
    color.yellow

labelText = "Divergence:\n" + tostring(divergence)
divergenceLabel = ShowDivergenceLabel ? label.new(x=bar_index, y=close, text=labelText, yloc=yloc.belowbar, color=divergenceColor, textcolor=color.black, style=label.style_label_up, size=size.normal) : na

//label.delete(divergenceLabel[1])

// ————— Alerts
alertcondition(crossover(HMA, saveMA_Min), title="Buy Signal", message="Hull Crossing above MA_Min, Bullish")
alertcondition(crossunder(HMA, saveMA_Max), title="Sell Signal", message="Hull Crossing below MA_Max, Bearish")

if crossover(HMA, saveMA_Min)
    strategy.entry("Enter Long", strategy.long)
else if crossunder(HMA, saveMA_Max)
    strategy.entry("Enter Short", strategy.short)

//


//@version=4

//study(title="4 EMA", shorttitle="4EMA", overlay=true)

len1 = input(8, minval=8, title="Length")
len2 = input(13, minval=8, title="Length")
len3 = input(21, minval=8, title="Length")
len4 = input(55, minval=8, title="Length")

src = input(close, title="Source")

entryema = ema(src, len1)
fastema = ema(src, len2)
mediumema = ema(src, len3)
slowema = ema(src, len4)

plot(entryema, color=color.blue, linewidth=3, title="Entry EMA")
plot(fastema, color=color.purple, linewidth=3, title="Fast EMA")
plot(mediumema, color=color.orange, linewidth=3, title="Medium EMA")
plot(slowema, color=color.yellow, linewidth=3, title="Slow EMA")

//


//study(shorttitle="BB color V1.1", title="Bollinger Bands color V1.1", overlay=true)

length = input(50, minval=1, title="MA - Simple")
src1 = input(close, title="Source")
len = input(2, minval=1, title="MA - Exponential")
mult = input(2.0, minval=0.001, maxval=50)
//pr = input(true, type=bool, title="Price Color" )

//Bollinger Bands
basis = sma(src1, length)
dev = mult * stdev(src1, length)
upper = basis + dev
lower = basis - dev

price1 = ema(src1, len)
linecolor = if price1 >= basis then color.green else color.red


//Affichage

plot(basis, color=color.red, transp=75, title="Moving Average")
p1 = plot(upper, color=color.green, transp=35, title="Upper Band")
p2 = plot(lower, color=color.red, transp=35, title="Lower Band")
```