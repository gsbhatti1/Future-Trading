## Overview

This strategy combines two powerful built-in indicators in TradingView - the Directional Movement Index (DMI) and the Detrended Price Oscillator (DPO) to form a reliable basis for trading decisions. The core logic of the strategy is to determine if the DPO value is greater than 0 when a DMI golden cross occurs, and generate a long signal if so; or to determine if the DPO value is less than 0 when a DMI dead cross occurs, and generate a short signal if so. This can effectively filter out a lot of false signals generated during range-bound oscillations in the market, thereby only generating trading signals when a trend is formed, avoiding repeated stop losses during oscillations.

## Principle

This strategy mainly uses the DMI indicator to determine the trend direction and strength. The DMI indicator consists of three curves: +DI, -DI and ADX. +DI represents the strength of uptrend, -DI represents the strength of downtrend, and their crossover can determine the current trend direction; ADX represents the strength of the trend, the higher the value, the more obvious the trend. However, ADX is not good at identifying low volatility ranges, so this strategy removes the ADX determination and only uses the +DI and -DI crossovers to determine the trend direction.

In order to filter out the false signals generated in the range-bound oscillations, the DPO indicator is introduced for auxiliary judgment. The DPO indicator represents the degree of deviation of the price from its middle rail. When the price is above the middle rail, the DPO is positive, and when below, it is negative. This strategy uses the positivity and negativity of the DPO indicator to judge whether it is currently in a trend. If the DMI indicator crosses but the DPO indicator is close to the 0 level, it is determined to be an oscillation and no trading signal is generated.

Specifically, the judgment logic is:

1. When +DI crosses above -DI, it is a golden cross, indicating a bull market. At this time, if the DPO indicator is greater than 0, it confirms that it is currently in an upward trend, and a long signal is generated.
2. When -DI crosses below +DI, it is a dead cross, indicating a bear market. At this time, if the DPO indicator is less than 0, it confirms that it is currently in a downward trend, and a short signal is generated.
3. If +DI/-DI crosses but DPO indicator is close to 0, it is determined as oscillation and no signal is generated.

## Advantage Analysis

The biggest advantage of this combined strategy is its high accuracy in identifying trends, generating trading signals only when real trend reversals occur, thus avoiding repeated losses during oscillating intervals. Its main advantages are:

1. Using the DMI indicator to determine the trend direction and strength, it is a mature and reliable technical indicator.
2. Filtering out false signals from range-bound oscillations with the help of the DPO indicator, generating signals only when a trend is formed, avoiding losses.
3. Combining multiple indicators can serve as mutual verification and improve the reliability of signals.
4. The strategy logic is simple and easy to understand and implement, suitable for automated or manual trading.
5. Since it only trades in trends, it can obtain a relatively high risk reward ratio.

## Risk Analysis

Although this is a highly reliable strategy, the following risks should be noted:

1. Sudden events may cause huge one-sided moves in the market, possibly missing such trend opportunities. This risk can be reduced by lowering the DPO parameters.
2. The DMI indicator itself may also generate wrong signals, and this risk cannot be completely avoided. Losses can be controlled by setting stops.
3. Improper parameter settings of the DPO indicator can also lead to misjudgments. The optimal parameters should be determined through repeated backtesting.
4. Trading costs will have a certain impact on profits, so the trading frequency should be controlled. Invalid trades can be reduced by optimizing parameters.

## Optimization

There is still room for further optimization of this strategy:

1. Different parameter combinations can
2. Be tested to find the best parameters to reduce signal delay and increase profitability.
3. Other indicators such as KDJ and MACD can be combined for verification, improving the accuracy of signals.
4. Parameters can be adjusted based on different varieties and timeframes to make the strategy more adaptable.
5. Dynamic stops can be set to control single loss. Different stop levels can also be set according to trend stages.
6. Machine learning methods can optimize entry and exit times to achieve higher returns.

## Summary

This strategy integrates the strengths of DMI and DPO indicators, making very accurate judgments on trend reversals, allowing for reliable identification of trend formation. At the same time, using the DPO indicator effectively filters out noises from range-bound oscillations, avoiding unnecessary trades. This makes it a highly efficient strategy suitable for both automated and manual trading. Of course, there are still many details that can be further optimized to achieve better performance. However, this combination of indicators provides important reference value for designing quantitative trading strategies.