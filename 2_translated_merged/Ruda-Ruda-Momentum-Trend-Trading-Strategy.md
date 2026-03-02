<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

Ruda Momentum Trend Trading Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/d56483cba8a45b2649.png)
[trans]
#### Overview
The Ruda Momentum Trend Trading Strategy is a quantitative trading strategy based on momentum and trend indicators. This strategy uses indicators such as OBV (On Balance Volume), EMA (Exponential Moving Average), and candlestick body ratio to determine entry and exit points. It enters a long position at the next day's opening price when the short-term EMA crosses above the long-term EMA, OBV hits a new high, and the candlestick body ratio exceeds the set threshold. The position is closed when the price drops below the stop-loss level or the closing price falls below the short-term EMA.

#### Strategy Logic
1. Calculate two EMA lines, with the short-term EMA parameter set to 5 and the long-term EMA parameter set to 21. When the short-term EMA crosses above the long-term EMA, it indicates an upward trend; conversely, it suggests a downward trend.
2. Calculate the OBV indicator. When OBV reaches a 10-day high, it signifies strong bullish momentum.
3. Calculate the candlestick body proportion. When the body proportion exceeds the set threshold (default 50%), it confirms the trend establishment.
4. When the trend is upward, bullish momentum is strong, and the trend is confirmed, the strategy buys at the next day's opening price, with the stop-loss set at the minimum of the current day's low and the opening price minus 1%.
5. The strategy exits the position when the price falls below the stop-loss level or the closing price drops below the short-term EMA.

#### Advantages Analysis
1. Combining trend and momentum indicators helps capture strong-performing assets.
2. Using the next day's opening price for entries and dynamic stop-loss helps avoid some false breakouts.
3. Clear stop-loss and take-profit conditions ensure controlled risk.

#### Risk Analysis
1. Trend and momentum indicators may exhibit lag, potentially leading to buying at highs and exiting too early.
2. Fixed parameters lack adaptability, causing varied performance across different market conditions.
3. Backtested on a single market and asset; further validation is needed for stability and applicability.

#### Optimization Directions
1. Optimize parameters of trend and momentum indicators to improve sensitivity and effectiveness.
2. Introduce market state detection to dynamically adjust parameters based on current market characteristics.
3. Expand backtesting scope to include various markets and assets to enhance strategy robustness.
4. Consider incorporating position management and risk control modules to improve the risk-return ratio.

#### Summary
The Ruda Momentum Trend Trading Strategy is a simple and user-friendly quantitative trading strategy that identifies strong assets and trend opportunities by combining trend and momentum indicators. However, it has certain limitations such as indicator lag and fixed parameters. Future improvements can focus on optimizing indicator parameters, introducing adaptive mechanisms, expanding backtesting scope, and enhancing risk management to boost the strategy's robustness and profitability.

|| 

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
|v_input_int_1|true|(?Backtest)Years |
|v_input_int_2|5|(?RUDA)Momentum |
|v_input_int_3|21|Trend |
|v_input_int_4|50|BODY |


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
strategy('Ruda_Strategy', overlay=true , initial_capital=5000 , pyramiding = 3, commission_type =  strategy.commission.cash_per_contract , commission_value =  1 )

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
//                 Operational Code                   //
//                                                    //
//                                                    //
////////////////////////////////////////////////////////
//
//
// Indicates Buy or Sell Conditions

// Condition True or False 
YEAR_BT= input.int(1,title="Years ", group = "Backtest")

INPUT_ME1 = input.int(5,title="Momentum ", group = "RUDA")
INPUT_ME2 = input.int(21,title="Trend ", group = "RUDA")
INPUT_CORPO = input.int(50,title="BODY ", group = "RUDA")/100



v_obv = ta.obv
v_med1 = ta.ema(close , INPUT_ME1)
v_med2 = ta.ema(close , INPUT_ME2)
valid_1 = v_med1 > v_med2 
valid_2 = v_obv >= ta.highest(v_obv[1], 10)
valid_3 = math.abs(close - open) / (high-low) > INPUT_CORPO
plot(v_med1)
plot(v_med2)

compra = valid_1 and valid_2 and  strategy.position_size == 0 and valid_3


var float v_minima_ref = na

dataInicio = timestamp(year(timenow) - YEAR_BT, month(timenow), dayofmonth(timenow), 00, 00)

// Global Variables
var float preco_entrada = na
var float preco_stop = na

if compra and time >= dataInicio and ta.change(time("D")) != 0 and ta.change(compra)  
    v_minima_ref := low
    preco_entrada := open
    preco_stop := math.min(low, open - 0.01 * open)
    strategy.entry("Compra", strategy.long , stop = preco_stop )
    if (not na(preco_entrada) and not na(preco_stop))
        label.new(x=bar_index, y= low * 0.9, text= "Day: " + str.tostring(dayofmonth) + "\nEntry Price: " + str.tostring(preco_entrada) + "\nStop Loss Price: " + str.tostring(preco_stop), style=label.style_label_up, color=color.green)

    
    
// Exit Logic
// Exit on Stop Loss
if (not na(preco_stop) and low < preco_stop and ta.change(low) < 0)
    strategy.close("Compra", comment="Exit on Stop")

// Exit on Profit
if (close < v_med1 and ta.change(close) < 0)
    strategy.close("Compra", comment="Exit on Average")

venda =( (not na(preco_stop) and low < preco_stop and ta.change(low) < 0) or (close < v_med1 and ta.change(close) < 0) ) and strategy.position_size > 0
codiff = compra ? 1 : venda ? -1 : na 
plotarrow(codiff, colorup=#00c3ff, colordown=#ff0062,title="Buy", maxheight=20, offset=0)





```

> Detail

https://www.fmz.com/strategy/446965

> Last Modified

2024-04-03 15:16:47