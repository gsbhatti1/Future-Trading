> Name

Dual-Moving-Average-and-Williams-Average-Combination-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/118aa1ac0b1387b9c46.png)
#### Overview

This strategy combines dual exponential moving averages and three Williams moving averages to form a comprehensive trend tracking and trend reversal signal generation system. It has excellent holding efficiency and can effectively filter out false signals.

#### Strategy Logic

This strategy consists of two sub-strategies:

1. Dual Exponential Moving Average (DEMA). This indicator combines the trend tracking capability of single exponential moving averages and the lagging feature of double exponential moving averages. It can go long faster when prices rise and can flatten positions faster when prices fall.

2. Williams Three Moving Averages. This indicator consists of long, medium, and short lines. It uses the crossover of moving averages of different periods to determine trend changes and generate trading signals. When the short line crosses above the medium line and the medium line crosses above the long line, it is a long signal. When the short line crosses below the medium line and the medium line crosses below the long line, it is a short signal.

The trading signals of this strategy are the "AND" operation of the results of the two sub-strategies. That is, only when both sub-strategies issue signals at the same time, orders will be triggered for this strategy. This can effectively reduce false signals and improve the stability of holding positions.

#### Advantage Analysis

The biggest advantage of this strategy is that it can effectively filter out false signals, which is determined by its strategy structure. Although double moving averages and Williams moving averages have their own disadvantages, combining them together can give full play to their respective advantages and compensate for each other. This enables the strategy to achieve efficient holdings in trending markets and to stop losses in time during range-bound markets.

In addition, this strategy has large parameter optimization space. By adjusting the parameters of dual moving averages and Williams three moving averages, it can adapt to the characteristics of different varieties and cycles, and has strong adaptability.

#### Risk Analysis

The main risk of this strategy is that when the market enters violent fluctuations, the stop loss point may be broken, resulting in greater losses. This is a common problem with moving average strategies. In addition, in oscillating markets, this strategy may frequently open and close positions, increasing the cost of trading fees.

To control these risks, it is recommended to use the Walk Forward Analysis method for parameter optimization, and set reasonable stop loss points. At the same time, additional indicators can also be introduced to determine the market status and suspend trading during oscillating markets.

#### Optimization Directions

This strategy has the following optimization directions:

1. Adjust the parameters of dual moving averages to adapt to different varieties and cycles.
2. Adjust the cycles of the three Williams moving average lines to adapt to market volatility frequencies.
3. Increase opening conditions to filter trading signals during specific market stages. For example, do not trade during violent fluctuations.
4. Increase stop loss indicators to control losses. Methods like trailing stop loss and average stop loss can be tried.
5. Introduce machine learning algorithms to automatically optimize parameters.

#### Conclusion

This strategy realizes effective filtering of trading signals by combining the advantages of dual moving averages and Williams moving averages, which can reduce false signals and improve holding efficiency. It can obtain better performance through parameter optimization according to market conditions and has great application potential. At the same time, risk management is also required to control losses caused by drastic market fluctuations.

||

#### Overview

This strategy combines dual exponential moving averages and three Williams moving averages to form a comprehensive trend tracking and trend reversal signal generation system. It has excellent holding efficiency and can effectively filter out false signals.

#### Strategy Logic

This strategy consists of two sub-strategies:

1. Dual Exponential Moving Average (DEMA). This indicator combines the trend tracking capability of single exponential moving averages and the lagging feature of double exponential moving averages. It can go long faster when prices rise and can flatten positions faster when prices fall.

2. Williams Three Moving Averages. This indicator consists of long, medium, and short lines. It uses the crossover of moving averages of different periods to determine trend changes and generate trading signals. When the short line crosses above the medium line and the medium line crosses above the long line, it is a long signal. When the short line crosses below the medium line and the medium line crosses below the long line, it is a short signal.

The trading signals of this strategy are the "AND" operation of the results of the two sub-strategies. That is, only when both sub-strategies issue signals at the same time, orders will be triggered for this strategy. This can effectively reduce false signals and improve the stability of holding positions.

#### Advantage Analysis

The biggest advantage of this strategy is that it can effectively filter out false signals, which is determined by its strategy structure. Although double moving averages and Williams moving averages have their own disadvantages, combining them together can give full play to their respective advantages and compensate for each other. This enables the strategy to achieve efficient holdings in trending markets and to stop losses in time during range-bound markets.

In addition, this strategy has large parameter optimization space. By adjusting the parameters of dual moving averages and Williams three moving averages, it can adapt to the characteristics of different varieties and cycles, and has strong adaptability.

#### Risk Analysis

The main risk of this strategy is that when the market enters violent fluctuations, the stop loss point may be broken, resulting in greater losses. This is a common problem with moving average strategies. In addition, in oscillating markets, this strategy may frequently open and close positions, increasing the cost of trading fees.

To control these risks, it is recommended to use the Walk Forward Analysis method for parameter optimization, and set reasonable stop loss points. At the same time, additional indicators can also be introduced to determine the market status and suspend trading during oscillating markets.

#### Optimization Directions

This strategy has the following optimization directions:

1. Adjust the parameters of dual moving averages to adapt to different varieties and cycles.
2. Adjust the cycles of the three Williams moving average lines to adapt to market volatility frequencies.
3. Increase opening conditions to filter trading signals during specific market stages. For example, do not trade during violent fluctuations.
4. Increase stop loss indicators to control losses. Methods like trailing stop loss and average stop loss can be tried.
5. Introduce machine learning algorithms to automatically optimize parameters.

#### Conclusion

This strategy realizes effective filtering of trading signals by combining the advantages of dual moving averages and Williams moving averages, which can reduce false signals and improve holding efficiency. It can obtain better performance through parameter optimization according to market conditions and has great application potential. At the same time, risk management is also required to control losses caused by drastic market fluctuations.

---

> Strategy Arguments

|Argument|Default|Description|
|----|----|----|
|v_input_int_1|14|(?●═════ 2/20 EMA ═════●)Length|
|v_input_int_2|13|(?●═════ 3Lines ═════●)LLength|
|v_input_int_3|8|MLength|
|v_input_int_4|5|SLength|
|v_input_int_5|8|LOffset|
|v_input_int_6|5|MOffset|
|v_input_int_7|3|SOffset|
|v_input_bool_1|false|(?●═════ MISC ═════●)Trade reverse|
|v_input_int_8|true|(?●═════ Time Start ═════●)From Day|
|v_input_int_9|true|From Month|
|v_input_int_10|2005|From Year|

> Source (PineScript)

```pinescript
/*backtest
start: 2023-12-01 00:00:00
end: 2023-12-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_