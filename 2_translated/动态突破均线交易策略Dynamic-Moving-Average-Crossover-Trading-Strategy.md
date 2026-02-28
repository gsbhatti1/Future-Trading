> Name

Dynamic Moving Average Crossover Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/16cdd1d9c9b1713a667.png)
[trans]

## Overview

The key idea of this strategy is to build multiple moving averages based on the Ratio OCHL Averager indicator with different timeframes and generate trading signals based on the crossover. It can dynamically capture price trends, making it suitable for medium-term trading.

## Strategy Logic

The strategy uses two Ratio OCHL Averager indicators with different timeframes as the fast and slow lines. The Ratio OCHL Averager is calculated as:

```
b = abs(close-open)/(high - low)
c = min(max(b, 0), 1)  
Ratio OCHL Averager = c*close + (1-c)*previous Ratio OCHL Averager
```

Here, `b` represents the intraday price movement ratio and `c` is the normalized value of `b`. The Ratio OCHL Averager incorporates open, close, high, and low prices to build the moving average.

The strategy sets a shorter period for the fast line and a longer period for the slow line. A buy signal is generated when the fast line crosses above the slow line, and a sell signal when the fast line crosses below. It captures trends by using the moving average crossover logic.

## Advantages

1. The Ratio OCHL Averager smooths price data and filters out market noise, making trading signals more reliable.
2. Dual moving average crossovers combined with different timeframes can better detect the start of a new trend.
3. Parameters for the fast and slow lines can be adjusted to fit different market conditions.
4. The strategy logic is simple and intuitive, easy to understand and implement.
5. Stop loss and take profit levels can be flexibly set to control risks.

## Risks

1. Moving average crossover may generate excessive false signals; other technical indicators may be needed for filtration.
2. Proper selection of fast and slow line periods should be made; inappropriate parameter choices could affect strategy performance.
3. This is a trend-following strategy, not suitable for range-bound markets. It should be used in trending conditions.
4. Stop loss and take profit points need to be adjusted appropriately to reduce losses and optimize profits.

## Optimization Directions

1. Consider combining momentum indicators like MACD or KDJ for signal filtration and quality improvement.
2. Test different combinations of fast and slow line periods to find the optimal parameters.
3. Optimize stop loss and take profit based on backtest results.
4. Consider dynamically adjusting parameters in specific market conditions, such as increasing the period during range-bound markets.

## Conclusion

The strategy uses a clear logic of using fast and slow moving average crossovers to determine trend direction. It is a dynamic trend-following strategy suitable for medium-term trading. There is still significant room for optimization through parameter tuning and signal filtration methods. Overall, it is a flexible and practical trend trading strategy.

||


## Overview

The key idea of this strategy is to build multiple moving averages based on the Ratio OCHL Averager indicator with different timeframes and generate trading signals based on the crossover. It can dynamically capture price trends, making it suitable for medium-term trading.

## Strategy Logic

The strategy uses two Ratio OCHL Averager indicators with different timeframes as the fast and slow lines. The Ratio OCHL Averager is calculated as:

```
b = abs(close-open)/(high - low)
c = min(max(b, 0), 1)  
Ratio OCHL Averager = c*close + (1-c)*previous Ratio OCHL Averager
```

Here `b` represents the intraday price movement ratio and `c` is the normalized value of `b`. The Ratio OCHL Averager incorporates open, close, high, and low prices to build the moving average.

The strategy sets a shorter period for the fast line and a longer period for the slow line. A buy signal is generated when the fast line crosses above the slow line, and a sell signal when the fast line crosses below. It captures trends by using the moving average crossover logic.

## Advantages

1. The Ratio OCHL Averager smooths price data and filters out market noise, making trading signals more reliable.
2. Dual moving average crossovers combined with different timeframes can better detect the start of a new trend.
3. Parameters for the fast and slow lines can be adjusted to fit different market conditions.
4. The strategy logic is simple and intuitive, easy to understand and implement.
5. Stop loss and take profit levels can be flexibly set to control risks.

## Risks

1. Moving average crossover may generate excessive false signals; other technical indicators may be needed for filtration.
2. Proper selection of fast and slow line periods should be made; inappropriate parameter choices could affect strategy performance.
3. This is a trend-following strategy, not suitable for range-bound markets. It should be used in trending conditions.
4. Stop loss and take profit points need to be adjusted appropriately to reduce losses and optimize profits.

## Optimization Directions

1. Consider combining momentum indicators like MACD or KDJ for signal filtration and quality improvement.
2. Test different combinations of fast and slow line periods to find the optimal parameters.
3. Optimize stop loss and take profit based on backtest results.
4. Consider dynamically adjusting parameters in specific market conditions, such as increasing the period during range-bound markets.

## Conclusion

The strategy uses a clear logic of using fast and slow moving average crossovers to determine trend direction. It is a dynamic trend-following strategy suitable for medium-term trading. There is still significant room for optimization through parameter tuning and signal filtration methods. Overall, it is a flexible and practical trend trading strategy.

||


## Strategy Arguments

| Argument | Default | Description |
| --- | --- | --- |
| `v_input_1` | true | STRATEGY 1? —> |
| `v_input_2` | false | Recursive |
| `v_input_3` | 600 | Resolution Line 1 |
| `v_input_4` | 0 | Resolution Line 1: Min/D/W/M |
| `v_input_5` | 1440 | Resolution Line 2 |
| `v_input_6` | 0 | Resolution Line 2: Min/D/W/M |
| `v_input_7` | 500 | Stop Loss |
| `v_input_8` | 2500 | Take Profit |
| `v_input_9` | true | BACKTEST RANGE —|
| `v_input_10` | 2019 | From Year |
| `v_input_11` | true | From Month |
| `v_input_12` | 2 | From Day |
| `v_input_13` | 9999 | To Year |
| `v_input_14` | true | To Month |
| `v_input_15` | true | To Day |

## Source (PineScript)

```pinescript
//@version=4
strategy(title="[XC] Adaptive Strategy V3 - Ratio OCHL Averager no repaint", shorttitle="R_OHCL", overlay=true, currency=currency.EUR, initial_capital=10000,
    default_qty_value=100, default_qty_type=strategy.percent_of_equity , calc_on_every_tick=false, calc_on_order_fills=true)

//                  ╔═ SETTINGS                  ╗
//░░░░░░░░░░░░░░░░░ ╚════════════════════════════╝ ░░░░░░░░░░░░░░░░░░░░░░░░

strategy_1     = input ( defval=true   , type=input.bool    , title="STRATEGY 1? —>"      )
Recursive      = input(false)
RES201         = "Min", RES202= "D", RES203 = "W", RES204 = "M"

//++ Resolution 1 ++
inp_resolution1 = input(600, minval=1, title="Resolution Line 1")
restype1        = input ( defval="Min"  , type=input.string , title= "Resolution Line 1" , options=[ "Min","D","W","M"])
multiplier1     = restype1 == "Min" ? "" : restype1 == "D" ? "D" : restype1 == "W" ? "W" : "M"
resolution1     = tostring(inp_resolution1)+ multiplier1

//++ Resolution 2 ++
inp_resolution2 = input(1440, minval=1, title="Resolution Line 2")
restype2        = input ( defval="Min"  , type=input.string , title= "Resolution Line L