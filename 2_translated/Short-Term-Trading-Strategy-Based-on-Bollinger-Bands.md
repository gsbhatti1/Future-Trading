```markdown
<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Short-Term-Trading-Strategy-Based-on-Bollinger-Bands

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/c37c8c6a6f7f29ce1f.png)
[trans]

## Overview

This strategy uses Bollinger Bands indicator to determine trading signals and set stop profit/loss levels. It goes long when price touches the middle band from below and goes short when price touches the middle band from above. It sets 0.5% take profit and 3% stop loss, belonging to a short-term trading strategy.

## Strategy Logic

The middle band of Bollinger Bands is the N-day simple moving average of closing price. The upper band is middle band + K times the N-day standard deviation of closing price. The lower band is middle band - K times the N-day standard deviation of closing price. It goes long when price breaks above the middle band from below, and it goes short when price breaks below the middle band from above. It opens fixed size for each trade and sets 0.5% take profit and 3% stop loss.

## Advantage Analysis

1. Using Bollinger Bands to determine trading signals can effectively capture price breakouts.
2. Adopting short-term trading, the trading cycle is very short which allows quickly switching directions.
3. Fixed size position and stop profit/loss setting manage risks well per trade.

## Risk Analysis

1. Bollinger Bands are sensitive to market volatility. Improper parameter settings may lead to more signals but lower win rate.
2. High frequency trading can significantly reduce profit margin if commissions are comparatively high.
3. Improper stop profit/loss setting may lead to premature stop loss or miss bigger profits.

Solutions:

1. Optimize parameters to find the best combination.
2. Select securities with lower commissions.
3. Optimize stop profit/loss levels through backtesting.

## Optimization

1. Combine with other indicators like K line patterns and MACD to filter signals and improve win rate.
2. Add more types of take profit such as trailing stop or partial closing to expand profit potential.
3. Optimize parameters of Bollinger Bands and stop profit/loss levels to find the best combination.

## Conclusion

The overall logic of this strategy is clear. Using Bollinger Bands to determine signals is effective. However, high trading frequency and limited profit space per trade are noted. It's recommended to combine trend indicators to filter signals and optimize parameters to improve strategy performance.

||

## Overview

This strategy uses the Bollinger Bands indicator to determine trading signals and set stop profit/loss levels. When the price touches the middle band from below, it goes long; when the price touches the middle band from above, it goes short. It sets 0.5% take profit and 3% stop loss, belonging to a short-term trading strategy.

## Strategy Logic

The middle band of Bollinger Bands is the N-day simple moving average of closing price. The upper band is the middle band + K times the N-day standard deviation of closing price. The lower band is the middle band - K times the N-day standard deviation of closing price. It goes long when the price breaks above the middle band from below, and it goes short when the price breaks below the middle band from above. Fixed size positions are opened for each trade, and 0.5% take profit and 3% stop loss are set.

## Advantage Analysis

1. Using Bollinger Bands to determine trading signals can effectively capture price breakouts.
2. Adopting short-term trading allows very quick switching between long and short positions.
3. Fixed size positions and stop profit/loss settings manage risks well per trade.

## Risk Analysis

1. The Bollinger Bands are sensitive to market volatility, and improper parameter settings may lead to more signals but lower win rate.
2. High-frequency trading can significantly reduce profit margins if commissions are relatively high.
3. Improper take profit or stop loss levels might result in premature stop losses or missing out on larger profits.

Solutions:

1. Optimize parameters to find the best combination.
2. Select securities with lower commissions.
3. Optimize take profit and stop loss settings through backtesting.

## Optimization

1. Combine other indicators like K line patterns and MACD to filter signals and improve win rate.
2. Add more types of take profit such as trailing stop or partial closing to expand profit potential.
3. Optimize parameters of Bollinger Bands and stop profit/loss levels to find the best combination.

## Conclusion

The overall logic of this strategy is clear. Using Bollinger Bands to determine signals is effective, but high trading frequency and limited profit space per trade are noted. It's recommended to combine trend indicators to filter signals and optimize parameters to improve strategy performance.

||

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|20|Longitud|
|v_input_2|2|Multiplicador|


> Source (PineScript)

```pinescript
//@version=5
strategy("Bollinger Bands Short-Term Trading Strategy", shorttitle="BB Strategy", overlay=true)

// Bollinger Bands parameters
length = input(20, title="Length")
mult = input(2.0, title="Multiplier")

// Calculate the Bollinger Bands
basis = ta.sma(close, length)
upper_band = basis + mult * ta.stdev(close, length)
lower_band = basis - mult * ta.stdev(close, length)

// Trading conditions
price_touches_basis_up = ta.crossover(close, basis)
price_touches_basis_down = ta.crossunder(close, basis)

// Strategy logic
if (price_touches_basis_up)
    strategy.entry("Buy", strategy.long, qty=1)
    
if (price_touches_basis_down)
    strategy.entry("Sell", strategy.short, qty=1)

// Logic to close the trade with a 0.5% take profit or 3% stop loss
target_profit = 0.005 // Updated to 0.5%
stop_loss = 0.03

if (strategy.position_size > 0)
    strategy.exit("Take Profit/Close", from_entry="Buy", profit=close * (1 + target_profit))
    strategy.exit("Stop Loss/Close", from_entry="Buy", loss=close * (1 - stop_loss))

if (strategy.position_size < 0)
    strategy.exit("Take Profit/Close", from_entry="Sell", profit=close * (1 - target_profit))
    strategy.exit("Stop Loss/Close", from_entry="Sell", loss=close * (1 + stop_loss))

// Plot the Bollinger Bands on the chart
plot(upper_band, color=color.blue, title="Upper Band")
plot(lower_band, color=color.red, title="Lower Band")
plot(basis, color=color.green, title="Basis")

```

> Detail

https://www.fmz.com/strategy/443252

> Last Modified

2024-03-01 13:29:47
```