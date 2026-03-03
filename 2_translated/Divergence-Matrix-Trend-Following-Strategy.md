## Overview

The Divergence Matrix Trend Following Strategy is a quantitative trading strategy that combines trend, divergence, and moving average analysis. This strategy uses dual RSI indicators to judge market trend direction and matrix moving averages to generate entry signals. The matrix moving averages adjust position sizing based on the degree of price divergence. Overall, the advantage of this strategy is to confirm trading signals with multiple indicators, which can effectively avoid false breakouts. Meanwhile, the matrix mechanism can lock in higher returns.

## Strategy Logic

The Divergence Matrix Trend Following Strategy consists of the following main parts:

1. **Dual RSI for trend judging**

   Use fast RSI and slow RSI to determine market trend direction. When the fast RSI shows overbought or oversold levels, check the slow RSI for trend direction.

2. **Matrix moving average for trading signals**

   Set up a group of matrix moving averages based on the entry price. When the price touches a moving average line, adjust the position accordingly. This allows more profits to be captured in trends.

3. **Bi-directional trading**

   Default is bi-directional trading. Can choose to only go long.

The specific trading logic is:

1. Use fast RSI to spot temporary overbought/oversold levels in the market.

2. Use slow RSI to determine the mid-to-long term trend direction of the market.

3. When fast RSI shows extremes and slow RSI signals trend reversal, take positions based on the long/short trend by slow RSI.

4. After entering positions, set up a group of matrix moving averages. These matrix lines are based around the entry price, with interval size defined in the "Matrix Interval %" parameter.

5. When price touches a matrix line, adjust position size accordingly. For example, increase longs on upward breakouts, reduce shorts on downward breakdowns.

6. When price sees large adjustments, positions will be reset to initial levels.

The above describes the main trading logic of this strategy. The matrix mechanism allows more trend profits to be locked in.

## Advantages

The Divergence Matrix Trend Following Strategy has the following advantages:

1. **Reliable dual RSI signals**. Fast RSI avoids false breakouts, and slow RSI ensures the major trend is correct.
   
2. **Matrix moving averages profit from trends**. Adjusting position size based on price divergence allows sustained profits to be captured.
   
3. **Supports bi-directional trading**. Default is dual directional trading, but can also go long only. This adapts to more market environments.

4. **Position reset mechanism controls risks**. Resetting positions when price sees large adjustments allows timely stop losses.

5. **Flexible parameter settings**. Users can select optimal parameter combinations based on historical data, trading instruments, etc.

6. **Clean code structure**. Clear separation of responsibilities makes the code easy to understand, optimize and extend.

In summary, the biggest edge of this strategy is to improve signal quality through multiple mechanisms while pursuing higher returns under controlled risks. This is a strategy balancing risk and reward.

## Risks

The Divergence Matrix Trend Following Strategy also has some risks, mainly in the following areas:

1. **Failure risk of dual RSI signals**. When the market is range-bound, RSI often gives false signals. Manual intervention is needed to adjust parameters or suspend trading.

2. **Improper matrix moving average risk**. If matrix parameters are not set properly, position adjustments can be too aggressive, thus magnifying losses. Conservative parameter testing is a must.

3. **Risk of over-leveraged positions**. Excessive position size adjustments will also expand losses. The maximum position size parameter needs to be set prudently.

4. **Trend reversal risk**. If failing to close positions promptly when trend reverses, large losses may be incurred. This calls for monitoring long-term trends carefully.

5. **Limited code optimization potential**. The strategy is already quite mature, and further optimization may have limited impact. If market conditions change significantly, the overall trading logic needs reassessment.

Evaluating and optimizing the strategy are key to reducing these risks. For example, adjusting parameter combinations, monitoring long-term indicators, etc., can help mitigate some of these risks.

## Optimization Directions

The Divergence Matrix Trend Following Strategy still has room for further optimization:

1. **Optimize dual RSI parameters**. Test more parameter combinations to choose the most accurate RSI cycle values.

2. **Custom matrix moving average settings**. Allow users to customize matrix moving average parameters based on different trading instruments, making them better suited to each instrument's characteristics.

3. **Add stop-loss mechanisms**. For example, set exit-moving averages; if price breaks below this line, execute a stop loss.

4. **Increase position sizing rules**. More scientifically reasonable adjustments in position scale and speed, preventing excessive leverage.

5. **Integrate other indicators**. Introduce MACD or KD for additional confirmation to enhance signal accuracy.

6. **Optimize code structure**. Continue improving the code's extendability, maintainability, and execution efficiency.

## Summary

The Divergence Matrix Trend Following Strategy is a multi-mechanism integrated quantitative trading strategy that primarily uses dual RSI indicators to determine trend direction and matrix moving averages for profit tracking during trends. Compared to single-indicator strategies, this approach offers more stable and efficient trading signals. Through parameter tuning and optimization, the strategy can adapt to various market environments, making it highly applicable. Overall, the strategy strikes a good balance between risk and reward, warranting active application and continuous refinement by investors.