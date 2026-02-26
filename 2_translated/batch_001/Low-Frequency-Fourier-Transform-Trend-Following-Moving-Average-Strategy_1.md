> Name

Low-Frequency-Fourier-Transform-Trend-Following-Moving-Average-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/eb94868f5596d2b52f.png)
[trans]

### Overview

This strategy is a trend following strategy that uses low frequency Fourier transform to extract the low frequency trend components from the price series and combines three moving averages (fast, medium and slow) to identify trends and generate trading signals. It goes long when the fast MA crosses above the medium MA and the price is above the slow MA, and goes short when the fast MA crosses below the medium MA and the price is below the slow MA. This strategy is suitable for tracking medium- and long-term trends.

### Strategy Logic

1. Use low frequency Fourier transform to extract the low frequency trend components from the price series. The low frequency Fourier transform can effectively filter out high frequency noise, making the extracted trend signals smoother.

2. Use three moving averages (fast, medium and slow) to judge trends. The slow MA has a period of 200, the medium MA has a period of 20, and the fast MA has a period of 5. The slow MA filters out noise, the medium MA captures trend reversals, and the fast MA generates trading signals.

3. When the fast MA crosses above the medium MA and the price is above the slow MA, the market is judged to be entering an upward trend, go long. When the fast MA crosses below the medium MA and the price is below the slow MA, the market is judged to be entering a downward trend, go short.

4. This is a trend following strategy. Once a trend is identified, it will try to hold the position as long as possible to profit from the trend.

### Advantage Analysis

1. The use of low frequency Fourier transform effectively filters out high frequency noise, making the identified trend signals more reliable and stable.

2. The adoption of fast, medium and slow MAs effectively judges the reversal of market trends and avoids false signals. The large parameter setting of the slow MA effectively filters out noise.

3. This strategy has significant advantages in tracking medium- and long-term trends. Once a trend is identified, it will continue to add positions to track the trend, thus obtaining excess returns.

4. This strategy has large parameter optimization space. Users can adjust parameters according to different varieties and cycles to improve adaptability.

### Risk Analysis

1. As a trend following strategy, this strategy cannot effectively determine and react to trend reversals caused by sudden events, which may lead to increased losses.

2. In oscillating markets, this strategy will generate more profitable and losing trades. But it can still be profitable eventually, requiring some psychological endurance.

3. Traditional trend following strategies tend to "dull," exiting trends prematurely is a problem that this strategy needs to solve.

4. Stop loss can be set to control single loss. Sudden event tests can also be included in backtesting to assess the risk resistance of the strategy.

### Optimization Directions

1. Try different moving average algorithms to adapt more varieties and cycles.

2. Add stop loss, consecutive loss exit and other stop loss strategies to control risks.

3. Add trend strength indicators to avoid too many transactions in oscillating and weak trend markets.

4. Add machine learning models to judge trend reversals, making the strategy somewhat adaptive to sudden events.

### Summary

This low frequency Fourier transform trend following moving average strategy has the advantages of filtering noise, identifying trends, and tracking trends. It is suitable for medium- and long-term holding. As a trend following strategy, it mainly faces the risks of trend reversal and sustained oscillation. There are coping strategies for these risks. In general, this strategy has large parameter space and high optimization potential. It is suitable for investors with certain strategy development and risk control capabilities to verify in live trading.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|200|Slow MA period|
|v_input_3|20|Mid MA period|
|v_input_4|5|Fast MA period|
|v_input_5|true|Use MA|
|v_input_6|true|First sinusoid|
|v_input_7|2|Second sinusoid|
|v_input_8|3|Third sinusoid|
|v_input_9|0|MA Type: EMA|SMA|ALMA|FRAMA|RMA|SWMA|VWMA|WMA|LinearRegression|
|v_input_10|false|Use linear regression?|
|v_input_11|13|Linear regression length|
|v_input_12|false|Linear regression offset|
|v_input_13|0|Lookback Period: 64|4|8|16|32|2|128|256|512|1024|2048|4096|
|v_input_14|false|Take Profit Points|
|v_input_15|false|Stop Loss Points|