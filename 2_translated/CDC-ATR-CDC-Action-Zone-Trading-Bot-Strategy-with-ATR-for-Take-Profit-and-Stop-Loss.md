> Name

CDC Action Zone Trading Bot Strategy with ATR for Take Profit and 5% Stop Loss

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/ca0a88661898c92098.png)

[trans]
#### Overview
This strategy is a trading bot strategy based on the CDC action zone. It uses the 12-period and 26-period Exponential Moving Averages (EMA) to determine market trends, going long when the short-term EMA is above the long-term EMA and going short when the opposite is true. The strategy employs Average True Range (ATR) to set dynamic take profit and stop loss levels. The take profit level is determined based on ATR and a multiplier, while the stop loss level is fixed at 5% of the current closing price.

#### Strategy Principles
1. Calculate the 12-period and 26-period EMAs to determine market trends.
2. Calculate ATR to set dynamic take profit and stop loss levels.
3. When the short-term EMA is above the long-term EMA, a buy signal is generated, and a long position is opened.
4. When the short-term EMA is below the long-term EMA, a sell signal is generated, and a short position is opened.
5. The take profit level is determined based on ATR and a multiplier, and the position is closed when the price reaches the take profit level.
6. The stop loss level is fixed at 5% of the current closing price, and the position is closed when the price reaches the stop loss level.

#### Strategy Advantages
1. Using EMAs to capture market trends can effectively adapt to different market conditions.
2. Employing ATR to set dynamic take profit levels can better protect profits.
3. Fixed stop loss levels help control risk and limit losses to an acceptable range.
4. The code structure is clear and easy to understand and modify, making it suitable for further optimization.

#### Strategy Risks
1. EMAs are lagging indicators and may generate false signals when the market changes rapidly.
2. ATR-based take profit levels may not protect profits in time during high market volatility.
3. Fixed stop loss levels may lead to premature position closures in some cases, missing out on potential profits.
4. The strategy does not consider trading costs and slippage, so actual trading results may differ from backtesting results.

#### Strategy Optimization Directions
1. Experiment with other trend indicators, such as MACD or moving average crossovers, to improve signal accuracy.
2. Optimize the ATR multiplier and take profit/stop loss percentages to better adapt to different market conditions.
3. Introduce dynamic stop loss mechanisms, such as trailing stops or volatility-based stops, to better control risk.
4. Consider trading costs and slippage, and choose appropriate trading instruments and trading sessions to improve the strategy's actual performance.

#### Summary
This strategy is an ATR-based take profit and stop loss trading bot strategy based on the CDC action zone. It uses EMAs to capture market trends, ATR to set dynamic take profit levels, and fixed percentage stop losses to control risk. Although the strategy has certain advantages, it still has some risks and room for improvement. With further optimization and testing, the strategy may achieve good performance in actual trading.

||

#### Overview
This strategy is a trading bot based on the CDC action zone. It uses 12-period and 26-period Exponential Moving Averages (EMA) to determine market trends, going long when the short-term EMA crosses above the long-term EMA and going short when the opposite occurs. The strategy employs Average True Range (ATR) to set dynamic take profit and stop loss levels. The take profit level is based on ATR and a multiplier, while the stop loss level is fixed at 5% of the current closing price.

#### Strategy Principles
1. Calculate the 12-period and 26-period EMAs to determine market trends.
2. Calculate ATR to set dynamic take profit and stop loss levels.
3. When the short-term EMA crosses above the long-term EMA, generate a buy signal and open a long position.
4. When the short-term EMA crosses below the long-term EMA, generate a sell signal and open a short position.
5. The take profit level is determined based on ATR and a multiplier, and the position is closed when the price reaches the take profit level.
6. The stop loss level is fixed at 5% of the current closing price, and the position is closed when the price reaches the stop loss level.

#### Strategy Advantages
1. Using EMAs to capture market trends can effectively adapt to different market conditions.
2. Employing ATR to set dynamic take profit levels can better protect profits.
3. Fixed stop loss levels help control risk and limit losses to an acceptable range.
4. The code structure is clear and easy to understand and modify, making it suitable for further optimization.

#### Strategy Risks
1. EMAs are lagging indicators and may generate false signals when the market changes rapidly.
2. ATR-based take profit levels may not protect profits in time during high market volatility.
3. Fixed stop loss levels may lead to premature position closures in some cases, missing out on potential profits.
4. The strategy does not consider trading costs and slippage, so actual trading results may differ from backtesting results.

#### Strategy Optimization Directions
1. Experiment with other trend indicators, such as MACD or moving average crossovers, to improve signal accuracy.
2. Optimize the ATR multiplier and take profit/stop loss percentages to better adapt to different market conditions.
3. Introduce dynamic stop loss mechanisms, such as trailing stops or volatility-based stops, to better control risk.
4. Consider trading costs and slippage, and choose appropriate trading instruments and trading sessions to improve the strategy's actual performance.

#### Summary
This strategy is an ATR-based take profit and stop loss trading bot based on the CDC action zone. It uses EMAs to capture market trends, ATR to set dynamic take profit levels, and fixed percentage stop losses to control risk. Although this strategy has certain advantages, it still faces some risks and can be improved through further optimization and testing. With better performance in actual trading, the strategy could perform well.

```pinescript
/*backtest
start: 2024-05-01 00:00:00
end: 2024-05-31 23:59:59
period: 1h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("CDC Action Zone Trading Bot with ATR for Take Profit and 5% Stop Loss", overlay=true)

// Get the closing price
close_price = close

// Calculate 12-period and 26-period EMAs
ema12 = ta.ema(close_price, 12)
ema26 = ta.ema(close_price, 26)

// Calculate ATR
atr_length = input.int(14, title="ATR Length")
atr = ta.atr(atr_length)

// Set the ATR Stoploss Multiplier
mult_atr_stoploss = input.float(2.5, title="ATR Stoploss Multiplier")

// Calculate ATR Trailing Stoploss
prev_stoploss = close_price
for i = 1 to 10
    prev_stoploss := math.max(prev_stoploss, high[i] - mult_atr_stoploss * atr)

// Set Take Profit as ATR Trailing Stoploss
takeProfitPercent = input.float(10, title="Take Profit (%)") / 100
takeProfit = close_price + (close_price - prev_stoploss) * takeProfitPercent

// Set Stop Loss to 5% of the current closing price
stopLossPercent = input.float(5, title="Stop Loss (%)") / 100
stopLoss = close_price * stopLossPercent

// Set the bar color
buyColor = input.color(color.green, title="Buy Color")
sellColor = input.color(color.red, title="Sell Color")
neutralColor = input.color(color.gray, title="Neutral Color")
color = if (ema12 > ema26)
    buyColor
else if (ema12 < ema26)
    sellColor
else
    neutralColor

// Generate Buy Signal
buySignal = color == buyColor and not na(color[1])

// Generate Sell Signal
sellSignal = color == sellColor and not na(color[1])

// Open Long Position
if (buySignal)
    strategy.entry("Long", strategy.long)

// Open Short Position
if (sellSignal)
    strategy.close("Long")  // Close the long position when a short signal is generated
```