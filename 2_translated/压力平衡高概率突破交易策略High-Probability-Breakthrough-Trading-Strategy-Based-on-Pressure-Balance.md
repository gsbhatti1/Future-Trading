> Name

High-Probability-Breakthrough-Trading-Strategy-Based-on-Pressure-Balance

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/d5712c5dcca8cfbd3c.png)
[trans]

#### Overview

This strategy utilizes a combination of multiple indicators to determine the trend direction and trading opportunities, adopting a pressure balance approach to enhance the winning rate. It primarily uses MACD, PSAR, and EMA indicators for judgment, integrating stop-loss and take-profit points to achieve efficient profitability.

#### Strategy Logic

1. Use EMA to calculate the moving average to determine the overall trend direction. A larger EMA value indicates an uptrend, while a smaller EMA value suggests a downtrend.

2. Use MACD to calculate the difference between fast and slow lines. When the difference is greater than 0, it indicates an uptrend; when less than 0, it indicates a downtrend.

3. Use PSAR to calculate continuous turning points. A larger PSAR value suggests a downtrend, while a smaller PSAR value suggests an uptrend.

4. Combine the above three indicators to determine trend consistency. When all three indicators give consistent results, it signals a clear trend and allows for entry or exit.

5. Enter trades based on buy and sell conditions, set stop-loss and take-profit points, and close positions when stop-loss or take-profit conditions are met to achieve profits.

6. Specific rules include:
   - Buy condition: not in an uptrend, MACD difference < 0, closing price > EMA
   - Sell condition: in an uptrend, MACD difference > 0, closing price < EMA
   - Stop loss condition: price reaches the next PSAR value
   - Take profit condition: reaching a preset take-profit ratio

#### Advantages of the Strategy

1. Using multiple indicators to determine trends improves accuracy.

2. Adopting a pressure balance approach increases winning probability when entering trades during clear trends.

3. Setting stop-loss and take-profit points limits losses and locks in profits.

4. Clear and systematic trading rules make it suitable for algorithmic trading.

5. Parameters can be optimized to adapt to different products and timeframes.

#### Risks of the Strategy

1. Incorrect trend judgment may result in wrong trade direction.

2. Extreme market movements may generate false signals from indicators.

3. Stop-loss points set too wide, unable to exit timely.

4. Improper parameter tuning leads to over-trading or missing trades.

5. Illiquid products cannot fulfill stop-loss and take-profit plans.

6. Risks can be mitigated by optimizing parameters, adjusting stops, and selecting liquid products.

#### Optimization Directions

1. Adjust the EMA period to optimize trend accuracy.
2. Tune MACD fast and slow periods for better sensitivity.
3. Optimize stop-loss and take-profit ratios to find the ideal balance.
4. Add other auxiliary indicators to improve entry timing.
5. Select products with good liquidity and significant price fluctuations.
6. Adjust timeframes to suit different product characteristics.

#### Summary

This strategy integrates multiple indicators for trend analysis, entering trades based on clear trends, while setting stop-loss and take-profit points to effectively capture market movements and achieve good returns while ensuring a certain level of profitability. Further improvements in stability and profitability can be achieved through parameter tuning and additional indicators. The clear trading rules make this strategy very suitable for algorithmic trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|60|Length EMA|
|v_input_2_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_3|12|Fast Length MACD|
|v_input_4|26|Slow Length MACD|
|v_input_5|9|Signal Smoothing|
|v_input_6|0|Oscillator MA Type MACD: EMA|SMA|
|v_input_7|0|Signal Line MA Type MACD: EMA|SMA|
|v_input_8|0.02|Start|
|v_input_9|0.02|Increment|
|v_input_10|0.2|Maximum|
|v_input_11|0.245|tplong|
|v_input_12|true|sllong|
|v_input_13|0.055|tpshort|
|v_input_14|0.03|slshort|

> Source (PineScript)

```pinescript
//@version=4
strategy(title = "Crypto Scalper", overlay = true, pyramiding=1, initial_capital = 100, default_qty_type=strategy.percent_of_equity, default_qty_value = 100, calc_on_order_fills=false, slippage=0, commission_type=strategy.commission.percent,commission_value=0.03)
len = input(60, minval=1, title="Length EMA")
src = input(close, title="Source")
out = ema(
```