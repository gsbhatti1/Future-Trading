``` pinescript
/*backtest
start: 2025-02-12 00:00:00
end: 2025-02-19 00:00:00
period: 1m
basePeriod: 1m
exchanges: [{"eid":"Binance","currency":"SOL_USDT"}]
*/

//@version=5
strategy("5min Triple Confirmation Crypto Strategy", overlay=true, margin_long=100, margin_short=100)

// ===== Inputs =====
fast_length = input.int(9, "Fast EMA Length")
slow_length = input.int(21, "Slow EMA Length")
rsi_length = input.int(14, "RSI Length")
volume_ma_length = input.int(20, "Volume MA Length")
atr_length = input.int(14, "ATR Length")
risk_reward = input.float(2.0, "Risk:Reward Ratio")

// ===== 1. Trend Confirmation (EMA Crossover) =====
fast_ema = ta.ema(close, fast_length)
slow_ema = ta.ema(close, slow_length)
bullish_trend = ta.crossover(fast_ema, slow_ema)
bearish_trend = ta.crossunder(fast_ema, slow_ema)

// ===== 2. Momentum Confirmation (RSI + MACD) =====
rsi = ta.rsi(close, rsi_length)
[macd_line, signal_line, _] = ta.macd(close, 12, 26, 9)

bullish_momentum = rsi > 50 and ta.crossover(macd_line, signal_line)
bearish_momentum = rsi < 50 and ta.crossunder(macd_line, signal_line)

// ===== 3. Volume Confirmation (Volume Spike + OBV) =====
volume_ma = ta.sma(volume, volume_ma_length)
volume_spike = volume > 1.8 * volume_ma
obv = ta.obv
obv_trend = ta.ema(obv, 5) > ta.ema(obv, 13)

// ===== Entry Conditions =====
long_condition = 
  bullish_trend and 
  bullish_momentum and 
  volume_spike

short_condition = 
  bearish_trend and 
  bearish_momentum and 
  volume_spike

// ===== Exit Conditions =====
atr_value = ta.atr(atr_length)
stop_loss = atr_value * risk_reward

long_stop_loss = if (bullish_trend and bullish_momentum) 
                  low - stop_loss 
                else na
short_stop_loss = if (bearish_trend and bearish_momentum) 
                   high + stop_loss 
                 else na

// === Trade Execution ====
if (long_condition)
    strategy.entry("Long", strategy.long)

if (short_condition)
    strategy.entry("Short", strategy.short)

// === Risk Management ===
strategy.exit("Take Profit Long", "Long", stop=high + atr_value * risk_reward / 2, limit=high + atr_value * risk_reward)
strategy.exit("Take Profit Short", "Short", stop=low - atr_value * risk_reward / 2, limit=low - atr_value * risk_reward)

// === Plotting ===
plotshape(series=bullish_trend and bullish_momentum and volume_spike, title="Long Entry", location=location.belowbar, color=color.green, style=shape.triangleup, size=size.small)
plotshape(series=bearish_trend and bearish_momentum and volume_spike, title="Short Entry", location=location.abovebar, color=color.red, style=shape.triangledown, size=size.small)

// === Additional Plotting for ATR Stop Loss
plot(long_stop_loss, color=color.blue)
plot(short_stop_loss, color=color.blue)
```

This Pine Script code implements the "5min Triple Confirmation Crypto Strategy" with the described layers of trend, momentum, and volume confirmations. It also includes risk management based on ATR and stop-loss levels for both long and short positions.