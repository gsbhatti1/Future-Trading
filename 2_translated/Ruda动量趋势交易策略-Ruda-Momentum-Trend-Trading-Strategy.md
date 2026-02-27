> Name

Ruda Momentum Trend Trading Strategy - Ruda-Momentum-Trend-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/d56483cba8a45b2649.png)
[trans]
#### Overview
The Ruda Momentum Trend Trading Strategy is a quantitative trading strategy based on momentum and trend indicators. The strategy uses indicators such as OBV (On Balance Volume), EMA (Exponential Moving Average), and candlestick body ratio to determine buy and sell signals. When the short-term EMA crosses above the long-term EMA, OBV reaches a new high, and the candlestick body ratio is greater than the set threshold, the strategy buys at the next day's opening price; when the price falls below the stop-loss price or the closing price falls below the short-term EMA, the strategy closes the position.

#### Strategy Principle
1. Calculate two EMA lines with parameters of 5 for the short-term EMA and 21 for the long-term EMA. When the short-term EMA crosses above the long-term EMA, the trend is considered upward, and vice versa.
2. Calculate the OBV indicator. When OBV reaches a 10-day high, the bullish momentum is considered strong.
3. Calculate the candlestick body ratio. When the body ratio is greater than the set threshold (default 50%), the trend is considered established.
4. When the trend is upward, bullish momentum is strong, and the trend is established, the strategy buys at the next day's opening price with a stop-loss price set at the minimum of the current day's low and the opening price minus 1%.
5. When the price falls below the stop-loss price or the closing price falls below the short-term EMA, the strategy closes the position.

#### Advantage Analysis
1. By combining trend and momentum indicators, the strategy can capture strong instruments.
2. Using the next day's opening price for buying and dynamic stop-loss can avoid some false breakouts.
3. The stop-loss and take-profit conditions are clear, and the risk is controllable.

#### Risk Analysis
1. Trend and momentum indicators have a lag, which may lead to buying at high prices and premature stop-losses.
2. Fixed parameters lack adaptability, and performance may vary significantly under different market conditions.
3. Backtesting on a single market and instrument requires further verification of the strategy's stability and applicability.

#### Optimization Direction
1. Optimize the parameters of trend and momentum indicators to improve indicator sensitivity and effectiveness.
2. Introduce market state judgment and dynamically adjust parameters according to current market characteristics.
3. Expand the backtesting scope, increase testing on different markets and instruments to improve strategy robustness.
4. Consider introducing position management and risk control modules to improve the risk-reward ratio.

#### Summary
The Ruda Momentum Trend Trading Strategy is a simple and easy-to-use quantitative trading strategy that captures strong instruments and trend opportunities by combining trend and momentum indicators. However, the strategy also has certain limitations, such as indicator lag and fixed parameters. In the future, the strategy can be optimized and improved by optimizing indicator parameters, introducing adaptive mechanisms, expanding the backtesting scope, and strengthening risk management to enhance the strategy's robustness and profitability.
[/trans]

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_int_1|true|(?Backtest) Nº Anos |
|v_input_int_2|5|(?RUDA) Momentum |
|v_input_int_3|21|Trend |
|v_input_int_4|50|CORPO |


> Source (PineScript)

``` pinescript
/*backtest
start: 2024-03-01 00:00:00
end: 2024-03-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © lhcbenac

//@version=5
strategy('Ruda_Strategy', overlay=true , initial_capital=5000 , pyramiding = 3, commission_type = strategy.commission.cash_per_contract , commission_value = 1 )

//
// 
////////////////////////////////////////////////////////
//                                                    //
//                                                    //
//                    Optimizations                   //
//                                                    //
//                                                    //
////////////////////////////////////////////////////////
//
// 

////////////////////////////////////////////////////////
//                                                    //
//                                                    //
//                Operational Code                   //
//                                                    //
//                                                    //
////////////////////////////////////////////////////////
//
//
// Indicates Buy or Sell situation

// True or False condition
YEAR_BT = input.int(1, title="Nº Anos"