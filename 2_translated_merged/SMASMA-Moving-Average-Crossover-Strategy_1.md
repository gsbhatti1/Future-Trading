``` pinescript
``` pinescript
//@version=3
//study(title="MA Crossover Strategy", overlay = true)
// Simple MA crossover strategy with a 10/100 MA crossover)

strategy("MA Crossover Strategy", overlay=true)
src = input(close, title="Source")

price = security(syminfo.tickerid, timeframe.period, src)
ma1 = input(10, title="1st MA Length")
type1 = input("SMA", "1st MA Type", options=["SMA", "EMA"])

ma2 = input(100, title="2nd MA Length")
type2 = input("SMA", "2nd MA Type", options=["SMA", "EMA"])

price1 = if (type1 == "SMA")
    sma(price, ma1)
else
    ema(price, ma1)
    
price2 = if (type2 == "SMA")
    sma(price, ma2)
else
    ema(price, ma2)

longCondition = price1 > price2 and not crossover(price1, price2) ? true : false
shortCondition = price1 < price2 and not crossunder(price1, price2) ? true : false

if (longCondition)
    strategy.entry("Long", strategy.long)
    
if (shortCondition)
    strategy.entry("Short", strategy.short)

// Plot the SMAs on the chart
plot(price1, title="SMA 10", color=color.blue)
plot(price2, title="SMA 100", color=color.red)
```
```