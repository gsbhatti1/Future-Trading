```markdown
> Name

Dynamic-Average-Cost-Dollar-Cost-Averaging-Compound-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/198c51b795f2997eeab.png)
[trans]

#### Overview

The dynamic average cost DCA compound strategy dynamically adjusts the quantity of each opening position. At the beginning of the trend, it first opens small positions to build a position. As the depth of consolidation increases, it gradually increases the position size. The strategy uses exponential functions to calculate stop loss price levels, and re-opens new batches when triggered, which can cause the cost of holding positions to continue to decline exponentially. As the depth increases, the cost of the positions can be gradually reduced. When the price reverses, the batch profit taking allows for greater returns.

#### Strategy Logic

This strategy uses a simple combination of RSI oversold signals and moving averages timing to determine entry opportunities. A first entry order is submitted when RSI drops below the oversold level and the close price is below the moving average. After the first entry, the exponential function calculates the price drop percentage for subsequent levels. Each time it triggers a DCA order, position sizing is recalculated to keep an equal amount per entry. As position size and cost change dynamically, this creates a leverage effect.

As the number of DCA cycles increases, the average holding cost continues to decline. Just a small rebound is enough for take profit on each position. After continuous entries are submitted, a stop loss line is plotted above the average holding price. Once the price breaks out above the average price and the stop loss line, all positions are closed.

The biggest advantage is that as the holding cost continues to decline, even during consolidation periods, cost can still be reduced step by step cumulatively. When the trend reverses, due to much lower holding costs than market prices, much greater profits can be realized.

#### Risks and Defects

The biggest risk is the limited position size initially. During continuous declines, there can be stop loss risks. So the stop loss percentage needs to be set reasonably based on personal risk appetite.

Additionally, setting the stop loss level has two extremes: if too loose, not enough retracement can be captured; but if too tight, the probability of getting stopped out during mid-term corrections increases. Therefore, choosing proper stop loss levels according to different market conditions and individual risk preferences is crucial.

If there are too many DCA levels, when prices rise substantially, extremely high holding costs may prevent effective stop losses. Thus, the maximum number of DCA layers should be set reasonably based on total capital allocation and the highest cost one can endure.

#### Optimization Suggestions

1. Optimize entry timing signals by testing different parameters and indicator combinations for higher win rate signals.
2. Optimize stop loss mechanisms by testing Λ trailing stop loss or curve-fitted trailing stop loss to achieve better results. Also, levels can be adjusted dynamically based on position allocation percentage.
3. Optimize take profit methods by testing different types of trailing take profits to find the best exit opportunities and enhance overall return.
4. Add anti-whipsaw mechanisms. Sometimes DCA signals can be triggered again soon after a stop loss event. A whipsaw range can be added to avoid aggressive re-entries right after stops.

#### Conclusion

This strategy utilizes RSI to determine entry points, with an exponential dynamic stop loss DCA mechanism to adjust position sizing and average costs dynamically. This allows for gaining price advantages during consolidation periods while providing more operational space in consolidations and achieving higher returns during trends. However, parameters still need to be set carefully based on capital allocation plans to control overall position risks.

||

#### Overview

The dynamic average cost DCA compound strategy dynamically adjusts the quantity of each opening position. At the beginning of the trend, it first opens small positions to build a position. As the depth of consolidation increases, it gradually increases the position size. The strategy uses exponential functions to calculate stop loss price levels, and re-opens new batches when triggered, which can cause the cost of holding positions to continue to decline exponentially. As the depth increases, the cost of the positions can be gradually reduced. When the price reverses, the batch profit taking allows for greater returns.

#### Strategy Logic

This strategy uses a simple combination of RSI oversold signals and moving averages timing to determine entry opportunities. A first entry order is submitted when RSI drops below the oversold level and the close price is below the moving average. After the first entry, the exponential function calculates the price drop percentage for subsequent levels. Each time it triggers a DCA order, position sizing is recalculated to keep an equal amount per entry. As position size and cost change dynamically, this creates a leverage effect.

As the number of DCA cycles increases, the average holding cost continues to decline. Just a small rebound is enough for take profit on each position. After continuous entries are submitted, a stop loss line is plotted above the average holding price. Once the price breaks out above the average price and the stop loss line, all positions are closed.

The biggest advantage is that as the holding cost continues to decline, even during consolidation periods, cost can still be reduced step by step cumulatively. When the trend reverses, due to much lower holding costs than market prices, much greater profits can be realized.

#### Risks and Defects

The biggest risk is the limited position size initially. During continuous declines, there can be stop loss risks. So the stop loss percentage needs to be set reasonably based on personal risk appetite.

Additionally, setting the stop loss level has two extremes: if too loose, not enough retracement can be captured; but if too tight, the probability of getting stopped out during mid-term corrections increases. Therefore, choosing proper stop loss levels according to different market conditions and individual risk preferences is crucial.

If there are too many DCA levels, when prices rise substantially, extremely high holding costs may prevent effective stop losses. Thus, the maximum number of DCA layers should be set reasonably based on total capital allocation and the highest cost one can endure.

#### Optimization Suggestions

1. Optimize entry timing signals by testing different parameters and indicator combinations for higher win rate signals.
2. Optimize stop loss mechanisms by testing Λ trailing stop loss or curve-fitted trailing stop loss to achieve better results. Also, levels can be adjusted dynamically based on position allocation percentage.
3. Optimize take profit methods by testing different types of trailing take profits to find the best exit opportunities and enhance overall return.
4. Add anti-whipsaw mechanisms. Sometimes DCA signals can be triggered again soon after a stop loss event. A whipsaw range can be added to avoid aggressive re-entries right after stops.

#### Conclusion

This strategy utilizes RSI to determine entry points, with an exponential dynamic stop loss DCA mechanism to adjust position sizing and average costs dynamically. This allows for gaining price advantages during consolidation periods while providing more operational space in consolidations and achieving higher returns during trends. However, parameters still need to be set carefully based on capital allocation plans to control overall position risks.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|timestamp(01 April 2021 20:00)|(?Backtest Window)Start Time|
|v_input_2|timestamp(01 Aug 2030 20:00)|End Time|
|v_input_float_1|3|(?Risk)Take Profit %|
|v_input_float_2|6|Close All %|
|v_input_int_1|8|(?DCA Settings)Max Amount of Entries|
|v_input_float_3|2|Price Drop % to open First DCA Order|
|v_input_float_4|1.4|Exponential Scale DCA levels|
|v_input_int_2|4999|Lines Bar Lookback|
|v_input_bool_1|false|(?Moving Average)Plot Moving Average|
|v_input_int_3|100|MA Length|
|v_input_int_4|14|(?RSI Settings)RSI Length|
|v_input_source_1_close|0|Source
```