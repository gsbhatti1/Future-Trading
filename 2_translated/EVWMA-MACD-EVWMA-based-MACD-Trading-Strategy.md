---

### Overview

This strategy is a MACD trading strategy based on Elastic Volume Weighted Moving Average (EVWMA). It leverages the advantages of EVWMA to design a strategy with clear and practical trading signals.

### Principles

The EVWMA indicator incorporates volume information into the calculation of moving averages, enabling moving averages to more accurately reflect price changes. The calculations for both the fast line and slow line in this strategy are based on EVWMA. The parameters of the fast line are set to be more sensitive, capturing short-term price fluctuations; while the parameters of the slow line are set to be more robust, filtering out some noise. The MACD formed by these two EVWMAs triggers long and short positions upon crossover, with the histogram providing visually enhanced trading signals.

### Advantage Analysis

The main advantage of this strategy is that it leverages the power of the EVWMA indicator to make the parameters of the MACD more stable and the trading signals clearer. Compared to simple moving averages, EVWMA better grasps market trend changes. This makes the strategy more adaptable, ensuring it works stably in various market environments.

### Risk Analysis

The main risk of this strategy lies in the inherent lag of MACD, which cannot promptly capture price reversals. Additionally, improper parameter settings for EVWMA can also affect the performance of the strategy. If the fast and slow line parameters are set incorrectly, it may lead to chaotic trading signals, impacting profitability.

To mitigate risks, parameters should be adjusted appropriately to maintain a moderate difference between the fast and slow lines. The histogram can assist in determining whether parameter adjustments are necessary. Additionally, stop-loss strategies can also be designed to prevent excessive single losses.

### Optimization Directions

This strategy can be optimized from the following aspects:

1. Use adaptive parameter setting techniques to automatically adjust EVWMA parameters based on market conditions, ensuring clear trading signals.
2. Introduce stop-loss mechanisms to effectively control single losses.
3. Incorporate other indicators to filter out false signals, such as combining with volume for significant price changes.
4. Optimize entry points by testing whether using divergence performs better.

### Conclusion

This strategy utilizes the advantages of the EVWMA indicator to build a simple and practical MACD strategy. It offers better stability and adaptability. However, it also has the inherent lag issue in MACD. We can improve its robustness through adaptive parameter optimization, stop-loss design, signal filtering, and other aspects.

---

### Strategy Arguments


|Argument|Default|Description|
|----|----|----|
|v_input_1|10|Fast Sum Length|
|v_input_2|20|Slow Sum Length|
|v_input_3|9|Signal Smoothing|


### Source (PineScript)

```pinescript
/*backtest
start: 2023-01-15 00:00:00
end: 2024-01-21 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=4
strategy("QuantNomad - EVWMA MACD Strategy", shorttitle = "EVWMA MACD", overlay = false)

// Inputs
fast_sum_length = input(10, title = "Fast Sum Length",  type = input.integer)
slow_sum_length = input(20, title = "Slow Sum Length",  type = input.integer)
signal_length   = input(9,  title = "Signal Smoothing", type = input.integer, minval = 1, maxval = 50)

// Calculate Volume Period
fast_vol_period = sum(volume, fast_sum_length)
slow_vol_period = sum(volume, slow_sum_length)

// Calculate EVWMA
fast_evwma = 0.0
fast_evwma := ((fast_vol_period - volume) * nz(fast_evwma[1], close) + volume * close) / (fast_vol_period)

// Calculate EVWMA
slow_evwma = 0.0
slow_evwma := ((slow_vol_period - volume) * nz(slow_evwma[1], close) + volume * close) / (slow_vol_period)

// Calculate MACD
macd   = fast_evwma - slow_evwma
signal = ema(macd, signal_length)
hist   = macd - signal

// Plot 
plot(hist,   title = "Histogram", style = plot.style_columns, color=(hist>=0 ? (hist[1] < hist ? #26A69A : #B2DFDB) : (hist[1] < hist ? #FFCDD2 : #EF5350) ), transp=0 )
plot(macd,   title = "MACD",      color = #0094ff, transp=0)
plot(signal, title = "Signal",    color = #ff6a00, transp=0)

// Strategy
strategy.entry("Long",   true, when = crossover(fast_evwma, slow_evwma))
strategy.entry("Short", false, when = crossunder(fast_evwma, slow_evwma))
```

### Detail

https://www.fmz.com/strategy/439609

### Last Modified

2024-01-22 10:50:25