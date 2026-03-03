```markdown
### Strategy Overview

The Renko reversal tracking strategy is a short-term trading strategy that utilizes Renko bricks to identify market reversals. It captures short-term reversal opportunities by monitoring color changes between adjacent bricks. Trading signals are generated when the current brick's color flips after consecutive same-colored bricks.

### Strategy Logic

1. Use traditional non-repainting Renko bricks.
2. Monitor color changes between neighboring bricks.
3. Signals emerge when the current brick's color flips while the previous two bricks share the same color.
4. Long signal: A bullish brick appears after two bearish bricks, indicating a potential uptrend.
5. Short signal: A bearish brick appears after two bullish bricks, indicating a potential downtrend.
6. Entry options: market order or stop order.
7. Set stop loss and take profit levels at multiples of the Renko brick size.

The core idea is to capitalize on pullback opportunities caused by changes in brick color. Consecutive same-colored bricks represent trend formation, while a subsequent flip in color suggests potential reversals.

The Renko brick size and the stop loss/take profit coefficients can be adjusted to optimize the strategy's performance.

### Advantages of the Strategy

- Bricks directly display reversal information.
- Simple and clear logic, easy to implement.
- Symmetrical long and short opportunities.
- Flexible adjustment of Renko brick size.
- Strict risk control with stop loss and take profit settings.

### Risk Warnings

- Requires a certain number of consecutive bricks to form signals.
- The Renko brick size directly impacts profitability and drawdowns.
- It is challenging to predict the duration of trends.
- There may be instances of consecutive stop losses.

### Conclusion

The Renko reversal tracking strategy innovatively applies traditional technical indicators by directly using changes in brick color to identify short-term reversals. This simple and practical approach can achieve stable returns through parameter tuning, making it worth backtesting, live optimization, and application.
```

```pinescript
//@version=3
// Simple Renko strategy, very profitable. Thanks to vacalo69 for the idea.
// Rules when the strategy opens order at market as follows:
//- Buy when previous brick (-1) was bearish and previous brick (-2) was bearish too and actual brick close is bullish
//- Sell when previous brick (-1) was bullish and previous brick (-2) was bullish too and actual brick close is bearish
// Rules when the strategy sends stop order are the same but this time a stop buy or stop sell is placed (better overall results).
// Note that strategy open an order only after that condition is met, at the beginning of next candle, so the actual close is not the actual price.
// Only input is the brick size multiplier for stop loss and take profit: SL and TP are placed at (brick size)x(multiplier) Or put it very high if you want startegy to close order on opposite signal.
// Adjust brick size considering:
//- Strategy works well if there are three or more consecutive bricks of same "color"
//- Expected Profit
//- Drawdown
//- Time on trade

// Study with alerts, MT4 expert advisor and jforex automatic strategy are available at request.

strategy("Renko Strategy Open_Close", overlay=true, calc_on_every_tick=true, pyramiding=0,default_qty_type=strategy.percent_of_equity,default_qty_value=100,currency=currency.USD)

// INPUTS
Multiplier=input(1,minval=0, title='Brick size multiplier: use high value to avoid SL and TP')
UseStopOrders=input(true,title='Use stop orders instead of market orders')

// CALCULATIONS
BrickSize=abs(open[1]-close[1])
targetProfit = 0
targetSL = 0

// STRATEGY CONDITIONS
longCondition = open[1]>close[1] and close>open and open[1]<open[2]
shortCondition = open[1]<close[1] and close<open and open[1]>open[2]

// STRATEGY
if (longCondition and not UseStopOrders)
    strategy.entry("LongBrick", strategy.long)
    targetProfit=close+BrickSize*Multiplier
    targetSL=close-BrickSize
    strategy.exit("CloseLong","LongBrick", limit=targetProfit, stop=targetSL)
    
if (shortCondition and not UseStopOrders)
    strategy.entry("ShortBrick", strategy.short)
    targetProfit = close-BrickSize*Multiplier
    targetSL = close+BrickSize
    strategy.exit("CloseShort","ShortBrick", limit=targetProfit, stop=targetSL)

if (longCondition and UseStopOrders)
    strategy.entry("LongBrick_Stop", strategy.long, stop=open[2])
    targetProfit=close+BrickSize*Multiplier
    targetSL=close-BrickSize
    strategy.exit("CloseLong","LongBrick_Stop", limit=targetProfit, stop=targetSL)
    
if (shortCondition and UseStopOrders)
    strategy.entry("ShortBrick_Stop", strategy.short, stop=open[2])
    targetProfit = close-BrickSize*Multiplier
    targetSL = close+BrickSize
    strategy.exit("CloseShort","ShortBrick_Stop", limit=targetProfit, stop=targetSL)
```

> Detail

https://www.fmz.com/strategy/426927

> Last Modified

2023-09-1
```