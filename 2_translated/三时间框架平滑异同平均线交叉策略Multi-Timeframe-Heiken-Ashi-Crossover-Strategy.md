> Name

Multi-Timeframe-Heiken-Ashi-Crossover-Strategy

> Author

ChaoZhang

> Strategy Description


```markdown
## Overview

This strategy is based on the smoothed convergence and divergence average indicators of three time periods. When the indicators of different periods are bullish or bearish in the same direction, a trading signal is generated. The purpose is to use multiple time frames to confirm trends and reduce the probability of false signals.

## Principle

The Heiken Ashi indicator is different from ordinary K-lines. Its calculation method can smooth the price curve and identify trends more accurately.

This strategy uses the smoothed convergence and divergence average indicators of three time periods: daily, weekly, and monthly. When the three are bullish in the same direction, that is, when all time periods have green fire candle lines, a buy signal is generated; when they are bearish in the same direction, that is, when all are red, a sell signal is generated.

After entering the market, as long as the smoothed convergence and divergence average line turns in any time period, a closing signal will be generated.
```

## Advantages

1. Multi-time frame verification can reduce false signals and enhance stability.
2. The smoothed average convergence and divergence indicator can identify trends and reduce noise.
3. The rules are simple, clear, and easy to implement.
4. The time period combination can be flexibly selected to adapt to different varieties.
5. No parameter optimization, extremely easy to operate.

## Risks and Solutions

1. Due to multiple restrictions, trading opportunities may be missed. Conditional restrictions can be reduced.
2. The lag problem of the smoothed average convergence and divergence still exists, which may delay the signal. Can be combined with other indicators for optimization.
3. Without a stop loss, the risk cannot be controlled. A trailing stop loss strategy can be added.
4. The profit and loss ratio is fixed and lacks flexibility. Dynamic stop-profit and stop-loss can be set.
5. Based only on indicators, it is easy to produce false signals. A volume and price confirmation mechanism can be added.

## Optimization Ideas

1. Test by adding more time frames, such as 15 minutes or 60 minutes.
2. Optimize the parameters of the smoothed average line of similarity and difference to improve sensitivity.
3. Add a trailing stop loss strategy to control risks.
4. Research on adding market structure indicators to avoid the shock range.
5. Add new re-entry conditions and extend the holding period.

## Summary

This strategy takes advantage of the multi-time period smoothed average convergence and divergence indicators to achieve trend tracking, but it is easy to generate false signals based only on indicators. It can be improved by adding more indicators, stop loss strategies, optimization parameters, etc., to make the strategy more reliable. Overall, the multi-time frame verification idea is worth learning from.
```


> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|D|TM 1|
|v_input_2|W|TM 2|
|v_input_3|M|TM 3|
|v_input_4|true|longA|
|v_input_5|false|shortA|


> Source (PineScript)

```pinescript
//@version=4
strategy("Heiken Ashi MTF Strategy")
ha_t = heikinashi(syminfo.tickerid)

res = input('D', title="TM 1")
ha_open = security(ha_t, res, open)
ha_close = security(ha_t, res, close)
ha_dif = ha_open-ha_close
ha_diff=iff(ha_dif > 0, 1, iff(ha_dif<0, 2, 3))

res2 = input('W', title="TM 2")
ha_open2 = security(ha_t, res2, open)
ha_close2 = security(ha_t, res2, close)
ha_dif2 = ha_open2-ha_close2
ha_diff2=iff(ha_dif2 > 0, 1, iff(ha_dif2<0, 2, 3))

res3 = input('M', title="TM 3")
ha_open3 = security(ha_t, res3, open)
ha_close3 = security(ha_t, res3, close)
ha_dif3 = ha_open3-ha_close3
ha_diff3=iff(ha_dif3 > 0, 1, iff(ha_dif3<0