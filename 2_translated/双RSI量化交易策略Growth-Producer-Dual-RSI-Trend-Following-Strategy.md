> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|19|Period for the longer RSI|
|v_input_2|120|Period for the shorter RSI|
|v_input_3|35|RVI benchmark period|

---

This is a dual RSI trend following strategy that utilizes two RSI indicators with different timeframes for long and short trading signals, combined with moving averages to determine trend direction. It belongs to the category of dual RSI algorithmic strategies.

## Principle Analysis

The dual RSI strategy mainly uses two RSI indicators with different timeframes for trading signals. The default parameters are set as follows:

- `v_input_1` (default 19) represents the period for the longer RSI.
- `v_input_2` (default 120) represents the period for the shorter RSI.
- `v_input_3` (default 35) is the benchmark period used in the RVI calculation.

When the longer RSI breaks below the oversold line, a long signal is generated. When the shorter RSI breaks above the overbought line, a short signal is generated. This forms the dual RSI crossover system for trading opportunities.

To filter false signals, the strategy also incorporates SMA and EMA moving averages for trend detection. Only when the short period SMA crosses above the long period EMA, the long RSI signal is considered. And only when the short SMA crosses below the long EMA, the short RSI signal is considered. This ensures that RSI signals are aligned with the trend direction and avoids trading against the trend.

In addition, the strategy also sets up stop loss and take profit logic. After opening positions, two take profit orders of different sizes are placed, together with a stop loss level.

## Advantage Analysis

The dual RSI algorithmic strategy has the following advantages:

1. The combination of long and short period RSIs can more accurately determine bullish and bearish signals and filter some false signals.
2. The moving average system helps determine the major trend direction, avoids trading against the trend, and can filter out most noise trades, improving win rate.
3. The flexible stop loss and take profit mechanism allows higher returns through different take profit settings, and manages risk through stop loss.
4. The trading logic is simple and clear, easy to understand and optimize, making it suitable for algorithmic traders to learn.

## Risk Analysis

Despite the advantages, the dual RSI strategy also has the following risks:

1. RSI itself has limited effectiveness in ranging markets and trend reversals. The strategy may underperform in these market conditions.
2. Although moving averages filter small noise, they are less effective in detecting intermediate cycle trend changes, and may miss trend turning points.
3. Improper stop loss and take profit settings may result in stops being too wide or profits too small, deteriorating strategy performance.
4. Large long/short positions can lead to magnified losses. Position sizing needs to be controlled.

To address these risks, parameters can be adjusted, more advanced trend and reversal indicators can be introduced, stop and profit logic optimized, and position sizing controlled to minimize risks.

## Optimization Directions

The dual RSI strategy can be further optimized in the following aspects:

1. Test different parameter combinations to find the optimal long and short RSI periods.
2. Introduce other indicators like MACD for better trend and reversal analysis.
3. Optimize stop loss and take profit strategies, use trailing stops or moving take profits for more flexibility.
4. Add position sizing control module to adjust long/short positions in different trend cycle stages.
5. Incorporate machine learning models to improve entry and exit accuracy.
6. Backtest on different products and timeframes for optimization.

## Conclusion

In summary, the dual RSI strategy is a typical trend following strategy. Its idea of combining dual RSI signals and moving average noise filtering is very classical and practical. Although there are areas for improvement, the overall logic is clear and easy to understand and optimize. This is a great strategy for algorithmic trading beginners to learn and practice. Through continuous optimization and iterations based on the "practice makes perfect" principle, stable trading results can be achieved.

|| 

## Overview

This is a dual RSI trend following strategy that utilizes two RSI indicators with different timeframes for long and short trading signals, combined with moving averages to determine trend direction. It belongs to the category of dual RSI algorithmic strategies.

## Principle Analysis

The dual RSI strategy mainly uses two RSI indicators with different timeframes for trading signals. The default parameters are set as follows:

- `v_input_1` (default 19) represents the period for the longer RSI.
- `v_input_2` (default 120) represents the period for the shorter RSI.
- `v_input_3` (default 35) is the benchmark period used in the RVI calculation.

When the longer RSI breaks below the oversold line, a long signal is generated. When the shorter RSI breaks above the overbought line, a short signal is generated. This forms the dual RSI crossover system for trading opportunities.

To filter false signals, the strategy also incorporates SMA and EMA moving averages for trend detection. Only when the short period SMA crosses above the long period EMA, the long RSI signal is considered. And only when the short SMA crosses below the long EMA, the short RSI signal is considered. This ensures that RSI signals are aligned with the trend direction and avoids trading against the trend.

In addition, the strategy also sets up stop loss and take profit logic. After opening positions, two take profit orders of different sizes are placed, together with a stop loss level.

## Advantage Analysis

The dual RSI algorithmic strategy has the following advantages:

1. The combination of long and short period RSIs can more accurately determine bullish and bearish signals and filter some false signals.
2. The moving average system helps determine the major trend direction, avoids trading against the trend, and can filter out most noise trades, improving win rate.
3. The flexible stop loss and take profit mechanism allows higher returns through different take profit settings, and manages risk through stop loss.
4. The trading logic is simple and clear, easy to understand and optimize, making it suitable for algorithmic traders to learn.

## Risk Analysis

Despite the advantages, the dual RSI strategy also has the following risks:

1. RSI itself has limited effectiveness in ranging markets and trend reversals. The strategy may underperform in these market conditions.
2. Although moving averages filter small noise, they are less effective in detecting intermediate cycle trend changes, and may miss trend turning points.
3. Improper stop loss and take profit settings may result in stops being too wide or profits too small, deteriorating strategy performance.
4. Large long/short positions can lead to magnified losses. Position sizing needs to be controlled.

To address these risks, parameters can be adjusted, more advanced trend and reversal indicators can be introduced, stop and profit logic optimized, and position sizing controlled to minimize risks.

## Optimization Directions

The dual RSI strategy can be further optimized in the following aspects:

1. Test different parameter combinations to find the optimal long and short RSI periods.
2. Introduce other indicators like MACD for better trend and reversal analysis.
3. Optimize stop loss and take profit strategies, use trailing stops or moving take profits for more flexibility.
4. Add position sizing control module to adjust long/short positions in different trend cycle stages.
5. Incorporate machine learning models to improve entry and exit accuracy.
6. Backtest on different products and timeframes for optimization.

## Conclusion

In summary, the dual RSI strategy is a typical trend following strategy. Its idea of combining dual RSI signals and moving average noise filtering is very classical and practical. Although there are areas for improvement, the overall logic is clear and easy to understand and optimize. This is a great strategy for algorithmic trading beginners to learn and practice. Through continuous optimization and iterations based on the "practice makes perfect" principle, stable trading results can be achieved.