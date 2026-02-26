> Name

Three-Candle-Reversal-Trend-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/8f3663bf3e117cdf31.png)
[trans]
### Overview  

The Three-Candle-Reversal-Trend-Strategy is a short-term trading strategy that identifies reversals in trends by detecting three consecutive bullish or bearish candles followed by an engulfing candle in the opposite direction, combined with multiple technical indicators to filter entry opportunities. The strategy trades with a 1:3 risk-reward ratio for aiming at excess returns.

### Strategy Logic  

The core logic of this strategy is to identify the pattern of three consecutive bullish or bearish candles on the chart, which usually implies an impending reversal in the short-term trend. When three bearish candles are detected, wait for the next engulfing bullish candle to go long. Conversely, when three bullish candles are detected, wait for the next engulfing bearish candle to go short. This allows capturing reversing opportunities in short-term trends in a timely manner.

In addition, multiple technical indicators are introduced to filter entry signals. Two Simple Moving Averages (SMA) lines with different parameter settings are adopted, and entry positions are considered only when the faster SMA crosses over the slower line. Besides, the Linear Regression indicator is used to judge whether the market is ranging or trending, and trades are taken only in trending conditions. There is also an option to combine the candlestick pattern with SMA golden crosses for additional entry signals. Through the comprehensive judgments of these indicators, most noise can be filtered out, and the entry accuracy is improved.

For stop loss and take profit settings, the strategy requires a minimum 1:3 risk-reward ratio. The Average True Range (ATR) indicator based on the price fluctuation of recent N candles is used to determine the stop loss level with an offset percentage. Take profit is then calculated accordingly to target proper excess returns for the risk taken.

### Advantages  

The Three-Candle-Reversal-Trend-Strategy has the following advantages:

1. Identifying short-term trend reversals for timely opportunities
2. Enhanced entry accuracy via multiple indicator filters  
3. Reasonable risk-reward profile with appropriate stop loss and take profit levels
4. Simple parameters for ease of understanding and operation

### Risks  

There are also some risks to note for this strategy:

1. Short-term reversals do not necessarily imply long-term trend reversals. Higher timeframe trends should be monitored. Longer period moving averages can be added as filters.
2. Single candlestick patterns may produce false signals. Other supplementary judgments can be considered.
3. Stop loss settings could be too aggressive. Stop loss range can be tightened.
4. Insufficient backtest data leads to uncertainty in real trading performance.

### Optimization Directions  

The strategy can be optimized in the following aspects:

1. Adjust parameters for moving averages and linear regression to better identify trends.
2. Add other indicators like Stoch for supplementary signal confirmation.
3. Optimize ATR parameters and stop loss percentage to balance risk and return.
4. Introduce trend breakout tracking mechanisms to improve profitability.
5. Establish robust capital management schemes to control trading risks.

### Conclusion  

Overall, the Three-Candle-Reversal-Trend-Strategy utilizes simple price patterns combined with multiple auxiliary indicators for short-term trading, built on a properly balanced risk-reward profile. It delivers decent performance with relatively low complexity and is worth investor attention and testing. There is also ample room for improvement via parameter tuning and rule supplementation to grow into a stable high-efficiency quantified trading strategy.

||

### Strategy Arguments  

|Argument|Default|Description|
|----|----|----|
|v_input_1|2011|(?Trading window) Start Year|
|v_input_int_1|true|Start Month|
|v_input_int_2|true|Start Day|
|v_input_2|2050|Finish Year|
|v_input_int_3|12|Finish Month|
|v_input_int_4|31|Finish Day|
|v_input_bool_1|true|(?Trading Options) SPY trading only|
|v_input_int_5|10|# of SPY options per trade|
|v_input_bool_2|false|reinvest profit?|
|v_input_float_3|3|Reward to Risk Ratio|
|v_input_bool_3|true|No long entry between 10 - 10:30 (Avoid 10 am dump)|
|v_input_bool_4|true|Trade 3s candle pattern|
|v_input_bool_5|true|Trade MA Cross Reversal Signal|
|v_input_int_6|14|(?Daily ATR)ATR period|
|v_input_float_1|5|% ATR to use for SL / PT|
|v_input_int_7|8|(?Moving Averages)Fast EMA|
|v_input_int_8|21|Fast SMMA|
|v_input_int_9|50|Slow SMMA|
|v_input_int_10|200|Slow S