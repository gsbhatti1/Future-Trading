> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|14|Length|
|v_input_2|true|KSmoothing|
|v_input_3|3|DLength|
|v_input_4|50|Level|
|v_input_5|9|LengthCMO|
|v_input_6|70|TopBand|
|v_input_7|20|LowBand|
|v_input_8|false|Trade reverse|


> Source (PineScript)

``` pinescript
/*backtest
start: 2023-09-22 00:00:00
end: 2023-10-22 00:00:00
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
////////////////////////////////////////////////////////////
//  Copyright by HPotter v1.0 17/09/2019
// This is combo strategies for get a cumulative signal. 
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous close 
// during 2 days and the meaning of 9- 
```

## Overview

This strategy combines momentum indicator CMO and reversal indicator Stochastic to build a multi-factor model for discovering trading opportunities across different market environments.

## Logic Analysis

The strategy consists of two sub-strategies:

1. 123 Reversal Strategy

    - Use 9-day Stochastic to identify overbought and oversold levels
    
    - Go long if close price rises for 2 consecutive days and Stochastic is below 50
    
    - Go short if close price falls for 2 consecutive days and Stochastic is above 50
    
2. CMO Absolute Value Strategy

    - Calculate absolute value of CMO
    
    - CMO above 70 indicates overbought, go short
    
    - CMO below 20 indicates oversold, go long
    
Finally, a trade signal is generated when two sub-strategies agree.

The strategy makes full use of the strengths of momentum indicator CMO and reversal indicator Stochastic. CMO is good at trend identification while Stochastic is useful for catching short-term reversals. The combination enables the model to uncover opportunities across different market phases.

## Advantage Analysis

The strategy has the following advantages:

1. Multi-factor model adapts to different market environments

2. CMO has strong trend detection capability, Stochastic accurately locates reversal points

3. Only trade when two signals agree to avoid false signals and improve profitability

4. Large parameter tuning space allows optimization for different products and timeframes

5. Combining long and short term indicators discovers more opportunities

6. Simple and clear rules, easy to understand and automate, suitable for algo trading

## Risk Analysis

The strategy also has the following risks:

1. Probability of false signals from sub-strategies exists, parameters need optimization

2. Sudden trend reversal can lead to large losses

3. High trading frequency, transaction costs need consideration

4. Lagging nature of indicators leads to delay

5. Parameter tuning is challenging for different products

Solutions:

1. Optimize sub-strategy parameters to reduce false signals

2. Use stop loss to limit loss per trade 

3. Tune entry rules to lower trading frequency

4. Employ tick data to minimize lag

5. Apply machine learning for auto parameter tuning

## Optimization Directions

The strategy can be improved in the following aspects:

1. Introduce more factors like volatility and volume for a systematic multi-factor model

2. Build dynamic parameter optimization mechanism adapting to market regimes

3. Optimize entry logic using probability and exponential smoothing etc. 

4. Hedge long-term position with short-term trades to achieve dual targets

5. Extract more features with deep learning to build non-linear trading rules

6. Explore parameter-free models to avoid human biases 

7. Incorporate high frequency data and news events to reduce lag

## Conclusion

The strategy utilizes momentum indicator CMO and reversal indicator Stochastic to construct a multi-factor model for trading opportunities in trending and sideways markets. Compared to single-factor models, the multi-factor approach adapts better to complex market environments. Meanwhile, the large parameter tuning space and simple rules make it easy to optimize and automate, suitable for algo trading development. However, risk management is crucial, and high demand on parameter selection and model optimization is required. Overall, the momentum reversal combo strategy provides a systematic trading idea worthy of reference and exploration.

|||


``` pinescript
//@version=4
// Copyright by HPotter v1.0 17/09/2019
// This is combo strategies for get a cumulative signal. 
//
// First strategy
// This System was created from the Book "How I Tripled My Money In The 
// Futures Market" by Ulf Jensen, Page 183. This is reverse type of strategies.
// The strategy buys at market, if close price is higher than the previous close 
// during 2 days and the meaning of 9- 
```