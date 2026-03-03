> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|true|Long|
|v_input_2|true|Short|
|v_input_3|true|leverage|
|v_input_4|20|BB Length|
|v_input_5|2.0|KC Multiplier|
|v_input_6|10|Establishment Trend MA Length|
|v_input_7|100|Stop Loss Level|
|v_input_8|true|Include Volume|
|v_input_9|false|Use ADX|
|v_input_10|20|ADX Length|

## Summary

The main idea of this strategy is to use Bollinger Bands, KC channels, and candlestick colors to determine market squeezes and releases. It also uses the establishment trend based on moving averages to make trading decisions at trend reversals.

By combining multiple indicators such as KDJ, MACD, and volume, the strategy aims to improve the accuracy of signal generation. Adjusting parameters for Bollinger Bands, KC channels, and establishment trends can help optimize performance. Multi-timeframe analysis helps in differentiating between long-term and short-term signals.

The strategy also includes an AI optimization approach to find the best parameter combinations and reduce overfitting. Overall, it focuses on capturing market dynamics by identifying key points where energy is stored or released.

## Strategy Arguments

|Argument          | Default Value  | Description                                                                                                                                                                                                 |
|------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `v_input_1`      | true          | Whether to enter a long position.                                                                                                                                                                             |
| `v_input_2`      | true          | Whether to enter a short position.                                                                                                                                                                            |
| `v_input_3`      | true          | Leverage ratio, default is 1 (no leverage).                                                                                                                                                                  |
| `v_input_4`      | 20            | Bollinger Bands length.                                                                                                                                                                                       |
| `v_input_5`      | 2.0           | KC channel multiplier.                                                                                                                                                                                        |
| `v_input_6`      | 10            | Establishment trend moving average length.                                                                                                                                                                     |
| `v_input_7`      | 100           | Stop loss level, the price will be closed when it touches this level to limit risk.                                                                                                                            |
| `v_input_8`      | true          | Whether to include trading volume in analysis.                                                                                                                                                                |
| `v_input_9`      | false         | Whether to use ADX as an additional indicator.                                                                                                                                                                 |
| `v_input_10`     | 20            | ADX length if used, otherwise ignored.                                                                                                                                                                        |

This setup allows for flexibility and adaptability in various market conditions, enhancing the robustness of the trading strategy.