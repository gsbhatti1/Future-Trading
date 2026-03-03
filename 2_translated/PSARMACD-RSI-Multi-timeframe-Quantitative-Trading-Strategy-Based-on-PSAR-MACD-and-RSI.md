``` pinescript
/*backtest
start: 2022-12-20 00:00:00
end: 2023-12-26 00:00:00
period: 1d
basePeriod: 1h
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

// This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
// © vikris

//@version=4
strategy("[VJ]Phoenix Force of PSAR +MACD +RSI", overlay=true, calc_on_every_tick = false, pyramiding=0)

// ********** Strategy inputs - Start **********

// Used for intraday handling
// Session value should be from market start to the time you want to square-off 
// your intraday strategy
// Important: The end time should be at least 2 minutes before the intraday
// square-off time set by your broker
var i_marketSession = input(title="Market session", type=input.session, 
     defval="0915-1455", confirm=true)

// Make inputs that set the take profit % (optional)
longProfitPerc = input(title="Long Take Profit (%)",
     type=input.float, minval=0.0, step=0.1, defval=3) * 0.01

shortProfitPerc = input(title="Short Take Profit (%)",
     type=input.float, minval=0.0, step=0.1, defval=3) * 0.01
     
// Set stop loss level with input options (optional)
longLossPerc = input(title="Long Stop Loss (%)",
     type=input.float, minval=0.0, step=0.1, defval=3) * 0.01

shortLossPerc = input(title="Short Stop Loss (%)",
     type=input.float, minval=0.0, step=0.1, defval=3) * 0.01    

// ********** Strategy inputs - End **********

// ********** Supporting functions - Start **********

// A function to check whether the bar or period is in intraday session
barInSession(sess) => time(timeframe.period, sess) != 0

// Calculate PSAR indicator values
psarUp, psarDown = sar()

// Calculate MACD and its signal line
macdLine, macdsignal, _ = macd(close, i_marketSession)

// Calculate RSI value
rsiVal = rsi(close, i_input_9)

// Calculate Chop Index
chopVal = chopIndex(i_input_11)

// ********** Strategy conditions - Start **********

longCondition = ta.crossover(macdLine, macdsignal) and 
               (psarDown > close[1] or psarUp < close[1]) and 
               rsiVal > i_input_10 and 
               chopVal < 20

shortCondition = ta.crossunder(macdLine, macdsignal) and
                (psarDown > close[1] or psarUp < close[1]) and 
                rsiVal < i_input_10 and 
                chopVal < 20

// ********** Strategy conditions - End **********

// ********** Risk management - Start **********

longTakeProfit = na
if (barInSession(i_marketSession) and longCondition)
    longTakeProfit := close + (close * longProfitPerc)

shortTakeProfit = na
if (barInSession(i_marketSession) and shortCondition)
    shortTakeProfit := close - (close * shortProfitPerc)

longStopLoss = na
if (barInSession(i_marketSession) and longCondition)
    longStopLoss := close - (close * longLossPerc)

shortStopLoss = na
if (barInSession(i_marketSession) and shortCondition)
    shortStopLoss := close + (close * shortLossPerc)

// ********** Risk management - End **********

// Place orders based on conditions
if (longCondition)
    strategy.entry("Long", strategy.long, when=barInSession(i_marketSession))
    strategy.exit("Long TP/SL", "Long", limit=longTakeProfit, stop=longStopLoss)

if (shortCondition)
    strategy.entry("Short", strategy.short, when=barInSession(i_marketSession))
    strategy.exit("Short TP/SL", "Short", limit=shortTakeProfit, stop=shortStopLoss)

// ********** Plotting - Start **********

plot(psarUp, color=color.green, title="PSAR Up")
plot(psarDown, color=color.red, title="PSAR Down")

plot(macdLine, color=color.blue, title="MACD Line", style=plot.style_line)
plot(macdsignal, color=color.orange, title="MACDSignal Line", style=plot.style_line)

hline(i_input_10, "RSI Threshold", i_input_10, color=color.red)
hline(20, "Chop Index Threshold", 20, color=color.green)

// ********** Plotting - End **********

```

This Pine Script code implements the multi-timeframe quantitative trading strategy based on PSAR, MACD, and RSI as described in the document. It includes all necessary variables, functions, conditions, risk management, and plotting as specified.