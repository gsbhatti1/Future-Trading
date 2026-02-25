> Source (PineScript)

``` pinescript
/*backtest
start: 2019-12-23 08:00:00
end: 2024-11-27 08:00:00
period: 2d
basePeriod: 2d
exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]
*/

//@version=5
strategy("RSI BUY/SELL + EMA + SLTP by rcpislr", overlay=true)

// User Parameters
rsi_period = input(14, title="RSI Period")
rsi_overbought = input(70, title="RSI Overbought Level")
rsi_oversold = input(30, title="RSI Oversold Level")
ema_period = input(400, title="EMA Period")
use_ema = input(true, title="Use EMA Condition")
sl_pct = input(1, title="Stop-Loss (%)") / 100
tp_pct = input(1, title="Take-Profit (%)") / 100

// Calculations for RSI and EMA in the specified time frame
rsi = ta.rsi(close, rsi_period)
ema = ta.ema(close, ema_period)

// Long and Short Signals
long_signal = rsi[2] > rsi_overbought and rsi < rsi_overbought  and (close > ema or not use_ema)
short_signal = rsi[2] < rsi_oversold and rsi > rsi_oversold and (close < ema or not use_ema)

// Trading Actions
if long_signal
    strategy.entry("Long", strategy.long)

if short_signal
    strategy.entry("Short", strategy.short)

// Stop-Loss and Take-Profit Implementation
if strategy.position_size > 0
    long_stop_loss = close * (1 - sl_pct)
    long_take_profit = close * (1 + tp_pct)
    strategy.exit("Long Exit", from_entry="Long", stop=long_stop_loss, limit=long_take_profit)

if strategy.position_size < 0
    short_stop_loss = 
```