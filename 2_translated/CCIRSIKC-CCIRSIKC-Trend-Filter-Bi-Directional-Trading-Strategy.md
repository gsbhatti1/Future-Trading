> Name

CCIRSIKC Trend Filter Bi-Directional Trading Strategy - CCIRSIKC-Trend-Filter-Bi-Directional-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1a9ea437fbea8fd3397.png)

#### Overview
This strategy employs CCI, RSI, and Keltner Channels (KC) indicators, combined with a trend filter to achieve bi-directional trading on AUDNZD and GBPNZD currency pairs. It uses CCI and RSI to determine overbought and oversold conditions, KC as a reference for stop-loss and take-profit, and a moving average as a trend filter to open positions in line with the trend. The strategy has been backtested on historical data over the past 5 years, achieving stable returns.

#### Strategy Principles
1. Calculate CCI, RSI, and KC indicators. The upper KC line is the midline plus ATR, and the lower line is the midline minus ATR.
2. Select the moving average type (SMA, EMA, SMMA, CMA, or TMA) and trend filter method (OFF, Normal, or Reversed) based on input parameters.
3. Long entry conditions: allow long, CCI < oversold line, close < KC lower line, RSI < oversold line, volume > 50-period average volume * multiplier, no current long position.
4. Short entry conditions: allow short, CCI > overbought line, close > KC upper line, RSI > overbought line, volume > 50-period average volume * multiplier, no current short position.
5. Long exit condition: CCI > 0. Short exit condition: CCI < 0.
6. Send alerts when opening and closing positions.

#### Strategy Advantages
1. Combines multiple indicators for comprehensive analysis, improving signal accuracy.
2. Uses trend filter methods, allowing flexible adjustments based on market trends.
3. Offers multiple moving average types, adapting to different market characteristics.
4. Validated through long-term historical data, demonstrating good stability and suitability for long-term use.
5. Bi-directional trading, suitable for various market conditions, providing more profit opportunities.
6. Highly automated, requiring no manual intervention, saving time and effort.

#### Strategy Risks
1. Lacks traditional stop-loss and take-profit, potentially leading to significant drawdowns in extreme market conditions.
2. May experience frequent opening and closing of positions in choppy markets, increasing trading costs.
3. Uses relatively short CCI periods, potentially generating noise signals.
4. Trend filters may have limited effectiveness when trends are unclear or market volatility increases.
5. Fixed position sizing, unable to adapt to changes in market volatility.

#### Strategy Optimization Directions
1. Consider adding trailing stops or fixed-point stop-losses to control single-trade risk.
2. Further optimize RSI and CCI parameters to reduce noise signals.
3. Consider introducing volatility indicators like ATR to adjust position sizing and stop-losses based on market volatility.
4. Add more currency pairs and optimize parameters individually based on each instrument's characteristics.
5. Attempt to introduce machine learning and other AI technologies for adaptive parameter optimization.

#### Summary
This strategy employs multiple classic indicators, making it relatively easy to code and backtest on TradingView. While the backtesting results are good, risk control and parameter adjustments are still necessary for live trading. It is recommended to start with small funds for testing and gradually increase investment as experience accumulates. With a high degree of automation, it is suitable for conservative investors to use over the long term.

|| 

#### Overview
This strategy combines CCI, RSI, and Keltner Channels (KC) indicators along with a trend filter to achieve bi-directional trading on AUDNZD and GBPNZD currency pairs. It uses CCI and RSI to determine overbought and oversold conditions, KC as a reference for stop-loss and take-profit, and a moving average as a trend filter to open positions in line with the trend. The strategy has been backtested on historical data over the past 5 years, achieving stable returns.

#### Strategy Principles
1. Calculate CCI, RSI, and KC indicators. The upper KC line is the midline plus ATR, and the lower line is the midline minus ATR.
2. Select the moving average type (SMA, EMA, SMMA, CMA, or TMA) and trend filter method (OFF, Normal, or Reversed) based on input parameters.
3. Long entry conditions: allow long, CCI < oversold line, close < KC lower line, RSI < oversold line, volume > 50-period average volume * multiplier, no current long position.
4. Short entry conditions: allow short, CCI > overbought line, close > KC upper line, RSI > overbought line, volume > 50-period average volume * multiplier, no current short position.
5. Long exit condition: CCI > 0. Short exit condition: CCI < 0.
6. Send alerts when opening and closing positions.

#### Strategy Advantages
1. Combines multiple indicators for comprehensive analysis, improving signal accuracy.
2. Uses trend filter methods, allowing flexible adjustments based on market trends.
3. Offers multiple moving average types, adapting to different market characteristics.
4. Validated through long-term historical data, demonstrating good stability and suitability for long-term use.
5. Bi-directional trading, suitable for various market conditions, providing more profit opportunities.
6. Highly automated, requiring no manual intervention, saving time and effort.

#### Strategy Risks
1. Lacks traditional stop-loss and take-profit, potentially leading to significant drawdowns in extreme market conditions.
2. May experience frequent opening and closing of positions in choppy markets, increasing trading costs.
3. Uses relatively short CCI periods, potentially generating noise signals.
4. Trend filters may have limited effectiveness when trends are unclear or market volatility increases.
5. Fixed position sizing, unable to adapt to changes in market volatility.

#### Strategy Optimization Directions
1. Consider adding trailing stops or fixed-point stop-losses to control single-trade risk.
2. Further optimize RSI and CCI parameters to reduce noise signals.
3. Consider introducing volatility indicators like ATR to adjust position sizing and stop-losses based on market volatility.
4. Add more currency pairs and optimize parameters individually based on each instrument's characteristics.
5. Attempt to introduce machine learning and other AI technologies for adaptive parameter optimization.

#### Summary
This strategy employs multiple classic indicators, making it relatively easy to code and backtest on TradingView. While the backtesting results are good, risk control and parameter adjustments are still necessary for live trading. It is recommended to start with small funds for testing and gradually increase investment as experience accumulates. With a high degree of automation, it is suitable for conservative investors to use over the long term.

```pinescript
//@version=5
strategy('CCI Strategy with Trend Filter AUDNZD, GBPNZD', overlay=true, default_qty_type=strategy.cash, default_qty_value=50000, commission_value=0.0005, slippage=2, initial_capital=10000)

// State variables to ensure one entry per signal
var bool isLongOpen = false
var bool isShortOpen = false

// Input Parameters for allowing long and short trades
allowLong = input(true, title='Allow Long Trades')
allowShort = input(true, title='Allow Short Trades')

// Trend Filter Inputs
maType = input.string(title='MA Type', options=['OFF', 'SMA', 'EMA', 'SMMA', 'CMA', 'TMA'], defval='OFF')
trendFilterMethod = input.string(title='Trend Filter Method', options=['OFF', 'Normal', 'Reversed'], defval='OFF')
maLength = input(14, title='MA Length')

// Other Input Parameters
lengthKC = input(30, title='Keltner Channels Length')
multKC = input(0.7, title='Keltner Channels Multiplier')
lengthCCI = input(5, title='CCI Length')
overboughtCCI = input(75, title='CCI Overbought Level')
oversoldCCI = input(-75, title='CCI Oversold Level')
rsiPeriod = input(30, title='RSI Period')
```