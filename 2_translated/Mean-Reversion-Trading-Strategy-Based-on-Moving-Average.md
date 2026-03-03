> Name

Mean-Reversion-Trading-Strategy-Based-on-Moving-Average

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/13f1e11f7f054b48ef9.png)

[trans]

### Overview

The mean reversion trading strategy is based on the price deviation from a moving average to make trading decisions. It takes advantage of the short-term deviation and long-term reversion pattern of prices to the mean by establishing positions when prices significantly below or above the moving average and closing positions when prices revert back.

### Strategy Logic

The strategy first calculates a moving average over a certain period to represent the long-term price trend. Then it determines the timing and size of positions based on the deviation of price from the moving average.

When the price falls below the moving average by a certain percentage, it signals the price deviates from the long-term trend. In this case, long positions are gradually built with increasing size as the deviation widens. When the price bounces back above the moving average, suggesting a reversion to the mean, the long positions are closed for profit taking.

Similarly, when the price rises above the moving average by a threshold, short positions are built. When the price drops back towards the moving average, the short positions are closed with profits.

### Advantage Analysis

1. Utilize the trend identification ability of moving averages to follow the long-term equilibrium trend of stock prices and identify the major trend direction.
2. Lower the average cost by scaling into positions, obtaining better entry prices.
3. Adopt staged take-profit to secure profits at different levels of mean reversion, lowering risks.
4. Control position sizing by fixed percentage to limit single trade loss size.
5. Flexible parameter settings such as moving average period and position sizing depending on different products.

### Risk Analysis

1. Frequent stop loss when prices oscillate. Can widen stop loss range or add other filters.
2. Strong trend may break through moving average, unable to close at mean reversion. Can reduce position size identified by trend strength indicators.
3. Improper parameter settings may result in over-aggressive entries or stops. Cautious backtesting and adjustment based on market conditions are necessary.
4. High trading frequency leads to substantial trading costs. Cost factors should be considered in parameter optimization.

### Improvement Directions

1. Optimize moving average period to adapt to product characteristics.
2. Optimize position sizing to balance risk and return.
3. Add other technical filters to avoid unnecessary trades.
4. Incorporate volatility measures to adjust position size based on market fluctuation levels.
5. Introduce profit target scaling to lower risk and increase return.

### Conclusion

The mean reversion strategy utilizes the equilibrium reversion tendency of stocks by entering on deviation from the moving average and taking profit on reversion. With proper parameter tuning and filters, it can adapt to market changes and achieve good returns under risk control. The strategy incorporates both trend following and risk management, making it worth researching and applying for investors.

||

### Overview

The mean reversion trading strategy is based on the price deviation from a moving average to make trading decisions. It takes advantage of the short-term deviation and long-term reversion pattern of prices to the mean by establishing positions when prices significantly below or above the moving average and closing positions when prices revert back.

### Strategy Logic

The strategy first calculates a moving average over a certain period to represent the long-term price trend. Then it determines the timing and size of positions based on the deviation of price from the moving average.

When the price falls below the moving average by a certain percentage, it signals the price deviates from the long-term trend. In this case, long positions are gradually built with increasing size as the deviation widens. When the price bounces back above the moving average, suggesting a reversion to the mean, the long positions are closed for profit taking.

Similarly, when the price rises above the moving average by a threshold, short positions are built. When the price drops back towards the moving average, the short positions are closed with profits.

### Advantage Analysis

1. Utilize the trend identification ability of moving averages to follow the long-term equilibrium trend of stock prices and identify the major trend direction.
2. Lower the average cost by scaling into positions, obtaining better entry prices.
3. Adopt staged take-profit to secure profits at different levels of mean reversion, lowering risks.
4. Control position sizing by fixed percentage to limit single trade loss size.
5. Flexible parameter settings such as moving average period and position sizing depending on different products.

### Risk Analysis

1. Frequent stop loss when prices oscillate. Can widen stop loss range or add other filters.
2. Strong trend may break through moving average, unable to close at mean reversion. Can reduce position size identified by trend strength indicators.
3. Improper parameter settings may result in over-aggressive entries or stops. Cautious backtesting and adjustment based on market conditions are necessary.
4. High trading frequency leads to substantial trading costs. Cost factors should be considered in parameter optimization.

### Improvement Directions

1. Optimize moving average period to adapt to product characteristics.
2. Optimize position sizing to balance risk and return.
3. Add other technical filters to avoid unnecessary trades.
4. Incorporate volatility measures to adjust position size based on market fluctuation levels.
5. Introduce profit target scaling to lower risk and increase return.

### Conclusion

The mean reversion strategy utilizes the equilibrium reversion tendency of stocks by entering on deviation from the moving average and taking profit on reversion. With proper parameter tuning and filters, it can adapt to market changes and achieve good returns under risk control. The strategy incorporates both trend following and risk management, making it worth researching and applying for investors.

||

### Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|28|Moving Average (bars)|
|v_input_2|5|Deviation Increment (%)|
|v_input_3|true|Level 1 (units)|
|v_input_4|2|Level 2 (units)|
|v_input_5|4|Level 3 (units)|
|v_input_6|8|Level 4 (units)|
|v_input_7|16|Level 5 (units)|


> Source (PineScript)

``` pinescript
/*backtest
start: 2022-10-19 00:00:00
end: 2023-10-25 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("YJ Mean Reversion", overlay=true)
//Was designed firstly to work on an index like the S&P 500, which over time tends to go up in value. 
//Avoid trading too frequently (e.g. Daily, Weekly), to avoid getting eaten by fees. 
//If you change the underlying asset, or time frame, tweaking the moving average may be necessary. 
//Can work with a starting capital of just $1000, optimise the settings as necessary. 
//Accepts floating point values for the amount of units to purchase (e.g. Bitcoin). 
//If price of units exceeds available capital, script will cancel the buy. 
//Adjusted the input parameters to be more intuitive.

//input variables
movingAverage = input(title="Moving Average (bars)", type=input.integer, defval=28, minval=1, maxval=1000)
//riskPercentage = input(title="Amount to Risk (%)", type=input.integer, defval=1, minval=1, maxval=50)
deviation = input(title="Deviation Increment (%)", type=input.float, defval=5, minval=0.01, maxval=100) / 100
unitsLevel1 = input(title="Level 1 (units)", type=input.float, defval=1, minval=0.0001, maxval=10000)
unitsLevel2 = input(title="Level 2 (units)", type=input.float, defval=2, minval=0.0001, maxval=10000)