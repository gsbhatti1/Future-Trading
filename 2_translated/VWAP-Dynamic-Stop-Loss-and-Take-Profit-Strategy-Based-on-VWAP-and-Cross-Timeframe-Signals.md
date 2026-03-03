> Name

Dynamic-Stop-Loss-and-Take-Profit-Strategy-Based-on-VWAP-and-Cross-Timeframe-Signals

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/fe74f9988e6c2d6162.png)
[trans]
## Overview

This strategy uses the VWAP (Volume Weighted Average Price) from the daily timeframe as a signal for entering and exiting trades. When the close price crosses above the VWAP, it triggers a long entry with the stop loss set at the previous candle's low if it is below the VWAP, and the target price set 3 points above the entry price. Conversely, when the close price crosses below the VWAP, it triggers a short entry with the stop loss set at the previous candle's high if it is above the VWAP, and the target price set 3 points below the entry price. This strategy does not include an exit condition; trades remain open until the opposing signal occurs.

## Strategy Principle

1. Obtain the VWAP data from the daily timeframe, which serves as the basis for trend determination and trading signals.
2. Determine whether the current close price crosses above/below the VWAP, acting as the trigger for long and short entries, respectively.
3. For long entries, if the previous candle's low is below the VWAP, it is used as the stop loss; otherwise, the VWAP itself is used. The opposite applies for short entries.
4. After entering a position, set a fixed 3-point take profit level.
5. The strategy continues to run until a reverse signal triggers the position to close and open a new one.

By using cross-timeframe VWAP data to determine trends and leveraging dynamic stop losses and fixed-point take profits, the strategy can effectively capture trending markets, control drawdown risks, and timely lock in profits.

## Advantage Analysis

1. Simplicity and effectiveness: The strategy logic is clear, using only the VWAP indicator for trend determination and signal triggering, making it simple to implement and optimize.
2. Dynamic stop loss: By setting the stop loss based on the previous candle's high or low, the strategy adapts better to market fluctuations and reduces risk.
3. Fixed-point take profit: Setting the target price with a fixed number of points helps to lock in profits promptly and avoid profit erosion.
4. Timely stop loss and take profit: The strategy immediately closes the position when a reverse signal is triggered, preventing additional losses on existing profits. It also opens a new position to capture new trending moves.

## Risk Analysis

1. Parameter optimization: The strategy uses a fixed 3 points for take profit, which may require optimization based on different instruments and market characteristics to select the optimal parameters for actual trading.
2. Choppy markets: In choppy market conditions, frequent entries and exits may lead to higher trading costs, affecting profitability.
3. Trend sustainability: The strategy relies on trending markets. If the market is range-bound or lacks trend sustainability, there may be more trading signals generated, introducing more risk.

## Optimization Directions

1. Trend filtering: Incorporate other trend indicators like moving averages, MACD, etc., to confirm trends and improve signal reliability.
2. Dynamic take profit: Adjust the take profit points dynamically based on market volatility, ATR, or other indicators to better adapt to market conditions.
3. Position sizing: Dynamically adjust the position size for each trade based on account size, risk tolerance, and other factors.
4. Trading session selection: Choose the optimal trading sessions based on the characteristics and liquidity of the instrument to improve strategy efficiency.

## Summary

This strategy utilizes cross-timeframe VWAP data for trend determination and signal triggering while employing dynamic stop losses and fixed-point take profits to control risks and lock in profits. It is a simple and effective quantitative trading strategy. Through optimizations in trend filtering, dynamic take profit, position sizing, and trading session selection, the strategy's robustness and profit potential can be further enhanced. However, when applying the strategy in practice, attention should be paid to market characteristics, trading costs, and parameter optimization to achieve better strategy performance.

[/trans]

> Source (PineScript)

```pinescript
//@version=5
strategy("Dynamic-Stop-Loss-and-Take-Profit-Strategy-Based-on-VWAP-and-Cross-Timeframe-Signals", overlay=true, initial_capital=1000, default_qty_value=100, default_qty_type=strategy.percent_of_equity)
```