> Name

Dual-Moving-Average-Turning-Point-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/194d3c1321b0c207a99.png)

[trans]

### Overview

The Dual Moving Average Turning Point strategy is a trading strategy based on the crossover of moving averages. It uses two moving averages with different parameter settings and determines entry and exit points according to their turning points. This strategy is simple and intuitive, easy to implement, and suitable for medium-to-long term trading.

### Strategy Logic

The strategy uses Price as the price input source and calculates two moving averages, SMA1 and SMA2, with different parameters. It uses the ROC indicator to determine the turning points of the moving averages. When SMA1's ROC value exceeds the positive threshold, it is considered an upward turn of SMA1 and an upward signal is recorded. When SMA1's ROC value breaks the negative threshold, it is considered a downward turn of SMA1 and a downward signal is recorded. The judgment logic for SMA2 is similar.

When SMA1 turns upward and the previous bar's SMA2 turns downward, a buy signal is generated to go long. When SMA1 turns downward and the previous bar's SMA2 turns upward, a sell signal is generated to go short.

The strategy uses the turning points of two moving averages to determine the trading direction and the turning point of one moving average to confirm entry timing. The dual moving average crossover ensures the trend has changed when entering the market, which helps avoid false breakouts.

### Advantage Analysis

- Using dual moving average crossover and turning points can effectively filter out false breakouts and improve entry accuracy.

- Combining moving average turning points with the ROC indicator can clearly identify turning points and avoid frequent trading.

- Adopting medium-to-long-term dual moving averages can track the main trend and achieve sizable trend profits.

- The strategy logic is simple and clear, easy to understand and implement, suitable for quant trading beginners.

- Customizable parameters suit different market environments with strong adaptability.

### Risk Analysis

- Dual moving average crossovers may generate many false signals in ranging markets, leading to losses.

- The ROC parameters need precise optimization, otherwise turn recognition will have errors, affecting strategy performance.

- Large periodic ranging markets may trigger stop loss multiple times. Expanding stop loss range can avoid it.

- Relying solely on moving averages, it's hard to respond to sudden events like major news, which may lead to losses.

- Note the overfitting problem in parameter optimization. Test period should be long enough to include different market conditions.

### Optimization Directions

- Optimize moving average parameters to find the best moving average period combination.

- Optimize ROC parameters to improve turning point recognition accuracy.

- Add stop loss mechanisms, such as dynamic stop loss based on breaking customized price levels.

- Add additional conditions like volume indicators to avoid false breakouts.

- Incorporate other indicators like MACD, BOLL to improve decision making.

- Use machine learning etc. to auto optimize parameters and adapt to market changes.

### Summary

In summary, the Dual Moving Average Turning Point strategy is a simple and practical trend following strategy. It can be implemented with basic moving average indicators and has clear, easy-to-understand logic, making it very suitable for quant trading beginners to learn and practice. With parameter optimization and stop loss optimization, the strategy stability can be greatly improved. Combining with other auxiliary indicators can further enhance the strategy. The highly customizable strategy can be flexibly applied to different market environments and is a recommended dual moving average trading strategy.

[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_close|0|Source: close|high|low|open|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|25|1st MA Length|
|v_input_3|0|1st MA Type: HMA|EMA|SMA|VWMA|
|v_input_4|true|Lookback 1|
|v_input_5|2.5|Minimum slope magnitude * 100|


> Source (PineScript)

```pinescript
//@version=3
strategy("MA Turning Point Strategy", overlay=true)
src = input(close, title="Source")

price = request.security(syminfo.tickerid, timeframe.period, src)
ma1 = input(25, title="1st MA Length")
type1 = input("HMA", "1st MA Type", options=["SMA", "EMA", "HMA", "VWMA"])
f_hma(_src, _length)=>
    _return = wma((2*wma(_src, _length/2))-wma(_src, _length/2), _length/4)
    _return
```