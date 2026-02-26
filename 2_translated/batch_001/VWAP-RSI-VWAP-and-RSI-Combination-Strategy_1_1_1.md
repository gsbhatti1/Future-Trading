||

## Overview  

The strategy is named "VWAP and RSI Combination Strategy". It utilizes Value Weighted Average Price (VWAP) and Relative Strength Index (RSI) indicators to implement a combination strategy of trend following entry and overbought oversold exit.

## Strategy Principle  

The main logic of this strategy is based on the following points:

1. Use the 50-day exponential moving average crossing above the 200-day line as a signal that the market trend is up.
2. When the closing price is higher than the VWAP price of the day, and the closing price is higher than the opening price, it is considered that the market is going stronger and can enter the market.
3. If the RSI indicator on at least one of the previous 10 K-lines is lower than 10, it is regarded as an oversold formation and a strong entry signal.
4. When the RSI indicator crosses down the overbought area of 90 again, exit the market.
5. Set a 5% stop loss to avoid excessive losses.

The above is the basic trading logic of this strategy. EMA judges the big trend, VWAP judges the daily trend, and RSI judges the overbought and oversold area to achieve effective combination of multiple indicators, which ensures the correct direction of the main trading while increasing entry and exit signals.

## Advantage Analysis  

The biggest advantage of this strategy is the combination use of indicators. The single VWAP cannot perfectly cope with all market conditions. At this time, with the help of RSI, some short-term oversold breakout opportunities can be identified. Additionally, the application of EMA also ensures that only long-cycle upward trends are selected, avoiding being trapped by short-term reversals.

This way of using combined indicators also increases the stability of the strategy. In the case of one or two false breakouts of the RSI, there are still VWAP and EMA for backup, and it is unlikely to make wrong trades. Similarly, when VWAP has false breakouts, there is also confirmation from RSI indicators. Therefore, this combination usage greatly improves the success rate of strategy implementation.

## Risk Analysis  

The main risk of this strategy lies in the use of the VWAP indicator. VWAP represents the average transaction price of the day, but not every day's price fluctuation fluctuates around VWAP. Therefore, VWAP breakout signals do not necessarily ensure that prices can continue to break through afterwards. Pseudo breakouts may cause losses in transactions.

In addition, RSI indicators are prone to have divergences. When the market is in a consolidation phase, the RSI may repeatedly touch the overbought and oversold zones multiple times, resulting in frequent output of trading signals. In this case, blindly following RSI signals for trading also faces certain risks.

To address this issue, we use the EMA exponential moving average as a large cycle judgment in the strategy, only considering trading when the large cycle is upward, which can alleviate the impact of the above two issues on the strategy to some extent. In addition, setting a stop loss can also keep a single loss within a certain range.

## Optimization Direction  

There is still room for further optimization of this strategy, mainly in the following aspects:

1. Introduce more indicators for combination. Such as Kalman lines, Bollinger bands, etc., to make trading signals clearer and more reliable.
2. Optimize transaction costs. The existing strategy does not consider the impact of fees and commissions. It can be combined with real trading accounts to optimize the size of the number of open positions.
3. Adjust the stop loss model. The existing stop loss method is relatively simple and cannot perfectly match market changes. Moving stop loss, tracking stop loss, and other methods can be tested.
4. Test the application effects of different varieties. Currently only tested on the S&P 500 and Nasdaq indices. The sample range can be expanded to find the varieties that best match this strategy.

## Summary  

This strategy integrates the advantages of EMA, VWAP, and RSI indicators to achieve effective combination of trend tracking and overbought oversold signals, which can find reasonable entry opportunities both in big cycle ups and short-term adjustments. At the same time, the strategy has considerable room for optimization, with potential improvements through the introduction of more indicators, adjustment of stop loss methods, and testing on different varieties.