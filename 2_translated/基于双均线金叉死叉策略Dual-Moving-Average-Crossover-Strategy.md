```pinescript
plot(doma4 and out4 ? out4: na, color=color.orange, linewidth=2, title="2nd MA")

// Buy and Sell Conditions
longCondition = crossover(out1, out3)
shortCondition = crossunder(out1, out3)

// Stop Loss and Take Profit
stopLoss = strategy.position_avg_price * (1 - profit)
takeProfit = strategy.position_avg_price * (1 + profit)

// Enter Positions
if (longCondition)
    strategy.entry("Long", strategy.long)

if (shortCondition)
    strategy.entry("Short", strategy.short)

// Exit Positions
if (strategy.position_size > 0)
    strategy.exit("Profit Target", "Long", stop=stopLoss, limit=takeProfit)
if (strategy.position_size < 0)
    strategy.exit("Loss Cut", "Short", stop=stopLoss, limit=takeProfit)
```

The above code completes the Pine Script for the dual-moving-average crossover strategy. It includes the conditions for entering and exiting positions based on the crossovers between the fast and slow moving averages, and sets up stop loss and take profit levels to control risk.