> Name

MACD动量缠绕DMI突破短线套利策略Inverse-MACD-Momentum-Entangled-with-DMI-Breakout-Short-Term-Scalping-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/10f9c64555169d84b4b.png)
[trans]


## Overview

This strategy focuses on short selling during bear market conditions by utilizing two strength-based indicators to provide confluence that the start of a short-term downtrend has occurred - catching the shorting opportunity as soon as possible.

The strategy works well on coins you plan to hodl long-term and performs especially well whilst using an automated trading bot that can execute trades for you. It allows you to hedge your investment by allocating a percentage of your coins to trade with, without risking your entire holding. This mitigates unrealized losses from hodling as it provides additional cash from the profits made. You can then choose to hodl this cash, or use it to reinvest when the market reaches attractive buying levels.

Alternatively, you can use this when trading contracts on futures markets where there is no need to already own the underlying asset prior to shorting it.

## Strategy Logic

The trading system uses the Momentum Average Convergence Divergence (MACD) indicator and the Directional Movement Index (DMI) indicator to confirm when the best time is for selling. Combining these two indicators prevents trading during uptrends and reduces the likelihood of getting stuck in a market with low volatility.

The MACD is a trend following momentum indicator and provides identification of short-term trend direction. In this variation it utilizes the 12-period as the fast and 26-period as the slow length EMAs, with signal smoothing set at 9.

The DMI indicates what way price is trending and compares prior lows and highs with two lines drawn between each - the positive directional movement line (+DI) and the negative directional movement line (-DI). The trend can be interpreted by comparing the two lines and which line is greater. When the negative DMI is greater than the positive DMI, there are more chances that the asset is trading in a sustained downtrend, and vice versa.

The system will enter trades when two conditions are met:

1) The MACD histogram turns bearish.

2) When the negative DMI is greater than the positive DMI.

The strategy comes with a fixed take profit combined with a volatility stop, which acts as a trailing stop to adapt to the trend's strength. Depending on your long-term confidence in the asset, you can edit the fixed take profit to be more conservative or aggressive.

The position is closed when:

Take-Profit Exit: +8% price decrease from entry price.

OR

Stop-Loss Exit: Price crosses above the volatility stop.

In general, this approach suits medium to long term strategies. The backtesting for this strategy begins on 1 April 2022 to 18 July 2022 in order to demonstrate its results in a bear market. Back testing it further from the beginning of 2022 onwards also produces good returns.

Pairs that produce very strong results include SOLUSDT on the 45m timeframe, MATICUSDT on the 2h timeframe, and AVAUSDT on the 1h timeframe. Generally, the back testing suggests that it works best on the 45m/1h timeframe across most pairs.

A trading fee of 0.1% is also taken into account and is aligned to the base fee applied on Binance.

## Advantage Analysis

The advantages of this strategy include:

- Utilizes the strengths of both MACD and DMI indicators to improve the accuracy of entry signals and avoid false breakouts.

- Employs a combination of fixed take profit and volatility trailing stop exit mechanisms to ensure higher take profits while controlling risk.

- Suitable for bear market downtrends to capture substantial short-term scalping profits.

- Can be used to hedge long positions to gain additional income. Or directly short futures contracts for scalping.

- Strong backtest results, especially on 1h and 45m timeframes suitable for high frequency trading.

## Risk Analysis

The risks of this strategy include:

- DMI and MACD as lagging indicators have a higher probability of generating erroneous signals around trend reversal points. Attention should be paid to the stop loss.

- The fixed take profit setting may be too conservative or aggressive depending on the volatility of different assets. It is recommended to adjust it according to the market conditions.

- The volatility trailing stop can be breached during periods of high volatility, requiring additional stop losses to be added.

- Choosing an inappropriate backtest period may lead to overly optimistic results. Longer term and testing across different market stages are needed.

- Real-world performance will be affected by trading fees, slippage from market orders, etc., which may differ from backtesting.

## Optimization Directions

This strategy can be further optimized in the following ways:

- Use machine learning methods to automatically optimize MACD and DMI parameter combinations for different timeframes and assets.

- Increase dynamic take profit based on volatility to adjust the stop profit according to market conditions.

- Add other indicators for judgment, forming a multi-factor model to improve filtering effects. For example, BVN and OBV indicators.

- Use machine learning models to judge trends to assist MACD and DMI in issuing signals.

- Replace market orders with limit orders to reduce slippage impact.

- Test different assets separately to find the optimal time frame parameter combinations.

## Summary

In summary, this short-term bear market arbitrage strategy leverages the strong combination of MACD and DMI indicators to determine selling opportunities, achieving substantial quantitative gains. It can be used to hedge long positions or directly short futures contracts for scalping. Optimizing stop loss strategies and adjusting parameters can further improve its success rate. This strategy is worth active application and optimization by bear market traders.