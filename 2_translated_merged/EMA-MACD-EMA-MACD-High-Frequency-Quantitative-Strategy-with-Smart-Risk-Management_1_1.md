<!-- AUTO-TRANSLATED BACKTEST CONFIGURATION -->
```pine
//@version=5
strategy("High-Frequency Trade Script with EMA, MACD, and ATR-based TP/SL", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=2, initial_capital=100000)

// Indicator Setup
emaBuy = ta.ema(close, 9)       // Short period EMA for buying
emaSell = ta.ema(close, 21)     // Long period EMA for selling
[macdLine, signalLine, _] = ta.macd(close, 6, 13, 4) // MACD with short periods
atr = ta.atr(14)  // Calculate ATR indicator

// Stop loss and take profit ratio setup
stopLossATRMultiplier = 1.5  // Reduce stop loss to 1.5 * ATR
riskToRewardRatio = 2.0  // Risk-reward ratio 1:2

// Risk Management Setup
riskPercentage = 1.0  // Risk as 1% of capital
capital = strategy.equity  // Total capital
riskAmount = capital * (riskPercentage / 100)  // Risk amount

// Buy signal conditions: Short EMA crosses above long EMA and MACD above Signal
longCondition = ta.crossover(emaBuy, emaSell) and macdLine > signalLine

// Sell signal conditions: Short EMA crosses below long EMA and MACD below Signal
shortCondition = ta.crossunder(emaBuy, emaSell) and macdLine < signalLine

// --- Automatically execute buy and sell orders with stop loss and take profit --- //
// Define stop loss and take profit lines
var line longStopLossLine = na
var line longTakeProfitLine = na
var line shortStopLossLine = na
var line shortTakeProfitLine = na

if (longCondition)
    longEntryPrice = close  // Entry price for buying
    longStopLoss = longEntryPrice - (atr * stopLossATRMultiplier)  // Stop loss based on ATR
    longTakeProfit = longEntryPrice + ((longEntryPrice - longStopLoss) * riskToRewardRatio)  // Take profit at 1:2 ratio

    // Calculate position size based on risk amount
    positionSize = riskAmount / (longEntryPrice - longStopLoss)  // Contract size

    // Place buy order
    strategy.entry("Buy", strategy.long, qty=positionSize)
    
    // Set stop loss and take profit orders
    strategy.exit("Take Profit/Stop Loss", "Buy", stop=longStopLoss, limit=longTakeProfit)

    // Draw stop loss and take profit lines
    // longStopLossLine := line.new(bar_index, longStopLoss, bar_index + 1, longStopLoss, color=color.red, width=1, style=line.style_dashed)  // Stop loss line
    // longTakeProfitLine := line.new(bar_index, longTakeProfit, bar_index + 1, longTakeProfit, color=color.green, width=1, style=line.style_dashed)  // Take profit line

if (shortCondition)
    shortEntryPrice = close  // Entry price for selling
    shortStopLoss = shortEntryPrice + (atr * stopLossATRMultiplier)  // Stop loss based on ATR
    shortTakeProfit = shortEntryPrice - ((shortStopLoss - shortEntryPrice) * riskToRewardRatio)  // Take profit at 1:2 ratio

    // Calculate position size based on risk amount
    positionSize = riskAmount / (shortStopLoss - shortEntryPrice)  // Contract size

    // Place sell order
    strategy.entry("Sell", strategy.short, qty=positionSize)
    
    // Set stop loss and take profit orders
    strategy.exit("Take Profit/Stop Loss", "Sell", stop=shortStopLoss, limit=shortTakeProfit)

    // Draw stop loss and take profit lines
    // shortStopLossLine := line.new(bar_index, shortStopLoss, bar_index + 1, shortStopLoss, color=color.red, width=1, style=line.style_dashed)  // Stop loss line
    // shortTakeProfitLine := line.new(bar_index, shortTakeProfit, bar_index + 1, shortTakeProfit, color=color.green, width=1, style=line.style_dashed)  // Take profit line

// --- Plot separate indicators --- //
plot(emaBuy, title="EMA Buy (9)", color=color.green, linewidth=2)   // Buy EMA
plot(emaSell, title="EMA Sell (21)", color=color.red, linewidth=2)  // Sell EMA
plot(macdLine, title="MACD Line", color=color.blue, linewidth=1)    // MACD Line
plot(signalLine, title="Signal Line", color=color.orange, linewidth=1)  // Signal Line
```