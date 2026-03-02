> Name

Momentum-Moving-Average-Crossover-Trend-Following-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1e0f1941706a9f448c7.png)

### Overview

This strategy combines moving average crossovers and momentum indicators to effectively track and reverse trends. It first uses fast and slow moving averages to generate golden cross long signals and death cross short signals. Then with momentum indicators of certain parameters, if the momentum on the fast MA turns up again after a golden cross, it is considered as the trend continuing, maintaining the long position. When the momentum declines, it is considered as a trend reversal, triggering a close-out. The same logic applies to death cross short signals when tracking trend reversals. An ADX filter is also used to avoid wrong signals when not in trending states.

### Strategy Logic

The core logic of this strategy is based on trend signals from MA crossovers and trend reversal signals from momentum indicators. The key parts are:

1. Calculate fast MA `price1` (5-period HMA) and slow MA `price2` (7-period HMA).

2. A golden cross with `price1` crossing above `price2` generates a long signal. A death cross with `price1` crossing below `price2` generates a short signal. This is the common usage of MAs.

3. After a long signal, if `price1`'s momentum `roc1` turns up again, it is considered as the trend continuing and the long position will be maintained.

4. When momentum `roc1` declines, it is considered as a trend reversal, triggering a close-out. The same logic applies to short signals.

5. Introduce an ADX threshold to avoid wrong signals when not in trending states. Signals are generated only when ADX is above the threshold.

### Advantage Analysis

Compared to simple MA strategies, this strategy's biggest advantage lies in the introduction of momentum indicators to determine trend reversals more promptly and accurately. Specific advantages include:

1. MAs themselves lag price changes, while momentum indicators can quickly capture reversal signals for timely stop loss or reverse trading.
2. Reversal signals based on momentum are more reliable, avoiding unnecessary open/close orders during trend trading.
3. ADX avoids wrong signals in non-trending markets, keeping the strategy more focused on trends with higher winning odds.
4. The logic is simple and easy to understand, suitable for algo trading beginners.
5. Large optimization space by adjusting MA periods, momentum parameters, etc., for different markets.

### Risk Analysis

The main risks of this strategy come from:

1. The lagging nature of MAs, which may cause delayed signals, missing the best entry points.
2. False breakouts causing unnecessary entries or exits. Needs further optimization of parameters or additional filters.
3. Trend reversal detection relies on momentum, which may falter during huge market swings.
4. ADX is imperfect in detecting trends and consolidations. Improper threshold settings can cause issues.
5. No consideration of trading costs. Proper stop loss should be set when applied in real trading.

### Optimization Directions

The strategy can be further optimized in the following aspects:

1. Try other types of MAs or adjust MA parameters for better smoothing effects.
2. Optimize momentum indicator length for higher sensitivity to catch price reversals.
3. Set price filters when momentum reverses to avoid being misled by short-term fluctuations.
4. Enhance ADX usage by using different parameters at different ADX levels.
5. Introduce volume indicators, etc., to improve signal quality and filter false breakouts.
6. Add stop loss mechanisms to control single trade loss. Evaluate realistic trading costs to set proper profit targets and stop losses.

### Summary

This strategy integrates the advantages of MA and momentum indicators to track trends and capture reversals. Compared to pure trend-following strategies, it can be more flexible in dealing with different market stages, avoiding losses from trend climax while maintaining trend trading. Further improvements can be made through parameter optimization and introducing auxiliary conditions. Overall, this strategy has clear and simple logic, making it very suitable for algo trading beginners to learn and apply.

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1_open|0|Source: open|high|low|close|hl2|hlc3|hlcc4