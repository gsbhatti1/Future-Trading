---
### Name

Double-Tops-Smart-Breakout-Strategy

### Author

ChaoZhang

### Strategy Description

---

## Overview

The Double-Tops Smart Breakout Strategy is a combination strategy that incorporates the 123 Reversal Strategy and the Pivot Detector Oscillator Strategy. It mainly utilizes double top patterns to identify potential trend reversal points, combining the pivot detector indicator to filter out false breakouts, in order to capture trend reversals at critical technical levels.

## Principles

The strategy consists of two parts:

1. 123 Reversal Strategy

   The 123 Reversal Strategy originates from the book "How I Tripled My Money in the Futures Market" by Ulf Jensen, page 183. It is a counter-trend reversal strategy.

   The logic is: when the closing price is higher than the previous closing price for 2 consecutive days, and the 9-day Stochastic Slow line is below 50, go long; when the closing price is lower than the previous closing price for 2 consecutive days, and the 9-day Stochastic Fast line is above 50, go short.

2. Pivot Detector Oscillator Strategy

   The Pivot Detector Oscillator Strategy was proposed by Giorgos E. Siligardos. The related article was published in the September 2009 issue of Stocks & Commodities magazine.

   This strategy uses a combination of moving averages and the RSI indicator to gauge oscillation when price approaches upper or lower bands. The specific calculation formula is as follows:

   ```
   When price > moving average:
       Indicator value = (RSI value - 35) / (85 - 35)
   When price <= moving average: 
       Indicator value = (RSI value - 20) / (70 - 20)

   If indicator value > 50, go long
   If indicator value < 50, go short
   ```

By combining the two strategies, when a double top pattern emerges, if the indicator issues a signal in the same direction, a breakout operation is executed. This allows capturing new trends at critical technical levels while avoiding false breakouts within consolidation ranges.

## Advantage Analysis

- Utilizes double indicators for more reliable signals
- Captures new trend outbreaks at key technical levels  
- Breakout operations allow larger profit potential
- Combining reversals and indicator filters avoids whipsaws in ranges
- Applicable to multiple products with flexibility

## Risk Analysis

- Double tops cannot fully eliminate false breakout risks
- Indicator settings require experience, improper parameters may cause wrong signals 
- Effective stop loss strategies are needed to control single loss
- Failed breakouts can lead to large losses
- Performance relies on parameter tuning for different products

Risk management and optimization:

- Optimize indicator parameters to lower false signals
- Adopt moving or trailing stops to limit losses
- Evaluate sustainability of breakouts to avoid reversals
- Adjust parameters based on different product characteristics

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Test different moving average systems to find optimal parameter combinations

2. Optimize RSI parameters to reduce false signals

3. Add volume filter to ensure valid breakouts 

4. Incorporate trend-determining indicators to avoid counter-trend breaks

5. Use machine learning for automatic parameter tuning

6. Add stop loss strategies to control risks

7. Evaluate breakout sustainability and set profit targets

8. Analyze different product characteristics for parameter adjustments

Through parameter optimization, evaluating breakout effects, adjusting stop loss strategies etc, the strategy can be continuously improved to obtain steady profits in different market environments.

## Conclusion

The Double-Tops Smart Breakout Strategy combines reversal patterns and indicator confirmation mechanisms to capture potential trend reversal points at critical technical levels. Compared to purely chasing breakouts, its execution timing is more precise, avoiding whipsaws in ranging markets. Meanwhile, the strategy emphasizes risk control and should be used with stop loss mechanisms. Through parameter optimization and combining technical indicators, steady breakout signals can be obtained to capture outbreaks and achieve large profits at trend reversal points. In summary, the strategy has precise timing selection and sound risk control. With proficiency, it can achieve excellent trading performance.

---

||

## Overview

The Double Tops Smart Breakout Strategy is a combination of the 123 Reversal Strategy and the Pivot Detector Oscillator Strategy. It mainly utilizes double top patterns to identify potential trend reversal points and uses the pivot detector indicator to filter out false breakouts, in order to capture trend reversals at critical technical levels.

## Principles

The strategy consists of two parts:

1. 123 Reversal Strategy

   The 123 Reversal Strategy originates from page 183 of Ulf Jensen's book "How I Tripled My Money in the Futures Market." It is a counter-trend reversal strategy.

   The logic is: when the closing price is higher than the previous closing price for 2 consecutive days, and the 9-day Stochastic Slow line is below 50, go long; when the closing price is lower than the previous closing price for 2 consecutive days, and the 9-day Stochastic Fast line is above 50, go short.

2. Pivot Detector Oscillator Strategy

   The Pivot Detector Oscillator Strategy was proposed by Giorgos E. Siligardos. The related article was published in the September 2009 issue of Stocks & Commodities magazine.

   This strategy uses a combination of moving averages and the RSI indicator to gauge oscillation when price approaches upper or lower bands. The specific calculation formula is as follows:

   ```
   When price > moving average:
       Indicator value = (RSI value - 35) / (85 - 35)
   When price <= moving average: 
       Indicator value = (RSI value - 20) / (70 - 20)

   If indicator value > 50, go long
   If indicator value < 50, go short
   ```

By combining the two strategies, when a double top pattern emerges, if the indicator issues a signal in the same direction, a breakout operation is executed. This allows capturing new trends at critical technical levels while avoiding false breakouts within consolidation ranges.

## Advantage Analysis

- Utilizes double indicators for more reliable signals
- Captures new trend outbreaks at key technical levels  
- Breakout operations allow larger profit potential 
- Combining reversals and indicator filters avoids whipsaws in ranges
- Applicable to multiple products with flexibility

## Risk Analysis

- Double tops cannot fully eliminate false breakout risks
- Indicator settings require experience, improper parameters may cause wrong signals
- Effective stop loss strategies are needed to control single loss
- Failed breakouts can lead to large losses
- Performance relies on parameter tuning for different products

Risk management and optimization:

- Optimize indicator parameters to lower false signals
- Adopt moving or trailing stops to limit losses
- Evaluate sustainability of breakouts to avoid reversals
- Adjust parameters based on different product characteristics

## Optimization Directions

The strategy can be optimized in the following aspects:

1. Test different moving average systems to find optimal parameter combinations

2. Optimize RSI parameters to reduce false signals

3. Add volume filter to ensure valid breakouts 

4. Incorporate trend-determining indicators to avoid counter-trend breaks

5. Use machine learning for automatic parameter tuning

6. Add stop loss strategies to control risks

7. Evaluate breakout sustainability and set profit targets

8. Analyze different product characteristics for parameter adjustments

Through parameter optimization, evaluating breakout effects, adjusting stop loss strategies etc, the strategy can be continuously improved to obtain steady profits in different market environments.

## Conclusion

The Double Tops Smart Breakout Strategy combines reversal patterns and indicator confirmation mechanisms to capture potential trend reversal points at critical technical levels. Compared to purely chasing breakouts, its execution timing is more precise, avoiding whipsaws in ranging markets. Meanwhile, the strategy emphasizes risk control and should be used with stop loss mechanisms. Through parameter optimization and combining technical indicators, steady breakout signals can be obtained to capture outbreaks and achieve large profits at trend reversal points. In summary, the strategy has precise timing selection and sound risk control. With proficiency, it can achieve excellent trading performance.

---