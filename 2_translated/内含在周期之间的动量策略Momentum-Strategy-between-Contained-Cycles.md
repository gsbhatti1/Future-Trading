> Name

Momentum-Strategy-between-Contained-Cycles

> Author

ChaoZhang

> Strategy Description

### Overview

The core idea of this strategy is to determine the trend direction using the "contained between cycles" candlestick pattern and use it as an entry signal. When a contained between cycles pattern appears that contains the previous candlestick, we can infer that this is a point where the trend is reversing, at which point we can go long on a breakout above the previous high or go short on a breakout below the previous low, with proper stop loss and take profit setup.

### Strategy Logic

1. Check if the contained between cycles pattern occurs. The specific logic is: the current candle's high is lower than the previous candle's high, and the current candle's low is higher than the previous candle's low.
2. Determine if the previous candle was bullish or bearish. If the close was higher than the open, it was bullish. If the close was lower than the open, it was bearish.
3. If the previous candle was bullish and the contained pattern occurs, place a buy stop order at the previous candle's high plus 10% of its range.
4. If the previous candle was bearish and the contained pattern occurs, place a sell stop order at the previous candle's low minus 10% of its range.
5. Once the stop order is triggered and position is opened, set the stop loss and take profit. The stop loss and take profit distances are a certain percentage of the previous candle's range.
6. If another inside bar pattern forms, close existing positions first and then place new pending orders.

### Advantage Analysis

The advantages of this strategy include:

1. It utilizes the inherent logic of candlesticks and provides an accurate entry timing. The contained pattern often implies upcoming trend reversal or acceleration.
2. The rules are simple and easy to follow for actual trading.
3. The stop loss and take profit based on previous candle's range helps control risk.
4. New pending orders are placed each time a qualified pattern appears, allowing us to follow the new trend.

### Risk Analysis

There are also some risks:

1. The contained pattern does not always result in trend reversal or acceleration. There are some false signals.
2. The stop loss distance may be too small to withstand large fluctuations in the market.
3. The take profit target may be too wide, preventing timely profits.
4. The strategy relies more on trending markets. The profit potential is limited during consolidation.
5. The high trading frequency leads to large transaction costs.

Solutions:

1. Add other indicators to confirm the signals and reduce false signals.
2. Widen the stop loss slightly but not more than 50% of the previous candle's range.
3. Shorten the take profit target to around 50% of the previous candle's range.
4. Optimize capital management, reduce individual position size for ranging markets.
5. Loosen the entry criteria to reduce trading frequency.

### Optimization Directions

Some ways to optimize the strategy:

1. Add a trend indicator like MACD to determine trend direction, avoiding whipsaws during consolidation.
2. Use more advanced stop loss techniques like trailing stop or profit protection stop loss.
3. Test different stop loss and take profit ratios to find the optimal parameters.
4. Add re-entry logic to capture the trend again after stop loss.
5. Optimize the position sizing based on market volatility.

6. Optimize capital management, such as fixed fractional position sizing.

7. Test the strategy on different products and timeframes.

### Conclusion

In summary, this is a strategy that uses the contained between cycles pattern to determine trend turning points and place pending orders to capture trend reversals. It has the advantages of clear entry signals, simple rules, and controllable risks, but also has some false signal risks and room for optimization. We can further improve its stability and profitability by combining trend filters, optimizing stops, adjusting position sizes etc. It is more suitable for trending markets, and needs to be optimized and tested for different market conditions before actual usage to maximize its effectiveness.

---

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|2018|From Year|
|v_input_2|true|From Month|
|v_input_3|true|From Day|
|v_input_4|9999|To Year|
|v_input_5|true|To Month|
|v_input_6|true|To D