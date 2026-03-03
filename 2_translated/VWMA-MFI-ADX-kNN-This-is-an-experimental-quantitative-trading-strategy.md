> Name

Based on VWMA and MFI-ADX kNN Machine Learning Quantitative Trading Strategy This-is-an-experimental-quantitative-trading-strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/762c27c901eec54e22.png)
[trans]

## Overview

This is an experimental quantitative trading strategy that combines moving average indicators and the kNN machine learning algorithm to generate trading signals. It uses the crossovers of two VWMA lines with different periods to determine the trend direction, and employs MFI and ADX indicators in conjunction with a kNN algorithm to filter the signals and improve their reliability.

## Strategy Principles

The core indicators for this strategy are two VWMA lines with different parameters, referred to as the fast line and slow line. A buy signal is generated when the fast line crosses above the slow line; conversely, a sell signal is issued when the fast line crosses below the slow line. Additionally, the strategy incorporates MFI and ADX indicators to evaluate the reliability of these signals under current market conditions through the kNN classification algorithm.

The fundamental idea behind the kNN algorithm involves comparing new data with historical data to identify the k most similar instances and categorizing based on their majority outcome. In this context, MFI and ADX serve as input parameters for the kNN algorithm to assess historical price movements (uptrend or downtrend) under different combinations of these indicators, thereby filtering the signals to enhance signal quality.

## Strategy Advantages

- Utilizes VWMA's trend-following capabilities, generating trading points via moving average crossovers
- Employs MFI and ADX for multidimensional feature extraction, aiding in trend direction determination
- Leverages kNN machine learning algorithms for dynamic optimization and filtering of trading signals
- An experimental strategy with significant room for improvement through data validation and refinement

## Risks and Mitigations

- VWMA lines can experience lag issues
- MFI and ADX have inherent lags that may misinterpret market conditions
- The choice of kNN algorithm parameters (e.g., the k value) significantly impacts results
- As an experimental strategy, performance in live trading may be suboptimal

Mitigations:

- Adjust MA parameters to minimize lag effects
- Enhance indicator algorithms for more accurate trend determination 
- Optimize kNN parameters to improve fit
- Validate and test the strategy through backtesting and paper trading

## Optimization Directions

There is significant potential for optimizing this strategy:

- Introduce additional moving average indicators to create diverse combinations
- Experiment with different auxiliary indicators such as MACD, KDJ, etc.
- Improve the kNN algorithm by utilizing alternative distance metrics
- Explore other machine learning algorithms like SVM, Random Forest, etc.
- Perform parameter tuning to find the optimal set

By integrating more indicators and machine learning approaches, there is an opportunity for enhanced stability and profitability.

## Summary

This strategy is an experimental quantitative trading approach based on VWMA and kNN machine learning. It combines strong trend-following capabilities with signal filtering via machine learning. There is significant potential for improvement by introducing additional features and optimizing algorithms to achieve better performance. However, as a novel strategy, it also carries certain risks that require further validation and enhancement. Overall, this strategy holds great innovative potential.

||

## Overview

This is an experimental quantitative trading strategy combining moving average indicators with kNN machine learning algorithms to generate trading signals. It uses the crossovers of two VWMA lines with different periods to determine trend direction, and applies MFI and ADX indicators alongside a kNN algorithm for signal filtering to enhance their reliability.

## Strategy Principles

The core indicators are two VWMA lines with distinct parameters: fast line and slow line. A buy signal is generated when the fast line crosses above the slow line; conversely, a sell signal is triggered when the fast line crosses below the slow line. Additionally, MFI and ADX indicators are used to evaluate the reliability of these signals under current market conditions through kNN classification.

The kNN algorithm compares new data with historical data to identify the most similar instances and categorizes based on their majority outcomes. Here, MFI and ADX serve as input parameters for the kNN algorithm to assess historical price movements (uptrend or downtrend) under different combinations of these indicators, thereby filtering signals to improve signal quality.

## Advantages

- Utilizes VWMA's trend-following abilities, generating trading points through moving average crossovers
- Employs MFI and ADX for multidimensional feature extraction, aiding in trend direction determination
- Leverages kNN machine learning algorithms for dynamic optimization and filtering of trading signals
- Experimental strategy with significant room for improvement through data validation and refinement

## Risks and Mitigations

- VWMA lines can experience lag issues
- MFI and ADX have inherent lags that may misinterpret market conditions
- The choice of kNN algorithm parameters (e.g., the k value) significantly impacts results
- As an experimental strategy, performance in live trading may be suboptimal

Mitigations:

- Adjust MA parameters to minimize lag effects
- Enhance indicator algorithms for more accurate trend determination 
- Optimize kNN parameters to improve fit
- Validate and test the strategy through backtesting and paper trading

## Optimization Directions

There is significant potential for optimizing this strategy:

- Introduce additional moving average indicators to create diverse combinations
- Experiment with different auxiliary indicators such as MACD, KDJ, etc.
- Improve the kNN algorithm by utilizing alternative distance metrics
- Explore other machine learning algorithms like SVM, Random Forest, etc.
- Perform parameter tuning to find the optimal set

By integrating more indicators and machine learning approaches, there is an opportunity for enhanced stability and profitability.

## Summary

This strategy is based on VWMA indicators and kNN machine learning. It leverages strong trend-following capabilities combined with signal filtering via machine learning. There is significant potential for improvement by introducing additional features and optimizing algorithms to achieve better results. However, as a novel strategy, it also carries certain risks that require further validation and enhancement. Overall, this strategy holds great innovative potential.

||

## Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1_open|0|Source: open|high|low|close|hl2|hlc3|hlcc4|ohlc4|
|v_input_2|13|Fast Length|
|v_input_3|19|Slow Length|
|v_input_4|13|Filter Length|
|v_input_5|6|Filter Smoothing|
|v_input_6|23|kNN nearest neighbors (k)|
|v_input_7|false|Draw background|

> Source (PineScript)

``` pinescript
/*backtest
start: 2023-11-21 00:00:00
end: 2023-12-21 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © lastguru

//@version=4
strategy(title="VWMA with kNN Machine Learning: MFI/ADX", shorttitle="VWMA + kNN: MFI/ADX", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=100)

/////////
// kNN //
/////////

// Define storage arrays for: parameter 1, parameter 2, price, result (up = 1; down = -1)
var knn1 = array.new_float(1, 0)
var knn2 = array.new_float(1, 0)
var knnp = array.new_float(1, 0)
var knnr = array.new_float(1, 0)

// Store the previous trade; buffer the current one until results are in
_knnStore (p1, p2, src) =>
    var prevp1 = 0.0
    var prevp2 = 0.0
    var prevsrc = 0.0
    
    array.push(knn1, prevp1)
    array.push(knn2, prevp2)
    array.push(knnp, prevsrc)
    array.push(knnr, src >= prevsrc ? 1 : -1)
```