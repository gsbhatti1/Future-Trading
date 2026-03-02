> Name

Momentum-Reversal-Moving-Average-Combination-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/145e902ff92c994dc34.png)
[trans]

## Overview
This strategy identifies trends by combining multiple moving average indicators. Specifically, this strategy uses a fast moving average ribbon and a slow moving average ribbon at the same time. The fast moving average ribbon consists of a 5-day EMA and a 25-day WMA, while the slow moving average ribbon consists of a 28-day EMA and a 72-day WMA. It generates a buy signal when the fast MA crosses above the slow MA, and a sell signal when the fast MA crosses below the slow MA. In addition, this strategy also uses the RSI indicator to assist in judging the timing.

## Strategy Logic
1. Use double moving averages to determine the trend direction
    - Fast MA Ribbon: 5-day EMA, 25-day WMA 
    - Slow MA Ribbon: 28-day EMA, 72-day WMA
    - When fast MA crosses above slow MA, generate a buy signal  
    - When fast MA crosses below slow MA, generate a sell signal
2. Use RSI indicator to assist in determining the timing of buys and sells
    - RSI Low to Buy: Generate a buy signal when RSI<35 
    - RSI High to Sell: Generate a sell signal when RSI>65
3. Adopt trend tracking mechanisms including moving stop loss and moving take profit
    - Moving stop loss: Track highest/lowest price to prevent excessive losses
    - Moving take profit: Track highest/lowest price for timely profit taking

## Advantage Analysis
1. Using double MAs to determine trends, fast and slow MAs working together can effectively identify turning points  
2. RSI indicator’s assistance helps avoid erroneous signals from MAs
3. Moving stop loss mechanism effectively controls losses of individual losing trades  
4. Moving take profit mechanism locks in profits and prevents profit retracement

## Risk Analysis
1. Relatively high probability of failure in trend determination by double MAs, may generate false signals
2. Improper RSI parameter settings may miss trading opportunities  
3. Excessively large stop loss magnitude may cause unnecessary losses
4. Excessively small take profit magnitude may result in profit shrinkage

## Optimization Directions
1. Parameters of fast and slow MAs can be optimized to find optimal parameter combinations
2. RSI parameters can also be optimized to find better overbought/oversold lines  
3. Test with different stop loss magnitudes to find balance between minimizing losses and avoiding false signals
4. Try adaptive take profit strategies to allow take profit magnitude to adjust on its own based on market volatility

## Conclusion
This strategy captures and tracks trends by determining trend direction with double MAs, judging timing assisted by RSI, and methods like moving take profit and stop loss. Further improvements can be achieved by optimizing parameters of MAs, RSI and profit/loss limits. The overall logic is clear and easy to understand and optimize. It is a practical and effective trend tracking strategy.

||

## Overview
This strategy identifies trends using multiple moving average indicators combined together. Specifically, it utilizes both fast and slow moving average ribbons simultaneously. The fast MA ribbon comprises of 5-day EMA and 25-day WMA whereas the slow MA ribbon consists of 28-day EMA and 72-day WMA. A buy signal is generated when the fast MA crosses above the slow MA, while a sell signal occurs when the fast MA falls below the slow MA. Additionally, an RSI indicator is employed to assist in timing decisions.

## Strategy Logic
1. Determine trend direction using double moving averages
    - Fast MA Ribbon: 5-day EMA, 25-day WMA 
    - Slow MA Ribbon: 28-day EMA, 72-day WMA
    - Buy signal generated when the fast MA crosses above the slow MA  
    - Sell signal generated when the fast MA crosses below the slow MA
2. Use RSI to assist in timing trades
    - RSI Low to Buy: Generate a buy signal when RSI <35 
    - RSI High to Sell: Generate a sell signal when RSI >65
3. Implement trend tracking mechanisms including moving stop loss and moving take profit
    - Moving Stop Loss: Track the highest or lowest price to prevent excessive losses
    - Moving Take Profit: Track the highest or lowest price for timely profits

## Advantage Analysis
1. Using double MAs enhances the accuracy of identifying turning points in trends  
2. RSI helps avoid misinterpretation by incorrect MA signals
3. A moving stop loss effectively mitigates individual losing trades
4. A moving take profit locks in profits and prevents profit erosion

## Risk Analysis
1. The trend determination through double MAs may generate false signals with a relatively high probability
2. Incorrect RSI parameter settings could miss trading opportunities  
3. Excessively wide stop loss levels may lead to unneeded losses
4. A narrow take profit level might result in reduced profits

## Optimization Directions
1. Optimize parameters of the fast and slow MAs for better performance 
2. Improve the overbought/oversold lines by tuning RSI parameters  
3. Experiment with different stop loss levels to find a balance between minimizing losses and reducing false signals
4. Explore adaptive take profit strategies that adjust based on market volatility

## Conclusion
This strategy captures trends using double moving averages, assists in trading timing through the RSI indicator, and implements moving stop and take profit mechanisms for effective trend following. Further optimization can be achieved by adjusting MA and RSI parameters as well as setting appropriate profit/loss limits. The overall logic is straightforward and easily adaptable, making it a practical and efficient trend-following strategy.

||

> Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|true|IS This a RENKO Chart|
|v_input_2|false|Alternate TimeFrame Multiplier (0=none)|
|v_input_3|false|Show Coloured MA Ribbons|
|v_input_4|false|Show Ribbon Median MA Lines|
|v_input_5|0|FAST MA Ribbon Type: : EMA|SMA|WMA|VWMA|SMMA|DEMA|TEMA|LAGMA|HullMA|ZEMA|TMA|SSMA|
|v_input_6|5|FAST Ribbon Lower MA Length|
|v_input_7|25|FAST Ribbon Upper Length|
|v_input_8|0|SLOW MA Ribbon Type: : EMA|SMA|WMA|VWMA|SMMA|DEMA|TEMA|LAGMA|HullMA|ZEMA|TMA|SSMA|
|v_input_9|28|SLOW Ribbon Lower MA Length|
|v_input_10|72|SLOW Ribbon Upper Length|
|v_input_11|2018|Backtest Start Year|
|v_input_12|true|Backtest Start Month|
|v_input_13|true|Backtest Start Day|
|v_input_14|0.02|start|
|v_input_15|0.02|increment|
|v_input_16|0.2|maximum|
|v_input_17|false|Use Opposite Trade as a Close Signal|
|v_input_18|true|Colour Candles to Trade Order state|
|v_input_19|0|What type of Orders: Longs+Shorts|LongsOnly|ShortsOnly|Flip|
|v_input_20|true|Trailing Stop|
|v_input_21|3|Trailing Stop (%)|
|v_input_22|true|Take Profit|
|v_input_23|3|Take Profit (%)|
|v_input_24|true|Trailing Profit (%)|
|v_input_25|false|Stop Loss|
|v_input_26|3|Stop Loss (%)|

> Source (PineScript)

```pinescript
//@version=3
strategy(title="[WAI GUA]", shorttitle="[EOS] 1.0", overlay=false )

//study(title="[WAI GUA]", shorttitle="[EOS] 1.0", overlay=true)

//
// Use Alternate Anchor TF for MAs 
uRenko    = input(true, title="IS This a RENKO Chart")
//
anchor     = input(0,minval=0,maxval=1440,title="Alternate TimeFrame Multiplier (0=none)")
//
src          = close //input(close, title="EMA Source")
showRibbons  = input(false,title="Show Coloured MA Ribbons")
showAvgs     = input(false,title="Show Ribbon Median MA Lines")

```

