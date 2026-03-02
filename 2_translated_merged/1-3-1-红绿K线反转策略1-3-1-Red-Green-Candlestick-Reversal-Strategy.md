> Name

1-3-1 Red-Green Candlestick Reversal Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/491225d47e40fa480f.png)

[trans]

## Overview

The 1-3-1 Red-Green Candlestick Reversal Strategy is a trading strategy that generates buy and sell signals based on candlestick patterns. It identifies buying opportunities when one red candle is followed by three consecutive green candles.

## Principles

The core logic of this strategy includes:

1. Checking if the current candle is a red candle, i.e., the close price is lower than the open price.
2. Confirming that the previous 3 candles are green candles, i.e., the close price is higher than the open price.
3. Verifying that the last green candle's closing price is higher than the previous two green candles' closing prices.
4. If all conditions are met, enter a long position at the close of the red candle.
5. Set stop loss to the lowest price of the red candle.
6. Set take profit based on the distance between the entry price and the stop loss.

By using this strategy, we can buy when the red candle is reversed, because the subsequent trend may be upward. Stop loss and take profit are set to control risk and lock in profits.

## Advantage Analysis

The 1-3-1 Red-Green Reversal Strategy has the following advantages:

1. Simple and clear logic, making it easy to understand and implement.
2. Utilizes candlestick pattern features without relying on indicators, avoiding issues related to over-optimization.
3. Has clear entry and exit rules for objective execution.
4. Sets stop loss and take profit to control the risk/reward ratio of each trade.
5. Good backtest results with strong potential for live trading.

## Risk Analysis

Some risks associated with this strategy include:

1. Candlestick patterns cannot perfectly predict future trends, introducing some uncertainty.
2. Only one entry is made; thus, the win rate may be lower due to stock-specific factors.
3. No consideration of market trend; holding during a sustained downtrend could pose significant risk.
4. Does not account for transaction costs and slippage, which might affect actual performance.

Solutions:

1. Consider integrating with Moving Averages (MAs) or other indicators to filter signals and improve entry success rate.
2. Adjust position sizing by scaling in across multiple entries.
3. Dynamically adjust the stop loss based on market conditions or pause trading temporarily.
4. Test different stop loss/take profit ratios.
5. Evaluate actual performance including transaction costs.

## Optimization Directions

Some ways this strategy can be optimized include:

1. Market Index Filtering: Filter signals based on short and medium-term market trends, entering positions during an uptrend and ceasing trades in a downtrend.
2. Volume Confirmation: Enter only when green candle volumes increase.
3. Optimize Stop Loss/Take Profit Ratios: Test different ratios to find the optimal parameters.
4. Position Sizing Optimization: Scale in across multiple entries to reduce single trade risk.
5. Add More Filters: Incorporate additional filters such as Moving Averages, volatility indicators, etc., to ensure higher probability of entry.
6. Big Data Training: Collect a large amount of historical data and use machine learning techniques to train optimal parameter thresholds.

## Conclusion

The 1-3-1 Red-Green Reversal Strategy is an overall simple and practical short-term trading strategy with clear entry and exit rules and good backtest results. With some optimization measures, it can become a reliable quantitative trading strategy. Proper risk management is also important to manage capital effectively.

||

## Overview 

The 1-3-1 Red-Green Candlestick Reversal Strategy generates buy and sell signals based on candlestick patterns. It looks for buying opportunities when one red candle is followed by three consecutive green candles.

## Principles

The core logic of this strategy includes:

1. Check if the current candle is a red candle, i.e., the close price is lower than the open price.
2. Confirm that the previous 3 candles are green candles, i.e., the close price is higher than the open price.
3. Verify that the last green candle's closing price is higher than the previous two green candles' closing prices.
4. If all conditions are met, enter a long position at the close of the red candle.
5. Set stop loss to the lowest price of the red candle.
6. Set take profit based on the distance between the entry price and the stop loss.

By using this strategy, we can buy when the red candle is reversed, because the subsequent trend may be upward. Stop loss and take profit are set to control risk and lock in profits.

## Advantage Analysis

The 1-3-1 Red-Green Reversal Strategy has the following advantages:

1. Simple and clear logic, making it easy to understand and implement.
2. Utilizes candlestick pattern features without relying on indicators, avoiding issues related to over-optimization.
3. Has clear entry and exit rules for objective execution.
4. Sets stop loss and take profit to control the risk/reward ratio of each trade.
5. Good backtest results with strong potential for live trading.

## Risk Analysis

Some risks associated with this strategy include:

1. Candlestick patterns cannot perfectly predict future trends, introducing some uncertainty.
2. Only one entry is made; thus, the win rate may be lower due to stock-specific factors.
3. No consideration of market trend; holding during a sustained downtrend could pose significant risk.
4. Does not account for transaction costs and slippage, which might affect actual performance.

Solutions:

1. Consider integrating with Moving Averages (MAs) or other indicators to filter signals and improve entry success rate.
2. Adjust position sizing by scaling in across multiple entries.
3. Dynamically adjust the stop loss based on market conditions or pause trading temporarily.
4. Test different stop loss/take profit ratios.
5. Evaluate actual performance including transaction costs.

## Optimization Directions

Some ways this strategy can be optimized include:

1. Market Index Filtering: Filter signals based on short and medium-term market trends, entering positions during an uptrend and ceasing trades in a downtrend.
2. Volume Confirmation: Enter only when green candle volumes increase.
3. Optimize Stop Loss/Take Profit Ratios: Test different ratios to find the optimal parameters.
4. Position Sizing Optimization: Scale in across multiple entries to reduce single trade risk.
5. Add More Filters: Incorporate additional filters such as Moving Averages, volatility indicators, etc., to ensure higher probability of entry.
6. Big Data Training: Collect a large amount of historical data and use machine learning techniques to train optimal parameter thresholds.

## Conclusion

The 1-3-1 Red-Green Reversal Strategy is an overall simple and practical short-term trading strategy with clear entry and exit rules and good backtest results. With some optimization measures, it can become a reliable quantitative trading strategy. Proper risk management is also important to manage capital effectively.

||

```pinescript
/*backtest
start: 2023-09-26 00:00:00
end: 2023-10-26 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
// by Genma01
strategy("Stratégie tradosaure 1 Bougie Rouge suivi de 3 Bougies Vertes", overlay=true, default_qty_type = strategy.percent_of_equity, default_qty_value = 100)

// Define parameters
var float stopLossPrice = na
var float takeProfitPrice = na
var float stopLossPriceD = na
var float takeProfitPriceD = na

// Check conditions
redCandle = close[3] < open[3] and low[3] < low[2] and low[3] < low[1] and low[3] < low[0]
greenCandles = close > open and close[1] > open[1] and close[2] > open[2]
higherClose = close > close[1] and close[1] > close[2]

// Calculate stop-loss
if (redCandle and greenCandles and higherClose) and strategy.position_size == 0
    stopLossPrice := low[3]

// Calculate take-profit
if not na(stopLossPrice) and strategy.position_size == 0
    takeProfitPrice := close + (close - stopLossPrice)

// Enter long position
if redCandle and greenCandles and higherClose and strategy.position_size == 0
    strategy.entry("Long", strategy.long)

// Exit from the position
if not na(stopLossPrice) and strategy.position_size > 0
    strategy.exit("Take Profit/Stop Loss", stop=stopLossPrice, limit=takeProfitPrice)

if strategy.position_size == 0
    stopLossPriceD
```