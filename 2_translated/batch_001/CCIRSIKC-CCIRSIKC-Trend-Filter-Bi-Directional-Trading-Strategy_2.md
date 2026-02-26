> Name

CCIRSIKC Trend Filter Bi-Directional Trading Strategy - CCIRSIKC-Trend-Filter-Bi-Directional-Trading-Strategy

> Author

ChaoZhang

> Strategy Description

![IMG](https://www.fmz.com/upload/asset/1a9ea437fbea8fd3397.png)

[trans]
#### Overview
This strategy employs CCI, RSI, and Keltner Channels (KC) indicators alongside a trend filter to conduct bi-directional trading on AUDNZD and GBPNZD currency pairs. It uses CCI and RSI to identify overbought/oversold conditions, with KC serving as a reference for stop-loss and take-profit levels. A moving average is used as a trend filter to enter trades in line with the prevailing trend. The strategy has been backtested on historical data spanning the past five years, yielding stable returns.

#### Strategy Principles
1. Calculate CCI, RSI, and KC indicators. The upper KC line is the midline plus ATR, while the lower line is the midline minus ATR.
2. Select the moving average type (SMA, EMA, SMMA, CMA, or TMA) and trend filter method (OFF, Normal, or Reversed) based on input parameters.
3. Long entry conditions: Allow long trades, CCI < oversold line, close < KC lower line, RSI < oversold line, volume > 50-period average volume * multiplier, no current long position.
4. Short entry conditions: Allow short trades, CCI > overbought line, close > KC upper line, RSI > overbought line, volume > 50-period average volume * multiplier, no current short position.
5. Long exit condition: CCI > 0. Short exit condition: CCI < 0.
6. Send alerts when opening and closing positions.

#### Strategy Advantages
1. Combines multiple indicators for comprehensive analysis, improving signal accuracy.
2. Utilizes trend filter methods to adapt flexibly based on market trends.
3. Offers various moving average types that can be selected according to different market conditions.
4. Validated through long-term historical data, demonstrating good stability and suitability for long-term use.
5. Bi-directional trading allows adapting to various market conditions, providing more profit opportunities.
6. Highly automated with minimal manual intervention required.

#### Strategy Risks
1. Lacks traditional stop-loss and take-profit mechanisms; may experience significant drawdowns during extreme market conditions.
2. Frequent opening and closing of positions in volatile markets could increase trading costs.
3. Shorter CCI periods may generate noise signals.
4. Trend filters may be less effective when trends are unclear or market volatility increases.
5. Fixed position sizing does not adapt to changes in market volatility.

#### Strategy Optimization Directions
1. Consider adding trailing stops or fixed-point stop-losses to control single-trade risk.
2. Further optimize RSI and CCI parameters to reduce noise signals.
3. Introduce volatility indicators like ATR to adjust position sizing and stop-losses based on market volatility.
4. Add more currency pairs and optimize parameters separately for each instrument.
5. Explore the use of machine learning and other AI technologies for adaptive parameter optimization.

#### Summary
The strategy incorporates multiple classic indicators, making it relatively easy to code and backtest using TradingView. Although the backtesting results are promising, risk management and parameter adjustments remain crucial in live trading. It is recommended to start with a small initial investment for testing purposes and gradually increase capital as experience is gained. With its high degree of automation, this strategy suits conservative investors interested in long-term use.

||

#### Overview
This strategy combines CCI, RSI, and Keltner Channels (KC) indicators along with a trend filter to conduct bi-directional trading on AUDNZD and GBPNZD currency pairs. It uses CCI and RSI to determine overbought/oversold conditions, KC as a reference for stop-loss and take-profit levels, and a moving average as a trend filter to open positions in line with the prevailing trend. The strategy has been backtested on historical data spanning the past five years, achieving stable returns.

#### Strategy Principles
1. Calculate CCI, RSI, and KC indicators. The upper KC line is the midline plus ATR, while the lower line is the midline minus ATR.
2. Select the moving average type (SMA, EMA, SMMA, CMA, or TMA) and trend filter method (OFF, Normal, or Reversed) based on input parameters.
3. Long entry conditions: Allow long trades, CCI < oversold line, close < KC lower line, RSI < oversold line, volume > 50-period average volume * multiplier, no current long position.
4. Short entry conditions: Allow short trades, CCI > overbought line, close > KC upper line, RSI > overbought line, volume > 50-period average volume * multiplier, no current short position.
5. Long exit condition: CCI > 0. Short exit condition: CCI < 0.
6. Send alerts when opening and closing positions.

#### Strategy Advantages
1. Combines multiple indicators for comprehensive analysis, improving signal accuracy.
2. Utilizes trend filter methods to adapt flexibly based on market trends.
3. Offers various moving average types that can be selected according to different market conditions.
4. Validated through long-term historical data, demonstrating good stability and suitability for long-term use.
5. Bi-directional trading allows adapting to various market conditions, providing more profit opportunities.
6. Highly automated with minimal manual intervention required.

#### Strategy Risks
1. Lacks traditional stop-loss and take-profit mechanisms; may experience significant drawdowns during extreme market conditions.
2. Frequent opening and closing of positions in volatile markets could increase trading costs.
3. Shorter CCI periods may generate noise signals.
4. Trend filters may be less effective when trends are unclear or market volatility increases.
5. Fixed position sizing does not adapt to changes in market volatility.

#### Strategy Optimization Directions
1. Consider adding trailing stops or fixed-point stop-losses to control single-trade risk.
2. Further optimize RSI and CCI parameters to reduce noise signals.
3. Introduce volatility indicators like ATR to adjust position sizing and stop-losses based on market volatility.
4. Add more currency pairs and optimize parameters separately for each instrument.
5. Explore the use of machine learning and other AI technologies for adaptive parameter optimization.

#### Summary
The strategy employs multiple classic indicators and is relatively easy to code and backtest using TradingView. While the backtesting results are good, risk control and parameter adjustments remain necessary in live trading. It is recommended to start with a small initial investment for testing purposes and gradually increase capital as experience accumulates. With its high degree of automation, it is suitable for conservative investors interested in long-term use.

||

``` pinescript
/*backtest
start: 2024-04-01 00:00:00
end: 2024-04-30 23:59:59
period: 2h
basePeriod: 15m
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

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
rsi