||

## Overview

The FiboBuLL Wave strategy is adapted from the filter version of the Bollinger Bands study, which can be found under my scripts page. The strategy goes long when the price closes above the upper band and goes short when the price closes below the lower band.

Bollinger Bands is a classic indicator that uses a simple moving average of 20 periods, along with plots of upper and lower bands that are 2 standard deviations away from the middle band. These bands help visualize price volatility and trend based on where the price is relative to the bands.   

The strategy does not take into account any other parameters such as Volume / RSI / Fundamentals etc., so users must use discretion based on confirmations from other indicators or fundamentals. The strategy results are purely based on long and short trades and do not take into account any user-defined targets or stop losses.

It works best when there is a continuation of the bar after price closes above/below upper/lower bands. It is definitely beneficial to use this strategy or the Bollinger Bands filter along with other indicators to get an early glimpse of breach/fail of bands on candle close during BB squeeze or based on volatility.

The strategy can be used on Heikin Ashi candles for spotting trends but HA candles are not recommended for trade entries as they do not reflect true price of the asset.

## Strategy Logic

The core logic behind FiboBuLL Wave strategy is to trade based on the breakout of Bollinger Bands. The Bollinger Bands consist of a middle band, upper band, and lower band. The middle band is a 21-period simple moving average of closing price; The upper band is calculated by adding 1 standard deviation above the middle band, reflecting the upper range of price fluctuation; The lower band is derived by subtracting 1 standard deviation below the middle band, reflecting the lower range of price movement.

A long signal is generated when the closing price breaks above the upper band; A short signal is triggered when the closing price breaks below the lower band. After taking long or short positions, existing trades will be closed out when price breaks the opposite band again.

The strategy uses `barssince` function to track the breakout of price relative to upper and lower bands. A long signal is generated when the number of bars since upper band breakout is less than that of lower band. A short signal is triggered when the number of bars since lower band breakout is less than that of upper band.

By adjusting the middle band period and standard deviation multiplier parameters, the breakout sensitivity of Bollinger Bands can be changed, thereby adjusting the timing of entry.

## Advantages

The FiboBuLL Wave strategy has some advantages:

1. Simple logic based on BB breakout, easy to understand
2. Breakout sensitivity can be controlled by adjusting parameters  
3. BB bands visualize price fluctuation and trend  
4. Can combine with other indicators, improve accuracy 
5. Applicable to multiple timeframes   

## Risks

There are also some risks to note for the FiboBuLL Wave strategy:

1. Prone to false signals relying purely on BB breakout
2. Unable to determine the momentum and duration after breakout   
3. No exit rules for reversal
4. High risk without stop loss  

The optimizations can be made in the following aspects:

1. Add filters using other indicators to avoid false signals  
2. Optimize parameters based on historical data
3. Set stop loss to limit maximum loss
4. Consider adding reversal factors to determine persistence

## Enhancement Opportunities

The main optimization directions for FiboBuLL Wave strategy include:   

1. Add volume indicators e.g., A/D line, to avoid weak breakout  
2. Combine overbought/oversold indicators e.g., RSI, to improve accuracy   
3. Optimize parameters like period and deviation multiplier based on backtest results  
4. Set stop loss and take profit to control risk and lock in profits
5. Consider trend and reversal filters to determine directional persistence  
6. Test optimum parameters across different products and timeframes

With these enhancements, the stability and profitability of the FiboBuLL Wave strategy can be significantly improved.

## Summary

The FiboBuLL Wave strategy utilizes Bollinger Bands to determine price breakouts and returns to the middle band for trading signals. By tracking price volatility with upper and lower bands, this strategy provides a basic framework for trading based on market fluctuations.

However, purely relying on breakouts can lead to false signals and weak breakouts. Therefore, it is essential to integrate trend analysis, volume indicators, and other factors to assess the reliability of breakouts, set stop losses to control risk, and lock in profits. This strategy can serve as a robust foundation for making trading decisions when combined with ongoing optimizations and the use of additional indicators.

FiboBuLL Wave strategy offers us a fundamental approach to determine trading opportunities based on price fluctuations. Through continuous optimization and integration with other indicators, it can become a powerful tool for formulating trading strategies.