<!-- AUTO-TRANSLATE FAILED: the JSON object must be str, bytes or bytearray, not NoneType -->


> Name

blackcat-L1-MartinGale-Scalping-Strategy

> Author

Zer3192

> Strategy Description

The Martingale strategy is a popular money management strategy commonly used in trading. It is typically employed by traders seeking recovery through increasing position size after each loss. Therefore, Martingale does not refer to a specific strategy but rather a general term for strategies involving adding to positions or doubling down.

In the Martingale strategy, traders double their position size after every losing trade. The purpose of this approach is to hope that eventually there will be a winning trade that recovers previous losses and generates profit.

The concept behind the Martingale strategy is based on the law of averages. By increasing position size after each loss, the strategy assumes that ultimately a profitable trade will occur which not only covers prior losses but also yields gains. This can be particularly attractive to traders looking for quick recovery from losses.

However, it's important to note that the Martingale strategy carries significant risks. If a trader experiences prolonged periods of losses or lacks sufficient capital, this strategy could lead to substantial losses. The strategy relies on the assumption that a profitable trade will happen within a certain timeframe, which is dangerous because there's no guarantee that a profitable trade will occur within any specified period.
Traders considering implementing the Martingale strategy should carefully evaluate their risk tolerance and fully understand potential drawbacks. Establishing a solid risk management plan to mitigate potential losses is crucial. Additionally, traders should realize that this strategy may not be suitable for all market conditions and might require adjustments according to market volatility.

In summary, the Martingale strategy is a money management method involving increasing position sizes after each loss in an attempt to recover from losing streaks. While it offers the potential for rapid recovery, it comes with significant risks that traders should carefully consider before employing such a trading approach.

Although I don't entirely agree with this trading philosophy, some private messages requested discussing this topic, so I wrote a simple framework around line 38 for short-term Martingale scalping.

Martingale scalp strategy is a trading strategy aimed at generating profits through frequent trades. It uses moving average crossovers to generate entry and exit signals. The strategy is implemented using TradingView’s Pine script language.

Firstly, the strategy defines input variables such as take-profit and stop-loss levels, along with trading modes (long-only, short-only, or bidirectional). Then, it sets up a rule allowing entries only when the trading mode is set to "long."

Strategy logic utilizes simple moving average (SMA) crossover and crossunder signals. It calculates short-term SMA (SMA3) and long-term SMA (SMA8), plotting them on the chart. Variables `crossoverSignal` and `crossunderSignal` track occurrences of crossover and crossunder events, while `crossoverState` and `crossunderState` determine the status of these conditions.

Execution of the strategy depends on current position size. When position size is zero (no open positions), the strategy checks for crossover/crossunder events. If a crossover occurs and long entries are allowed under the trading mode, it enters a long position. Entry price, stop price, take-profit price, and stop-loss price are calculated based on the current closing price and SMA8 value. Similarly, if a crossunder event occurs and short entries are permitted, it initiates a short position with corresponding price calculations.

If a long position exists and the current closing price reaches either take-profit or stop-loss level accompanied by a crossunder event, the long position is closed out, resetting entry price, stop price, take-profit price, and stop-loss price back to zero.

Likewise, if a short position exists and the current closing price hits either take-profit or stop-loss level accompanied by a crossover event, the short position is exited, resetting relevant prices accordingly.

Additionally, the strategy uses the `plotshape` function to plot entry and exit points on the chart. An upward-pointing triangle indicates buy entry; a downward-pointing triangle denotes sell exit; a downward-pointing triangle marks sell entry; and an upward-pointing triangle shows sell exit.

Overall, the Martingale scalp strategy aims to capture small profits by leveraging short-term moving average crosses. Risk management is achieved through predefined take-profit and stop-loss levels, and different trading modes accommodate various market conditions.

> Strategy Arguments



|Argument|Default|Description|
|----|----|----|
|v_input_1|1.03|Take Profit|
|v_input_2|0.95|Stop Loss|
|v_input_string_1|0|Trading Mode: Long|Short|BiDir|


> Source (PineScript)

``` pinescript
//@version=5
 strategy('[blackcat] L1 MartinGale Scalping Strategy', overlay=true, pyramiding = 5)
 
 // Define input variables
// martingaleMultiplier = input(2, title="加倍倍数")
 takeProfit = input(1.03, title='Take Profit')
 stopLoss = input(0.95, title='Stop Loss')
 inputTradingMode = input.string(defval='Long', options=['Long', 'Short', 'BiDir'], title='Trading Mode')
 
 //The purpose of this rule is to forbid short entries, only long etries will be placed. The rule affects the following function: 'entry'.
strategy.risk.allow_entry_in(inputTradingMode == 'Long' ? strategy.direction.long : inputTradingMode == 'Short' ? strategy.direction.short : strategy.direction.all)

// Define strategy logic 
entryPrice = 0.0
stopPrice = 0.0
takeProfitPrice = 0.0
stopLossPrice = 0.0

// Define SMA crossover and crossunder signals
sma3 = ta.sma(close, 3)
sma8 = ta.sma(close, 8)
plot(sma3, color=color.yellow)
plot(sma8, color=color.fuchsia)
crossoverSignal = ta.crossover(sma3, sma8)
crossunderSignal = ta.crossunder(sma3, sma8)
crossoverState = sma3 > sma8
crossunderState = sma3 < sma8

if strategy.position_size == 0
    if crossoverState
       strategy.entry('Buy',strategy.long)
       entryPrice := close
       stopPrice := close - stopLoss * sma8[1]
       takeProfitPrice := close + takeProfit * sma8[1]
       stopLossPrice := stopPrice
       stopLossPrice
    if crossunderState
        strategy.entry('Sell', strategy.short)
        entryPrice := close
        stopPrice := close + stopLoss *  sma8[1]
        takeProfitPrice := close - takeProfit *  sma8[1]
        stopLossPrice := stopPrice
        stopLossPrice

if strategy.position_size > 0
    if (close > takeProfitPrice or close < stopLossPrice) and crossunderState
        strategy.close('Buy')
        entryPrice := 0.0
        stopPrice := 0.0
        takeProfitPrice := 0.0
        stopLossPrice := 0.0
        stopLossPrice
    else
        strategy.entry('Buy', strategy.long)
        entryPrice := close
        stopPrice := close - stopLoss *  sma8[1]
        takeProfitPrice := close + takeProfit *  sma8[1]
        stopLossPrice := stopPrice
        stopLossPrice

if strategy.position_size < 0
    if (close > takeProfitPrice or close < stopLossPrice) and crossoverState
        strategy.close('Sell')
        entryPrice := 0.0
        stopPrice := 0.0
        takeProfitPrice := 0.0
        stopLossPrice := 0.0
        stopLossPrice
    else
        strategy.entry('Sell', strategy.short)
        entryPrice := close
        stopPrice := close + stopLoss *  sma8[1]
        takeProfitPrice := close - takeProfit *  sma8[1]
        stopLossPrice := stopPrice
        stopLossPrice

// Plot entry and exit points
plotshape(strategy.position_size > 0 and crossoverSignal, 'Buy Entry', shape.triangleup, location.belowbar, color.new(color.green, 0), size=size.small)
plotshape(strategy.position_size > 0 and (close >= takeProfitPrice or close <= stopLossPrice), 'Buy Exit', shape.triangledown, location.abovebar, color.new(color.red, 0), size=size.small)
plotshape(strategy.position_size < 0 and crossunderSignal, 'Sell Entry', shape.triangledown, location.abovebar, color.new(color.red, 0), size=size.small)
plotshape(strategy.position_size < 0 and (close >= takeProfitPrice or close <= stopLossPrice), 'Sell Exit', shape.triangleup, location.belowbar, color.new(color.green, 0), size=size.small)
```

> Detail

https://www.fmz.com/strategy/428756

> Last Modified

2023-11-03 17:27:45