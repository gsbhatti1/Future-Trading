> Name

HYE Mean Reversion SMA Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1afbc5f1b00bdc7aacb.png)

## Overview

The HYE Mean Reversion SMA Strategy is a mean reversion trading strategy using simple moving averages and the relative strength index (RSI). It generates buy and sell signals when the price deviates from the moving average by a certain percentage, combined with RSI indicator filtering. It is a short-term trading strategy.

## Strategy Logic

The strategy is mainly based on the following rules:

1. When the 2-period simple moving average falls 3% below the 5-period simple moving average, it is considered the price deviates from the mean and a buy signal is generated.
  
2. When the 2-period SMA crosses over the 5-period SMA, it is considered the price reverts to the mean and a sell signal is generated.

3. Combined with the exponential moving average of 5-period RSI, buy signals are only generated when RSI is below 30 and sell signals when RSI is above 70, to avoid unnecessary trading.

The main idea is to capture mean reversion opportunities by using short-term price fluctuations. Buy when the price drops by a certain percentage, sell when the price reverts near the moving average, to make a profit. Meanwhile, the RSI indicator can identify overbought and oversold conditions to filter out some noisy trading signals.

## Advantage Analysis

The strategy has the following advantages:

1. Simple to implement with low monitoring costs.
   
2. Captures short-term mean reversion opportunities using price deviation from moving averages. Good backtest performances historically.
  
3. RSI indicator can effectively filter noise trading and avoid chasing peaks and killing valleys.
  
4. Flexible parameter adjustment adaptable to different market environments.

5. Supports long only, short only or both directions trading to suit different preferences.

## Risk Analysis

There are also some risks:

1. Mean reversion relies on the price reverting to the moving average. There are high stop loss risks if drastic price changes occur.
  
2. Improper parameter settings may lead to over-trading or missing opportunities.
  
3. Performance is highly correlated with the market. Underperforms in range-bound and volatile markets.

Countermeasures:

1. Set proper stop loss to control single trade loss.
  
2. Gradually optimize parameters and evaluate risk adjusted returns.

3. Combine with stock index to enhance adaptivity.

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Test different moving average combinations to find optimal parameters.
  
2. Try incorporating other indicators to identify trends and improve win rate.
  
3. Add stop loss mechanisms to reduce maximum drawdown.
  
4. Optimize entry and exit rules to improve profit factors.
  
5. Adopt machine learning techniques to build adaptive parameters.

## Conclusion

The HYE Mean Reversion SMA Strategy is a simple and practical short-term mean reversion strategy. It uses the price deviation from moving averages to generate trading signals, filtering out noise with RSI indicator. It demonstrated good backtest performances. The strategy is easy to implement with adjustable parameters adaptable to different market environments. But the uncertainty of reversion and stop loss risks should be noted, necessitating proper optimization for different market conditions. Overall, it provides a good reference mean reversion strategy template for quantitative trading.

||

## Source (PineScript)

```pinescript
// @version=4
strategy("HYE Mean Reversion SMA [Strategy]", overlay = true)
  
// Strategy inputs
source = input(title="Source", defval=close)
tradeDirection = input(title="Trade Direction", type=input.string, options=["Long Only", "Short Only", "Both"], defval="Long Only")
smallMAPeriod = input(title="Small Moving Average", defval=2)
bigMAPeriod = input(title="Big Moving Average", defval=5)
percentBelowToBuy = input(title="% below to buy", defval=3)
percentAboveToSell = input(title="% above to sell", defval=3)
rsiPeriod = input(title="Rsi Period", defval=2)
maxRsiLevelForBuy = input(title="Maximum Rsi Level for Buy", defval=30)
minRsiLevelForSell = input(title="Minimum Rsi Level for Sell", defval=70)
startDate = input(title="Start Date", type=input.datetime, defval=datetime(2020, 1, 1))
endDate = input(title="End Date", type=input.datetime, defval=datetime(2021, 12, 31))

// Calculate moving averages
shortSMA = sma(source, smallMAPeriod)
longSMA = sma(source, bigMAPeriod)

// RSI calculation
rsiValue = rsi(source, rsiPeriod)

// Buy and sell signals based on the defined rules
if (tradeDirection == "Long Only" or tradeDirection == "Both")
    buySignal = shortSMA < longSMA * (1 - percentBelowToBuy / 100) and rsiValue < minRsiLevelForSell
    strategy.entry("Buy", strategy.long, when=buySignal)

if (tradeDirection == "Short Only" or tradeDirection == "Both")
    sellSignal = shortSMA > longSMA * (1 + percentAboveToSell / 100) and rsiValue > maxRsiLevelForBuy
    strategy.close("Buy", when=sellSignal)
```

This script defines the HYE Mean Reversion SMA Strategy, incorporating simple moving averages, RSI, and customizable parameters for both buy and sell signals.