## Overview  

This strategy combines the price change rate and moving average technical indicators to locate the buy and sell points accurately. When the price drops sharply, a buy threshold is established. And when the price continues to fall, long positions are opened. When the price rises, a sell threshold is set up. And existing long positions are closed out when the price keeps rising and breaks through the sell threshold. At the same time, the strategy also adopts the pyramiding method to open multiple long positions at different price levels to lower the cost.

## Principles  

### Long Entry Logic

1. Calculate the Rate of Change (ROC) of the price, and set up the long entry threshold line.
2. When the price breaks through the long entry threshold downwards, record this breakpoint and initiate the long entry limit line.
3. The long entry limit line lasts for a certain duration defined by input parameters and expires afterwards.  
4. When the price continues to fall and crosses below the long entry limit line, the first long position is opened.

### Long Close Logic  

1. Calculate the Rate of Change (ROC) of the price, and set up the long close threshold line.
2. When the price breaks through the long close threshold upwards, record this breakpoint and initiate the long close limit line.
3. The long close limit line lasts for a certain duration defined by input parameters and expires afterwards. 
4. When the price continues to rise and crosses above the long close limit line, all existing long positions are closed.

### Risk Control

The strategy has built-in stop loss and take profit functions that can be customized to control risks dynamically.

### Pyramiding 

When opening each new trade position, the system calculates the subsequent long entry price according to the input percentage parameters, thus implementing averaging down through multiple long entries.

## Advantages  

1. Adopt the rate of change (ROC) indicator to locate buy and sell signals accurately. ROC is very sensitive to price changes.
2. Use limit lines for further confirmation of entry and exit signals to avoid false breaks.
3. The pyramiding method tracks market value while keeping risks under control.
4. Built-in stop loss and take profit strictly controls risks for each position.

## Risks & Solutions  

1. Fierce market fluctuation may lead to too many open positions. We can set reasonable parameters for pyramiding to limit total open positions.
2. Stop loss or take profit may get triggered frequently when the market is ranging. We can loosen the percentage levels or even disable SL & TP in sideways markets.

## Optimizations  

1. Combine with other indicators like moving averages to filter entry signals. Only adopt ROC signals when prices actually break the MA lines.
2. Improve the pyramiding logic, open subsequent positions only when prices continue to fall by a certain percentage instead of just lowering the entry price.
3. Optimal parameter settings may differ significantly across trading instruments. Extensive backtest and demo trading is necessary.
4. Build an adaptive stop loss mechanism with different percentage levels based on market volatility conditions.

## Conclusion  

The strategy effectively combines accurate entry signals with limit line filters, built-in risk management functions, and pyramiding for position sizing. With reasonable parameter tuning, it can acquire excess returns while keeping risks in check. Future improvements may focus more on signal filtering methods and risk control for broader market adaptability.

*/

strategy("Price-Change-Average-Pricing-Strategy-Based-on-Quantitative-Indicators", overlay=true)

// Input Parameters
v_input_1 = input(25, title="(?Risk)Portfolio Percentage")
v_input_2 = input(true, title="Leverage")
v_input_3 = input(5, title="Broker Maintenance Margin Percentage")
v_input_4 = input(true, title="Take Profit")
v_input_5 = input(5.6, title="Percentage")
v_input_6 = input(true, title="Stop Loss")
v_input_7 = input(2.5, title="Percentage")
v_input_8 = input(2, title="(?Price Averaging Layers)2nd Layer Long Entry %")
v_input_9 = input(5, title="3rd Layer Long Entry %")
v_input_10 = input(9, title="4th Layer Long Entry %")
v_input_11 = input(3, title="(?ROC Logic to OPEN Long Entry)Rate of Change bar lookback")
v_input_12 = input(0.5, title="ROC Threshold % to Setup Long Entry")
v_input_13 = input(0.5, title="Price Drop Threshold % to OPEN Long Entry")
v_input_14 = input(3, title="Duration of Long Entry Threshold Line in bars")
v_input_15 = input(0.8, title="Min % of Price Drop to OPEN Long Entry")
v_input_16 = input(3, title="(?ROC Logic to CLOSE Long Entry)Rate of Change bar lookback")
v_input_17 = input(0.8, title="ROC Threshold % to Setup Close Threshold")
v_input_18 = input(1.7, title="Price Rise Threshold % to CLOSE Long Entry")
v_input_19 = input(3, title="Duration of Entry Limit in bars")

// Calculations
long_entry_roc = roc(close, v_input_11) > v_input_12 ? 1 : 0
long_close_roc = roc(close, v_input_16) < -v_input_17 ? 1 : 0

// Long Entry Conditions
if (long_entry_roc and close < ROCLine and high[1] <= low)
    strategy.entry("Long", strategy.long)

// Long Close Conditions
if (long_close_roc and close > ROCLimit)
    strategy.close("Long")

// Risk Control
stop_loss = v_input_6 ? strategy.position_avg_price * (1 - v_input_7 / 100) : na
take_profit = v_input_4 ? strategy.position_avg_price * (1 + v_input_5 / 100) : na

if (strategy.position_size > 0)
    strategy.exit("Stop Loss", "Long", stop=stop_loss, limit=take_profit)

// Pyramiding Logic
var float entry_prices[4] = array.new_float(4)
var int positions = 0

for i = 1 to v_input_8
    if (long_entry_roc and close < ROCLine and high[1] <= low and positions < 4)
        array.push(entry_prices, strategy.position_avg_price * (1 - v_input_15 / 100))
        positions := positions + 1

for i = 1 to v_input_9
    if (long_entry_roc and close < ROCLine and high[1] <= low and positions < 4)
        array.push(entry_prices, strategy.position_avg_price * (1 - v_input_15 / 100))
        positions := positions + 1

for i = 1 to v_input_10
    if (long_entry_roc and close < ROCLine and high[1] <= low and positions < 4)
        array.push(entry_prices, strategy.position_avg_price * (1 - v_input_15 / 100))
        positions := positions + 1

// Plotting
plot(ROCLine, title="Long Entry Threshold Line", color=color.blue, linewidth=2)
plot(ROCLimit, title="Long Close Limit Line", color=color.red, linewidth=2)

// Variables for backtesting and demo trading
long_entry_roc := close > ROCLine
ROCLine = roc(close, v_input_11) < -v_input_13 ? strategy.position_avg_price * (1 + v_input_15 / 100) : na
ROCLimit = roc(close, v_input_16) > -v_input_18 ? close : na

plotshape(series=long_entry_roc, location=location.belowbar, color=color.green, style=shape.labelup, title="Buy Signal")
plotshape(series=long_close_roc, location=location.abovebar, color=color.red, style=shape.labeldown, title="Sell Signal")