## Overview

This strategy combines the price reversal strategy and the Relative Strength Index (RSI) indicator to achieve an organic combination of trend judgment and overbought-oversold detection. The price reversal part judges whether a price reversal signal has occurred, and the RSI part is used to determine whether the market is overbought or oversold. The combination of the two signals can effectively filter out false signals and improve signal quality.

## Strategy Principle

The price reversal part uses the 123 pattern to judge price reversals. Specifically, when the closing price is lower than the previous closing price for 2 consecutive days, and the 9-day stochastic indicator lower channel line is higher than 50, a buy signal is generated; When the closing price is higher than the previous closing price for 2 consecutive days, and the 9-day stochastic oscillator upper channel line is lower than 50, a sell signal is generated.

The RSI part judges whether the market is overbought or oversold according to whether the Relative Strength Index is higher than 70 or lower than 30. An RSI above 70 is an overbought signal, and an RSI below 30 is an oversold signal.

Finally, a logical "AND" operation is performed on the price reversal signal and the RSI signal. That is, only when both are buy or sell signals will an actual trading signal be generated to enter the market. This effectively filters out false signals from single indicators and improves signal quality.

## Advantage Analysis

1. The combination of multiple indicators can effectively filter out false signals.

   This strategy uses price pattern indicators and overbought-oversold indicators at the same time. The two signals need to be in the same direction before entering the market. This can maximize filtering out the false signals that a single indicator may produce and ensure the reliability of each entry signal.

2. Trading method with reversal as the main and trend as the accessory.

   The price reversal part mainly uses the 123 pattern to judge the reversal situation. This is a typical reversal trading method. At the same time, the RSI indicator can also judge trends and act as an auxiliary confirmation. The combination of reversal-based and trend-assisted can capture reversal opportunities while avoiding trend conflicts.

3. Simple parameter settings for easy live trading operations.

   This strategy uses only two common indicators with a moderate number of parameters. This makes the overall structure of the strategy simple and clear, with low difficulty for live operations, which is easy to master. This is very important for live traders.

## Risk Analysis

1. Risk of reversal failure

   There is a probability of failure inherent in price reversal trading that cannot be completely avoided. When the price forms a 123 signal but then reverses back again. This will cause the trade to fail.

2. Risk of excessively high trading frequency

   The standard of the strategy itself is relatively loose, which easily generates more trading signals. If not controlled, it will lead to excessively high operating frequencies, increasing trading costs and psychological pressure.

3. Improper RSI Parameter Settings

   The overbought/oversold zones of the RSI indicator default to 30-70. These are empirical parameters. If the actual market does not match, correct signals may be missed or incorrect signals may be issued.

### Risk Mitigation

1. Adjust position size appropriately to control single loss.
2. Increase filtering conditions to reduce trading frequency. For example, add moving average judgment.
3. Test different markets and dynamically adjust RSI parameter ranges to set reasonable values.

## Strategy Optimization

1. Add moving average indicator judgment

   On the existing basis, add a moving average judgment rule to filter out small-range noise to some extent.

2. Optimize RSI parameter settings 

   Through backtesting historical data, test and determine the optimal parameter combination of RSI overbought and oversold values.

3. Evaluate the profit-loss ratio as the position exit

   In addition to the existing stop loss method, a profit target versus stop loss relationship exit mechanism can be added to lock in profits.

## Summary

This strategy uses double confirmation of price reversal judgment and RSI indicator judgment to implement a trading approach with reversal as the main focus and trend as an accessory. At the same time, simple parameter settings make it easy for live traders to grasp. By optimizing, more filtering conditions can be added while maintaining signal capture quality. The overall operation of this strategy is effective and has practical value in real-world application.

|