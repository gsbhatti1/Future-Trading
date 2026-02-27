```markdown
## Overview

The RSI Trend Reversal strategy utilizes the reversal signals of the RSI indicator to identify potential trend reversal points and enter long or short trades. This strategy combines price reversal and RSI reversal signals to effectively filter out false reversal signals.

## Strategy Logic

This strategy is based on the combination of RSI reversal signals and price reversal signals, mainly including four situations:

1. **Regular Bullish Reversal:** When RSI forms a higher low (meaning RSI trend reverses from up to down) and price forms a lower low (meaning price trend reverses from down to up), a regular bullish reversal signal is generated.

2. **Hidden Bullish Reversal:** When RSI forms a lower low (meaning RSI trend continues from up to down) but price forms a higher low (meaning price trend reverses from down to up), a hidden bullish reversal signal is generated.

3. **Regular Bearish Reversal:** When RSI forms a lower high (meaning RSI trend reverses from down to up) and price forms a higher high (meaning price trend reverses from up to down), a regular bearish reversal signal is generated.

4. **Hidden Bearish Reversal:** When RSI forms a higher high (meaning RSI trend continues from down to up) but price forms a lower high (meaning price trend reverses from up to down), a hidden bearish reversal signal is generated.

This strategy combines both RSI and price reversal signals to generate trading signals, avoiding false signals from relying merely on RSI or price reversals alone, making the strategy more robust.

## Advantage Analysis

The RSI Trend Reversal strategy has the following advantages:

1. **Combining RSI and Price Reversals:** It effectively filters out many false reversal signals and improves signal quality by combining both RSI and price trends.
2. **Identifying Hidden Patterns:** It identifies hidden bullish and bearish patterns, which often precede powerful price trends, allowing early entry.
3. **Customizable Parameters:** Customizable RSI parameters and lookback periods can be adjusted for different markets, offering flexibility.
4. **Visual Signal Identification:** Visualizing indicator patterns and signals provides a clear view of the market state.
5. **Simple Strategy Logic:** The logic is simple and clear, making it easy to understand and implement.

## Risk Analysis

The RSI Trend Reversal strategy also has the following risks:

1. **False Signals:** Despite combining RSI and price reversals, occasional misjudgments may still occur as indicators are statistical measures of prices.
2. **Hidden Pattern Recognition:** Hidden bullish and bearish patterns can be hard to identify without experience, leading to missed opportunities.
3. **Parameter Optimization:** Improper lookback period settings may result in missing reversal points or delayed judgments, requiring adjustments for different markets.
4. **Stop Loss Implementation:** Stop loss strategies should be used to avoid increased losses after bearish reversals.

Risks can be managed by optimizing parameters, using strict stop losses, and prudently taking hidden reversal signals.

## Optimization Directions

The RSI Trend Reversal strategy can be optimized in the following aspects:

1. **Optimize RSI Parameters:** Test different RSI periods to find optimal settings for various markets.
2. **Fine-Tune Lookback Periods:** Balance catching reversals early and avoiding false signals by optimizing lookback periods.
3. **Volume Analysis:** Incorporate volume analysis, such as identifying large volume unwinding causing price reversals.
4. **Combine with Other Indicators:** Integrate other indicators like MACD or Bollinger Bands to improve judgment accuracy.
5. **Implement Stop Loss Strategies:** Set stop losses after price breaks new highs/lows to limit potential losses.
6. **Refine Strategy Logic:** Adjust strategy logic based on backtest results to enhance profitability.

## Summary

The RSI Trend Reversal strategy identifies potential trend turning points by combining RSI reversals and price reversals, effectively leveraging RSI's trend judgment capability while filtering false signals with price information. The strategy has simple and clear logic that is easy to implement. Parameters and stop loss strategies can be optimized to manage risks and further improve performance. Overall, the RSI Trend Reversal strategy is a reliable and practical short-term trading strategy.

||

## Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| v_input_1 | 5 | RSI Period |
| v_input_2_close | 0 | RSI
```